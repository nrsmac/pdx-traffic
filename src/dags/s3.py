import json
import boto3
from dagster import get_dagster_logger
from dagster_aws.s3 import S3Resource

log = get_dagster_logger()

s3_resource = S3Resource(
    region_name="us-west-2",
)


def upload_json_to_s3(json_: dict | list, bucket_name: str, key: str):
    """
    Upload a dictionary as json to S3 .

    Args:
        df (pd.DataFrame): The DataFrame to upload.
        bucket_name (str): Name of the S3 bucket.
        key (str): Key/path for the object in S3.

    Returns:
        None
    """
    try:
        # Serialize the DataFrame to pickle
        serialized_json = json.dumps(json_)

        # Create an S3 client
        s3_client = boto3.client("s3")

        # Upload the serialized DataFrame to S3
        s3_client.put_object(Bucket=bucket_name, Key=key, Body=serialized_json)
        log.info(f"Successfully uploaded DataFrame to S3: {key}")
    except Exception as e:
        log.error(f"Error uploading DataFrame to S3: {e}")
