from dagster import (
    DefaultScheduleStatus,
    Definitions,
    ScheduleDefinition,
)
from dags import jobs

from trip_check_api.consts import RAW_BUCKET_NAME
from dagster_aws.s3 import S3PickleIOManager, S3Resource


# Detector Data every 2 min
traffic_detector_schedule = ScheduleDefinition(
    name="traffic_detector_schedule",
    job=jobs.traffic_detector_job,
    cron_schedule="*/2 * * * *",
    default_status=DefaultScheduleStatus.RUNNING,
)
# RWIS every 5 minutes
rwis_schedule = ScheduleDefinition(
    name="rwis_schedule",
    job=jobs.rwis_job,
    cron_schedule="*/5 * * * *",
    default_status=DefaultScheduleStatus.RUNNING,
)
# CLS every 10m
cls_schedule = ScheduleDefinition(
    name="cls_schedule",
    job=jobs.cls_job,
    cron_schedule="*/10 * * * *",
    default_status=DefaultScheduleStatus.RUNNING,
)
# Incidents every 30s, just use five minutes for now since an incident wont likely last longer than 30s
incidents_schedule = ScheduleDefinition(
    name="incidents_schedule",
    job=jobs.incidents_job,
    cron_schedule="*/5 * * * *",
    default_status=DefaultScheduleStatus.RUNNING,
)

defs = Definitions(
    schedules=[
        traffic_detector_schedule,
        rwis_schedule,
        cls_schedule,
        incidents_schedule,
    ],
    resources={
        "io_manager": S3PickleIOManager(
            s3_resource=S3Resource(),
            s3_bucket=RAW_BUCKET_NAME,
        ),
        "s3": S3Resource(),
    },
    jobs=jobs.all_jobs,
)
