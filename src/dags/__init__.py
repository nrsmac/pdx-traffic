from dags.assets import trip_check
from dagster import AssetSelection, DefaultScheduleStatus, Definitions, ScheduleDefinition, load_assets_from_package_module
from dags import assets
from dagster_aws.s3 import S3PickleIOManager, S3Resource

from trip_check_api.consts import RAW_BUCKET_NAME


# Detector Data every 2 min
detector_schedule = ScheduleDefinition(
    name="traffic_detector_schedule",
    target=AssetSelection.groups("traffic_detector_road_data"),
    cron_schedule="*/2 * * * *",
    default_status=DefaultScheduleStatus.RUNNING,
)
# RWIS every 5
rwis_schedule = ScheduleDefinition(
    name="rwis_schedule",
    target=AssetSelection.keys("rwis_status", "rwis_inventory"),
    cron_schedule="*/5 * * * *",
    default_status=DefaultScheduleStatus.RUNNING,
)
# CLS every 10m
cls_schedule = ScheduleDefinition(
    name="cls_schedule",
    target=AssetSelection.keys("cls_speed", "cls_inventory"),
    cron_schedule="*/10 * * * *",
    default_status=DefaultScheduleStatus.RUNNING,
)
# Incidents every 30s, just use a minute for now since an incident wont likely last longer than 30s
incidents_schedule = ScheduleDefinition(
    name="incidents_schedule",
    target=AssetSelection.keys("incidents"),
    cron_schedule="*/1 * * * *",
    default_status=DefaultScheduleStatus.RUNNING,
)

defs = Definitions(
    assets=load_assets_from_package_module(trip_check, group_name='ODOT'),
    # schedules=[
    #     detector_schedule,
    #     rwis_schedule,
    #     cls_schedule,
    #     incidents_schedule
    # ],
    resources = {
        # "io_manager": S3PickleIOManager(
        #     s3_resource=S3Resource(),
        #     s3_bucket=RAW_BUCKET_NAME,
        # )
    }
)