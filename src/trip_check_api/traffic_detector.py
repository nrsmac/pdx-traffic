from trip_check_api import api


def get_traffic_detector_inventory() -> dict:
    return api.get("/TrafficDetector/Inventory")


def get_traffic_detector_ramp() -> dict:
    return api.get("/TrafficDetector/Ramp")


def get_traffic_detector_roadway() -> dict:
    return api.get("/TrafficDetector/Roadway")
