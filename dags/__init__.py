from dagster import AssetSelection, DefaultScheduleStatus, Definitions, ScheduleDefinition, load_assets_from_package_module
from dags import assets


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

defs = Definitions(
    assets=load_assets_from_package_module(assets),
    schedules=[
        detector_schedule,
        rwis_schedule,
        cls_schedule
    ] 
)