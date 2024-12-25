from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="WZDxBeginLocation")


@_attrs_define
class WZDxBeginLocation:
    """ Work Zone Event Begin Location

        Attributes:
            road_name (Union[Unset, str]): The name of the road on which the work zone applies
            road_num (Union[Unset, str]): The designated road number
            road_direction (Union[Unset, str]): The designated direction of the roadway that is impacted by the work zone
                activity
            latitude (Union[Unset, float]): The estimated latitude along the roadway where the work zone area begins
            longitude (Union[Unset, float]): The estimated longitude along the roadway where the workzone area begins
            milepoint (Union[Unset, float]): The milepost marker along a roadway where the workzone begins
            cross_street (Union[Unset, str]): The cross street along the roadway where the work zone area begins
     """

    road_name: Union[Unset, str] = UNSET
    road_num: Union[Unset, str] = UNSET
    road_direction: Union[Unset, str] = UNSET
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    milepoint: Union[Unset, float] = UNSET
    cross_street: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        road_name = self.road_name

        road_num = self.road_num

        road_direction = self.road_direction

        latitude = self.latitude

        longitude = self.longitude

        milepoint = self.milepoint

        cross_street = self.cross_street


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if road_name is not UNSET:
            field_dict["RoadName"] = road_name
        if road_num is not UNSET:
            field_dict["RoadNum"] = road_num
        if road_direction is not UNSET:
            field_dict["RoadDirection"] = road_direction
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if milepoint is not UNSET:
            field_dict["Milepoint"] = milepoint
        if cross_street is not UNSET:
            field_dict["CrossStreet"] = cross_street

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        road_name = d.pop("RoadName", UNSET)

        road_num = d.pop("RoadNum", UNSET)

        road_direction = d.pop("RoadDirection", UNSET)

        latitude = d.pop("Latitude", UNSET)

        longitude = d.pop("Longitude", UNSET)

        milepoint = d.pop("Milepoint", UNSET)

        cross_street = d.pop("CrossStreet", UNSET)

        wz_dx_begin_location = cls(
            road_name=road_name,
            road_num=road_num,
            road_direction=road_direction,
            latitude=latitude,
            longitude=longitude,
            milepoint=milepoint,
            cross_street=cross_street,
        )


        wz_dx_begin_location.additional_properties = d
        return wz_dx_begin_location

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
