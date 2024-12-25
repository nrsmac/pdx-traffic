import os
from dagster import asset
from dotenv import load_dotenv
from trip_check_api_client.api.tle import tle_get_local_events_by_filter
from trip_check_api_client.api.rwis import rwis_get_status_filter_v2
from trip_check_api_client.api.td import td_get_ramp_data_filter, td_get_roadway_data_filter
from trip_check_api_client.client import Client

load_dotenv()

AUTHKEY = os.getenv('TRIPCHECK_API_KEY')
PDX_BOUNDS = "-122.875228,45.414915,-122.631469,45.559331"

def _get_authenticated_client():
    client = Client(base_url="http://api.odot.state.or.us/tripcheck/") 
    client._headers.update({
        'Ocp-Apim-Subscription-Key': AUTHKEY
    })
    return client

def accidents():
    with _get_authenticated_client() as client:
        accidents = tle_get_local_events_by_filter.sync_detailed(client=client, bounds=PDX_BOUNDS)
    return accidents

def road_conditions():
    with _get_authenticated_client() as client:
        rwis_statuses = rwis_get_status_filter_v2.sync_detailed(client=client, bounds=PDX_BOUNDS)
    return rwis_statuses

@asset(compute_kind='API')
def traffic_detector_inventory():
    with _get_authenticated_client() as client:
        rwis_statuses = td_get_roadway_data_filter.sync_detailed(client=client)
    return rwis_statuses

def traffic_detector_road_data():
    with _get_authenticated_client() as client:
        rwis_statuses = td_get_roadway_data_filter.sync_detailed(client=client)
    return rwis_statuses

def traffic_detector_ramp_data():
    with _get_authenticated_client() as client:
        rwis_statuses = td_get_ramp_data_filter.sync_detailed(client=client)
    return rwis_statuses