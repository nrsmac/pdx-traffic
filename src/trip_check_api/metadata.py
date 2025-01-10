from enum import Enum
from pprint import pprint
from typing import Annotated
from trip_check_api import api

def get_incident_event_types():
    data = api.get(f"/Incidents/Metadata")
    raw_event_types = data['incident-metadata-items']['event-types']
    flat_event_types = _unpack_type_codes(raw_event_types, 'id', 'name')
    return flat_event_types

def get_incident_event_subtypes():
    data = api.get(f"/Incidents/Metadata")
    raw_event_subtypes = data['incident-metadata-items']['event-subtypes']
    flat_event_subtypes = _unpack_type_codes(raw_event_subtypes, 'id', 'name')
    return flat_event_subtypes
    
def get_road_condition_descriptions():
    data = api.get(f"/RW/Metadata")
    raw_conditions = data['road-weather-items']['road-condition-list']
    flat_weather_conditions = _unpack_type_codes(raw_conditions, 'road-cond-id', 'road-cond-desc')
    return flat_weather_conditions

def get_weather_condition_descriptions():
    data = api.get(f"/RW/Metadata")
    raw_conditions = data['road-weather-items']['weather-condition-list']
    flat_weather_conditions = _unpack_type_codes(raw_conditions, 'weather-id', 'weather-desc')
    return flat_weather_conditions

def get_routes() -> dict:
    data = api.get(f"/Routes")
    return data['location-list']


def get_travel_impact_descriptions() -> Annotated[Enum, 'TravelImpactDescription']:
    tle_metadata = api.get(f"/Tle/TleWazeMetadata")
    raw_travel_impacts = tle_metadata['TLE-incident-items']['TLE-travel-impact-list']
    flat_travel_impacts = _unpack_type_codes(raw_travel_impacts, 'impact-id', 'impact-desc')
    return flat_travel_impacts

def get_travel_incident_types() -> Annotated[Enum, 'TravelIncidentType']:
    tle_metadata = api.get(f"/Tle/TleWazeMetadata")
    raw_incident_types = tle_metadata['TLE-incident-items']['TLE-incd-type-list']
    flat_incident_types = _unpack_type_codes(raw_incident_types, 'type-id', 'type')
    return flat_incident_types

def _unpack_type_codes(input_dict: dict, code_field_name: str, description_field_name: str) -> dict:
    flattened = {}
    for _dict in input_dict:
        code = _dict[code_field_name]
        description = _dict[description_field_name]
        flattened[description] = code
    return flattened

if __name__ == "__main__":
    metadata = [
        get_routes(),
        get_travel_incident_types(),
        get_travel_impact_descriptions(),
        get_road_condition_descriptions(),
        get_weather_condition_descriptions(),
        get_incident_event_types(),
        get_incident_event_subtypes(),
    ]