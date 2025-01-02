from datetime import datetime
from dagster import AssetExecutionContext, MaterializeResult, MetadataValue, asset
from dags import trip_check as tc

@asset(compute_kind='source')
def traffic_detector_inventory(context: AssetExecutionContext):
    df = tc.get_traffic_detector_inventory_df()
    table_name=''.join(context.asset_key.path)
    return df


@asset(compute_kind='source')
def traffic_detector_road_data(context: AssetExecutionContext):
    df = tc.get_traffic_detector_road_data_df()
    table_name=''.join(context.asset_key.path)
    return MaterializeResult(
        metadata={
            "num_records": len(df),  # Metadata can be any key-value pair
            "preview": MetadataValue.md(df.head().to_markdown()),
            # The `MetadataValue` class has useful static methods to build Metadata
        }
    )


@asset(compute_kind='source')
def rwis_inventory(context: AssetExecutionContext):
    """Road Conditions"""
    df = tc.get_rwis_inventory_df()
    table_name=''.join(context.asset_key.path)
    return MaterializeResult(
        metadata={
            "num_records": len(df),  # Metadata can be any key-value pair
            "preview": MetadataValue.md(df.head().to_markdown()),
            # The `MetadataValue` class has useful static methods to build Metadata
        }
    )


@asset(compute_kind='source')
def rwis_status(context: AssetExecutionContext):
    """Road Conditions"""
    df = tc.get_rwis_status_df()
    table_name=''.join(context.asset_key.path)
    return MaterializeResult(
        metadata={
            "num_records": len(df),  # Metadata can be any key-value pair
            "preview": MetadataValue.md(df.head().to_markdown()),
            # The `MetadataValue` class has useful static methods to build Metadata
        }
    )


@asset(compute_kind='source')
def cls_speed(context: AssetExecutionContext):
    df = tc.get_cls_speed_df()
    return MaterializeResult(
        metadata={
            "num_records": len(df), 
            "preview": MetadataValue.md(df.head().to_markdown()),
        }
    )


@asset(compute_kind='source')
def cls_inventory(context: AssetExecutionContext):
    df = tc.get_cls_inventory_df()
    table_name=''.join(context.asset_key.path)
    df.to_pickle(f"data/{table_name}_{datetime.now().isoformat()}")
    return MaterializeResult(
        metadata={
            "num_records": len(df),  # Metadata can be any key-value pair
            "preview": MetadataValue.md(df.head().to_markdown()),
            # The `MetadataValue` class has useful static methods to build Metadata
        }
    )
