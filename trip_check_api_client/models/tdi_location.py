from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TDILocation")


@_attrs_define
class TDILocation:
    """ Traffic Detector Inventory Location

        Attributes:
            highway_name (Union[Unset, str]): Highway name
            location_name (Union[Unset, str]): Location name
            location_id (Union[Unset, int]): Location identifier
            latitude (Union[Unset, float]): Geographic latitude
            longitude (Union[Unset, float]): Geographic longitude
            milepoint (Union[Unset, float]): Milepoint
            highway_direction (Union[Unset, str]): Highway Direction
     """

    highway_name: Union[Unset, str] = UNSET
    location_name: Union[Unset, str] = UNSET
    location_id: Union[Unset, int] = UNSET
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    milepoint: Union[Unset, float] = UNSET
    highway_direction: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        highway_name = self.highway_name

        location_name = self.location_name

        location_id = self.location_id

        latitude = self.latitude

        longitude = self.longitude

        milepoint = self.milepoint

        highway_direction = self.highway_direction


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if highway_name is not UNSET:
            field_dict["highway-name"] = highway_name
        if location_name is not UNSET:
            field_dict["location-name"] = location_name
        if location_id is not UNSET:
            field_dict["location-id"] = location_id
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if milepoint is not UNSET:
            field_dict["milepoint"] = milepoint
        if highway_direction is not UNSET:
            field_dict["highway-direction"] = highway_direction

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        highway_name = d.pop("highway-name", UNSET)

        location_name = d.pop("location-name", UNSET)

        location_id = d.pop("location-id", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        milepoint = d.pop("milepoint", UNSET)

        highway_direction = d.pop("highway-direction", UNSET)

        tdi_location = cls(
            highway_name=highway_name,
            location_name=location_name,
            location_id=location_id,
            latitude=latitude,
            longitude=longitude,
            milepoint=milepoint,
            highway_direction=highway_direction,
        )


        tdi_location.additional_properties = d
        return tdi_location

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
