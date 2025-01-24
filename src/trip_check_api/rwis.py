from trip_check_api import api
from trip_check_api.consts import PDX_BOUNDS


def get_rwis_inventory() -> dict:
    return api.get(f"/v2/Rwis/Inventory?Bounds={PDX_BOUNDS}")


def get_rwis_status() -> dict:
    return api.get(f"/v2/Rwis/Status?Bounds={PDX_BOUNDS}")
