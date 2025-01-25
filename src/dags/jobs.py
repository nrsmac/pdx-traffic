from dags.s3 import upload_json_to_s3
from trip_check_api import metadata, cls, incidents, rwis, traffic_detector
from trip_check_api.consts import RAW_BUCKET_NAME
from dagster import job, op
import pendulum


@op
def incident_event_types():
    data = metadata.get_incident_event_types()
    key = f"trip_check/incident_event_types/{pendulum.now().to_iso8601_string()}.json"
    upload_json_to_s3(json_=data, bucket_name=RAW_BUCKET_NAME, key=key)


@op
def incident_event_subtypes():
    data = metadata.get_incident_event_subtypes()
    key = (
        f"trip_check/incident_event_subtypes/{pendulum.now().to_iso8601_string()}.json"
    )
    upload_json_to_s3(json_=data, bucket_name=RAW_BUCKET_NAME, key=key)


@op
def road_condition_descriptions():
    data = metadata.get_road_condition_descriptions()
    key = f"trip_check/road_condition_descriptions/{pendulum.now().to_iso8601_string()}.json"
    upload_json_to_s3(json_=data, bucket_name=RAW_BUCKET_NAME, key=key)


@op
def weather_condition_descriptions():
    data = metadata.get_weather_condition_descriptions()
    key = f"trip_check/weather_condition_descriptions/{pendulum.now().to_iso8601_string()}.json"
    upload_json_to_s3(json_=data, bucket_name=RAW_BUCKET_NAME, key=key)


@op
def routes():
    data = metadata.get_routes()
    key = f"trip_check/routes/{pendulum.now().to_iso8601_string()}.json"
    upload_json_to_s3(json_=data, bucket_name=RAW_BUCKET_NAME, key=key)


@op
def travel_impact_descriptions():
    data = metadata.get_travel_impact_descriptions()
    key = f"trip_check/travel_impact_descriptions/{pendulum.now().to_iso8601_string()}.json"
    upload_json_to_s3(json_=data, bucket_name=RAW_BUCKET_NAME, key=key)


@op
def travel_incident_types():
    data = metadata.get_travel_incident_types()
    key = f"trip_check/travel_incident_types/{pendulum.now().to_iso8601_string()}.json"
    upload_json_to_s3(json_=data, bucket_name=RAW_BUCKET_NAME, key=key)


@op
def cls_inventory():
    data = cls.get_cls_inventory()
    key = f"trip_check/cls_inventory/{pendulum.now().to_iso8601_string()}.json"
    upload_json_to_s3(json_=data, bucket_name=RAW_BUCKET_NAME, key=key)


@op
def cls_length():
    data = cls.get_cls_length()
    key = f"trip_check/cls_length/{pendulum.now().to_iso8601_string()}.json"
    upload_json_to_s3(json_=data, bucket_name=RAW_BUCKET_NAME, key=key)


@op
def cls_speed():
    data = cls.get_cls_speed()
    key = f"trip_check/cls_speed/{pendulum.now().to_iso8601_string()}.json"
    upload_json_to_s3(json_=data, bucket_name=RAW_BUCKET_NAME, key=key)


@job
def cls_job():
    cls_length()
    cls_speed()


@op
def incidents_():
    data = incidents.get_incidents()
    key = f"trip_check/incidents/{pendulum.now().to_iso8601_string()}.json"
    upload_json_to_s3(json_=data, bucket_name=RAW_BUCKET_NAME, key=key)


@job
def incidents_job():
    incidents_()


@op
def rwis_inventory():
    data = rwis.get_rwis_inventory()
    key = f"trip_check/rwis_inventory/{pendulum.now().to_iso8601_string()}.json"
    upload_json_to_s3(json_=data, bucket_name=RAW_BUCKET_NAME, key=key)


@op
def rwis_status():
    data = rwis.get_rwis_status()
    key = f"trip_check/rwis_status/{pendulum.now().to_iso8601_string()}.json"
    upload_json_to_s3(json_=data, bucket_name=RAW_BUCKET_NAME, key=key)


@job
def rwis_job():
    rwis_status()


@op
def traffic_detector_inventory():
    data = traffic_detector.get_traffic_detector_inventory()
    key = f"trip_check/traffic_detector_inventory/{pendulum.now().to_iso8601_string()}.json"
    upload_json_to_s3(json_=data, bucket_name=RAW_BUCKET_NAME, key=key)


@op
def traffic_detector_ramp():
    data = traffic_detector.get_traffic_detector_ramp()
    key = f"trip_check/traffic_detector_ramp/{pendulum.now().to_iso8601_string()}.json"
    upload_json_to_s3(json_=data, bucket_name=RAW_BUCKET_NAME, key=key)


@op
def traffic_detector_roadway():
    data = traffic_detector.get_traffic_detector_roadway()
    key = (
        f"trip_check/traffic_detector_roadway/{pendulum.now().to_iso8601_string()}.json"
    )
    upload_json_to_s3(json_=data, bucket_name=RAW_BUCKET_NAME, key=key)


@job
def traffic_detector_job():
    traffic_detector_ramp()
    traffic_detector_roadway()


@job
def metadata_job():
    incident_event_types()
    incident_event_subtypes()
    road_condition_descriptions()
    weather_condition_descriptions()
    routes()
    travel_impact_descriptions()
    travel_incident_types()
    traffic_detector_inventory()
    cls_inventory()
    rwis_inventory()


all_jobs = [metadata_job, cls_job, incidents_job, rwis_job, traffic_detector_job]
