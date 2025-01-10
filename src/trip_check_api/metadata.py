from enum import Enum
from pprint import pprint
from trip_check_api import api


# Metadata: All Incidents -- incident types
def get_metadata_all_incidents():
    data = api.get(f"/Incidents/Metadata")
    return data
    
# Metadata: Road and Weather
def get_metadata_road_and_weather():
    data = api.get(f"/RW/Metadata")
    return data

# Metadata: Routes
def get_metadata_routes():
    data = api.get(f"/Routes")
    return data

# Metadata: TLE and Waze Incidents -- incident metadata
def get_metadata_tle_and_waze_incidents():
    data = api.get(f"/Tle/TleWazeMetadata")
    return data

def get_all_metadata_json():
    return {
        'all_incidents': get_metadata_all_incidents(),
        'road_and_weather': get_metadata_road_and_weather(),
        'routes': get_metadata_routes(),
        'tle_and_waze_incidents': get_metadata_tle_and_waze_incidents()
    }

def get_travel_impact_descriptions(tle_metadata: dict):
    raw_travel_impacts = tle_metadata['TLE-incident-items']['TLE-travel-impact-list']
    flat_travel_impacts = {}
    for _dict in raw_travel_impacts:
        code = _dict['impact-id']
        description = _dict['impact-desc']
        flat_travel_impacts[description] = code
        
    print(flat_travel_impacts)
    return Enum('TravelImpactDescriptions', flat_travel_impacts)

if __name__ == "__main__":
    tle_metadata = get_metadata_tle_and_waze_incidents()
    pprint(get_travel_impact_descriptions(tle_metadata=tle_metadata))