from datetime import datetime
from dagster import AssetExecutionContext, MaterializeResult, MetadataValue, Output, asset
from dags import trip_check as tc

@asset(compute_kind='source', io_manager_key='postgres_io_manager')
def traffic_detector_inventory(context: AssetExecutionContext):
    df = tc.get_traffic_detector_inventory_df()
    return df

@asset(compute_kind='source', io_manager_key='postgres_io_manager')
def traffic_detector_road_data(context: AssetExecutionContext):
    df = tc.get_traffic_detector_road_data_df()
    return Output(df)

@asset(compute_kind='source', io_manager_key='postgres_io_manager')
def rwis_inventory(context: AssetExecutionContext):
    """Road Conditions"""
    df = tc.get_rwis_inventory_df()
    return Output(df)


@asset(compute_kind='source', io_manager_key='postgres_io_manager')
def rwis_status(context: AssetExecutionContext):
    """Road Conditions"""
    df = tc.get_rwis_status_df()
    return Output(df) 

@asset(compute_kind='source', io_manager_key='postgres_io_manager')
def cls_speed(context: AssetExecutionContext):
    df = tc.get_cls_speed_df()
    return df

@asset(compute_kind='source', io_manager_key='postgres_io_manager')
def cls_inventory(context: AssetExecutionContext):
    df = tc.get_cls_inventory_df()
    return df
