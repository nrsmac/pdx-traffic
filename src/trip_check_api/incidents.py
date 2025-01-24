from trip_check_api import api


def get_incidents() -> dict:
    return api.get("/Incidents")
