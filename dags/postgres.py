import os
from dotenv import load_dotenv
import pandas as pd
from psycopg2 import ProgrammingError
from sqlalchemy import MetaData, create_engine, text
from sqlalchemy.exc import OperationalError
from contextlib import contextmanager

def upsert_to_postgres(table_name, df, primary_keys):
    POSTGRES_USER=os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DB='postgres'
    db_url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/{POSTGRES_DB}"
    engine = create_engine(db_url)
    metadata = MetaData()

    # Check if the table exists
    table_exists = False
    try:
        with engine.connect() as conn:
            result = conn.execute(text(f"SELECT 1 FROM pg_tables WHERE tablename = '{table_name}'"))
            table_exists = result.scalar() is not None
    except OperationalError as e:
        print(f"Error checking table existence: {e}")
        return False

    if not table_exists:
        # Create the table if it doesn't exist
        df.to_sql(table_name, engine, index=False, if_exists='fail')

        # Add primary key constraint
        with engine.connect() as conn:
            conn.execute(text(f"ALTER TABLE {table_name} ADD CONSTRAINT {table_name}_pk PRIMARY KEY ({', '.join(primary_keys)})"))
    else:
        # Ensure primary key constraint exists
        with engine.connect() as conn:
            try:
                conn.execute(text(f"ALTER TABLE {table_name} DROP CONSTRAINT IF EXISTS {table_name}_pk;"))
            except ProgrammingError:
                # Ignore if constraint doesn't exist
                pass
            
            conn.execute(text(f"ALTER TABLE {table_name} ADD CONSTRAINT {table_name}_pk PRIMARY KEY ({', '.join(primary_keys)})"))

        # Verify primary key constraint
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT conname 
                FROM pg_constraint 
                WHERE contype = 'p' AND conrelid::regclass::text = :table_name
            """), {"table_name": table_name})
            constraints = result.fetchall()
            if not constraints:
                print(f"No primary key constraint found for table {table_name}. Creating one.")
                conn.execute(text(f"ALTER TABLE {table_name} ADD CONSTRAINT {table_name}_pk PRIMARY KEY ({', '.join(primary_keys)})"))
            elif len(constraints) > 1:
                print(f"Multiple primary key constraints found for table {table_name}. Using the first one.")

    # Perform upsert operation
    temp_table_name = f"temp_{table_name}_{id(table_name)}"

    # Create a temporary table
    df.to_sql(temp_table_name, engine, index=False, if_exists='replace')

    # Prepare the upsert query
    columns = ', '.join(df.columns)
    placeholders = ', '.join(['%s'] * len(df.columns))
    update_clause = ', '.join([f"{col} = EXCLUDED.{col}" for col in df.columns if col not in primary_keys])

    upsert_query = f"""
    INSERT INTO {table_name} ({columns})
    SELECT {columns} FROM {temp_table_name}
    ON CONFLICT ({', '.join(primary_keys)})
    DO UPDATE SET {update_clause}
    """

    try:
        with engine.connect() as conn:
            conn.execute(text(upsert_query))

        # Clean up the temporary table
        with engine.connect() as conn:
            conn.execute(text(f"DROP TABLE {temp_table_name}"))
    except Exception as e:
        print(f"Error during upsert: {e}")
        raise

    return True

if __name__ == "__main__":
    load_dotenv()
    df = pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [30, 25, 35]
    })

    result = upsert_to_postgres('people', df, ['id'])
    print(f"Upsert operation {'successful' if result else 'failed'}")
