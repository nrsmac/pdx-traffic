from trip_check_api import api


def get_cls_inventory() -> dict:
    return api.get("/Cls/Inventory")


def get_cls_length() -> dict:
    return api.get("/Cls/Length")


def get_cls_speed() -> dict:
    return api.get("/Cls/Speed")
