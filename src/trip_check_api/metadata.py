from trip_check_api import api


def get_incident_event_types() -> dict:
    return api.get("/Incidents/Metadata")


def get_incident_event_subtypes() -> dict:
    return api.get("/Incidents/Metadata")


def get_road_condition_descriptions() -> dict:
    return api.get("/RW/Metadata")


def get_weather_condition_descriptions() -> dict:
    return api.get("/RW/Metadata")


def get_routes() -> dict:
    return api.get("/Routes")


def get_travel_impact_descriptions() -> dict:
    return api.get("/Tle/TleWazeMetadata")


def get_travel_incident_types() -> dict:
    return api.get("/Tle/TleWazeMetadata")
