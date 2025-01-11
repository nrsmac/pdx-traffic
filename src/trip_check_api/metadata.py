from enum import Enum
from pprint import pprint
import pandas as pd

from trip_check_api import api

def get_incident_event_types() -> pd.DataFrame:
    data = api.get(f"/Incidents/Metadata")
    raw_event_types = data['incident-metadata-items']['event-types']
    flat_event_types = pd.DataFrame(raw_event_types).set_index('id')
    return flat_event_types

def get_incident_event_subtypes() -> pd.DataFrame:
    data = api.get(f"/Incidents/Metadata")
    raw_event_subtypes = data['incident-metadata-items']['event-subtypes']
    flat_event_subtypes = pd.DataFrame(raw_event_subtypes).set_index('id')
    return flat_event_subtypes
    
def get_road_condition_descriptions() -> pd.DataFrame:
    data = api.get(f"/RW/Metadata")
    raw_conditions = data['road-weather-items']['road-condition-list']
    flat_weather_conditions = pd.DataFrame(raw_conditions).set_index('road-cond-id')
    return flat_weather_conditions

def get_weather_condition_descriptions() -> pd.DataFrame:
    data = api.get(f"/RW/Metadata")
    raw_conditions = data['road-weather-items']['weather-condition-list']
    flat_weather_conditions = pd.DataFrame(raw_conditions).set_index('weather-id')
    return flat_weather_conditions

def get_routes() -> pd.DataFrame:
    data = api.get(f"/Routes")
    return pd.DataFrame(data['location-list'])


def get_travel_impact_descriptions() -> pd.DataFrame:
    tle_metadata = api.get(f"/Tle/TleWazeMetadata")
    raw_travel_impacts = tle_metadata['TLE-incident-items']['TLE-travel-impact-list']
    flat_travel_impacts = pd.DataFrame(raw_travel_impacts).set_index('impact-id')
    return flat_travel_impacts

def get_travel_incident_types() -> pd.DataFrame:
    tle_metadata = api.get(f"/Tle/TleWazeMetadata")
    raw_incident_types = tle_metadata['TLE-incident-items']['TLE-incd-type-list']
    flat_incident_types = pd.DataFrame(raw_incident_types).set_index('type-id')
    return flat_incident_types
