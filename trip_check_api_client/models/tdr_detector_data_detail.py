from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime






T = TypeVar("T", bound="TDRDetectorDataDetail")


@_attrs_define
class TDRDetectorDataDetail:
    """ Detector Station

        Attributes:
            station_id (Union[Unset, int]): Station identifier
            detector_id (Union[Unset, int]): Detector Id
            lane (Union[Unset, int]): Lane
            detection_time_stamp (Union[Unset, datetime.datetime]): Detection Time Stamp
            vehicle_count (Union[Unset, int]): Vehicle Count
            vehicle_occupancy (Union[Unset, int]): Vehicle Occupancy
            detector_reliability (Union[Unset, int]): Detector Reliability
            vehicle_speed (Union[Unset, int]): Vehicle Speed
     """

    station_id: Union[Unset, int] = UNSET
    detector_id: Union[Unset, int] = UNSET
    lane: Union[Unset, int] = UNSET
    detection_time_stamp: Union[Unset, datetime.datetime] = UNSET
    vehicle_count: Union[Unset, int] = UNSET
    vehicle_occupancy: Union[Unset, int] = UNSET
    detector_reliability: Union[Unset, int] = UNSET
    vehicle_speed: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        station_id = self.station_id

        detector_id = self.detector_id

        lane = self.lane

        detection_time_stamp: Union[Unset, str] = UNSET
        if not isinstance(self.detection_time_stamp, Unset):
            detection_time_stamp = self.detection_time_stamp.isoformat()

        vehicle_count = self.vehicle_count

        vehicle_occupancy = self.vehicle_occupancy

        detector_reliability = self.detector_reliability

        vehicle_speed = self.vehicle_speed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if station_id is not UNSET:
            field_dict["station-id"] = station_id
        if detector_id is not UNSET:
            field_dict["detector-id"] = detector_id
        if lane is not UNSET:
            field_dict["lane"] = lane
        if detection_time_stamp is not UNSET:
            field_dict["detection-time-stamp"] = detection_time_stamp
        if vehicle_count is not UNSET:
            field_dict["vehicle-count"] = vehicle_count
        if vehicle_occupancy is not UNSET:
            field_dict["vehicle-occupancy"] = vehicle_occupancy
        if detector_reliability is not UNSET:
            field_dict["detector-reliability"] = detector_reliability
        if vehicle_speed is not UNSET:
            field_dict["vehicle-speed"] = vehicle_speed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        station_id = d.pop("station-id", UNSET)

        detector_id = d.pop("detector-id", UNSET)

        lane = d.pop("lane", UNSET)

        _detection_time_stamp = d.pop("detection-time-stamp", UNSET)
        detection_time_stamp: Union[Unset, datetime.datetime]
        if isinstance(_detection_time_stamp,  Unset):
            detection_time_stamp = UNSET
        else:
            detection_time_stamp = isoparse(_detection_time_stamp)




        vehicle_count = d.pop("vehicle-count", UNSET)

        vehicle_occupancy = d.pop("vehicle-occupancy", UNSET)

        detector_reliability = d.pop("detector-reliability", UNSET)

        vehicle_speed = d.pop("vehicle-speed", UNSET)

        tdr_detector_data_detail = cls(
            station_id=station_id,
            detector_id=detector_id,
            lane=lane,
            detection_time_stamp=detection_time_stamp,
            vehicle_count=vehicle_count,
            vehicle_occupancy=vehicle_occupancy,
            detector_reliability=detector_reliability,
            vehicle_speed=vehicle_speed,
        )


        tdr_detector_data_detail.additional_properties = d
        return tdr_detector_data_detail

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
