from dagster import ConfigurableIOManager, EnvVar, InputContext, OutputContext
import pandas as pd
from psycopg2 import OperationalError
from sqlalchemy import create_engine

class PostgresIOManager(ConfigurableIOManager):
    user: str = EnvVar('POSTGRES_USER')
    password: str = EnvVar('POSTGRES_PASSWORD')
    host: str = 'localhost'
    port: int = 5432
    db: str = 'postgres'

    def _get_url(self):
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"

    def handle_output(self, context: OutputContext, obj):
        table_name = f"{context.asset_key.path[-1]}"
        
        # Create SQLAlchemy engine
        engine = create_engine(self._get_url())
        
        try:
            # Write dataframe to SQL
            obj.to_sql(
                name=table_name,
                con=engine,
                if_exists='append',
                index=False
            )
            
            print(f"Dataframe written to {table_name} successfully")
        except OperationalError as e:
            print(f"Error writing to {table_name}: {e}")

    def load_input(self, context):
        table_name = f"{context.asset_key.path[-1]}"
        
        # Create SQLAlchemy engine
        engine = create_engine(self._get_url())
        
        try:
            df = pd.read_sql(f"SELECT * FROM {table_name}", con=engine)
            
            print(f"Dataframe loaded from {table_name} successfully")
            return df
        except OperationalError as e:
            print(f"Error loading data from {table_name}: {e}")
            raise
