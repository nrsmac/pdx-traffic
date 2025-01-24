from time import sleep
import pytest
from trip_check_api import metadata, cls, incidents, rwis, traffic_detector


@pytest.mark.parametrize(
    "function",
    [
        metadata.get_incident_event_types,
        metadata.get_incident_event_subtypes,
        metadata.get_road_condition_descriptions,
        metadata.get_weather_condition_descriptions,
        metadata.get_routes,
        metadata.get_travel_impact_descriptions,
        metadata.get_travel_incident_types,
        cls.get_cls_inventory,
        cls.get_cls_length,
        cls.get_cls_speed,
        incidents.get_incidents,
        rwis.get_rwis_inventory,
        rwis.get_rwis_status,
        traffic_detector.get_traffic_detector_inventory,
        traffic_detector.get_traffic_detector_ramp,
        traffic_detector.get_traffic_detector_roadway,
    ],
)
def test_trip_check_api_collectors(function):
    result = function()
    assert result is not None
    assert len(result) > 0
    sleep(2)
