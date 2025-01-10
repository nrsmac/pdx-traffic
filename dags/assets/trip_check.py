from dagster import AssetExecutionContext, Output, asset
from trip_check_api import api as tc
from trip_check_api.consts import PDX_BOUNDS, RAW_BUCKET_NAME
from dags.s3 import upload_dataframe_to_s3
from dags.util import get_current_time_str, get_materialization_key

@asset(compute_kind='source')
def incidents(context: AssetExecutionContext):
    data = tc.get(f"/Incidents?Bounds={PDX_BOUNDS}")
    upload_dataframe_to_s3(data, RAW_BUCKET_NAME, key=get_materialization_key(context))

@asset(compute_kind='source')
def metadata_all_incident(context: AssetExecutionContext):
    data = tc.get(f"/Incidents/Metadata")
    upload_dataframe_to_s3(data, RAW_BUCKET_NAME, key=get_materialization_key(context))

@asset(compute_kind='source')
def traffic_detector_inventory(context: AssetExecutionContext):
    data = tc.get(f"/TrafficDetector/inventory")
    upload_dataframe_to_s3(data, RAW_BUCKET_NAME, key=get_materialization_key(context))

@asset(compute_kind='source')
def traffic_detector_roadway(context: AssetExecutionContext):
    data = tc.get(f"/TrafficDetector/Roadway")
    upload_dataframe_to_s3(data, RAW_BUCKET_NAME, key=get_materialization_key(context))

@asset(compute_kind='source')
def rwis_inventory(context: AssetExecutionContext):
    """Road Conditions"""
    data = tc.get(f"/v2/Rwis/Inventory?Bounds={PDX_BOUNDS}")
    upload_dataframe_to_s3(data, RAW_BUCKET_NAME, key=get_materialization_key(context))

@asset(compute_kind='source')
def rwis_status(context: AssetExecutionContext):
    """Road Conditions"""
    data = tc.get(f"/v2/Rwis/Status?Bounds={PDX_BOUNDS}")
    upload_dataframe_to_s3(data, RAW_BUCKET_NAME, key=get_materialization_key(context))

@asset(compute_kind='source')
def cls_speed(context: AssetExecutionContext):
    data = tc.get('/Cls/Speed')
    upload_dataframe_to_s3(data, RAW_BUCKET_NAME, key=get_materialization_key(context))

@asset(compute_kind='source')
def cls_inventory(context: AssetExecutionContext):
    data = tc.get('/Cls/Inventory')
    upload_dataframe_to_s3(data, RAW_BUCKET_NAME, key=get_materialization_key(context))

