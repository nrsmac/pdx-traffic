import boto3
from dagster import get_dagster_logger
from dagster_aws.s3 import S3Resource
import pandas as pd
import pickle

log = get_dagster_logger()

s3_resource=S3Resource(
    region_name='us-west-2',
)

def upload_dataframe_to_s3(df, bucket_name, key):
    """
    Upload a pandas DataFrame to S3 as a pickle file.
    
    Args:
        df (pd.DataFrame): The DataFrame to upload.
        bucket_name (str): Name of the S3 bucket.
        key (str): Key/path for the object in S3.
        
    Returns:
        None
    """
    try:
        # Serialize the DataFrame to pickle
        serialized_df = pickle.dumps(df)
        
        # Create an S3 client
        s3_client = boto3.client('s3')
        
        # Upload the serialized DataFrame to S3
        s3_client.put_object(Bucket=bucket_name, Key=key, Body=serialized_df)
        log.info(f"Successfully uploaded DataFrame to S3: {key}")
    except Exception as e:
        log.error(f"Error uploading DataFrame to S3: {e}")

def download_dataframe_from_s3(bucket_name, key):
    """
    Download a serialized DataFrame from S3 and deserialize it into a pandas DataFrame.
    
    Args:
        bucket_name (str): Name of the S3 bucket.
        key (str): Key/path for the object in S3.
        
    Returns:
        pd.DataFrame: The deserialized DataFrame.
    """
    try:
        # Create an S3 client
        s3_client = boto3.client('s3')
        
        # Get the serialized DataFrame from S3
        response = s3_client.get_object(Bucket=bucket_name, Key=key)
        body = response['Body']
        serialized_df = body.read()
        
        # Deserialize the DataFrame
        df = pickle.loads(serialized_df)
        
        return df
    except Exception as e:
        log.error(f"Error downloading DataFrame from S3: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Create a sample DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
    
    # Upload the DataFrame to S3
    upload_dataframe_to_s3(df, 'pdx-traffic-raw', 'my-df')
    
    # Download and display the DataFrame from S3
    downloaded_df = download_dataframe_from_s3('pdx-traffic-raw', 'my-df')
    if downloaded_df is not None:
        print(downloaded_df)
