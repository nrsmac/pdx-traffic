from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="DmsInventoryItem")


@_attrs_define
class DmsInventoryItem:
    """ DMS Inventory Item

        Attributes:
            device_id (Union[Unset, int]): The unique device identifier
            device_name (Union[Unset, str]): Device name and descriptor
            latitude (Union[Unset, float]): Geographic latitude
            longitude (Union[Unset, float]): Geographic longitude
            elevation (Union[Unset, int]): Elevation/altitude above sea level
            route_id (Union[Unset, str]): Route identifier
            milepoint (Union[Unset, float]): Device milepoint location
            class_ (Union[Unset, str]): Device class
            subclass (Union[Unset, str]): Device subclass
     """

    device_id: Union[Unset, int] = UNSET
    device_name: Union[Unset, str] = UNSET
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    elevation: Union[Unset, int] = UNSET
    route_id: Union[Unset, str] = UNSET
    milepoint: Union[Unset, float] = UNSET
    class_: Union[Unset, str] = UNSET
    subclass: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        device_name = self.device_name

        latitude = self.latitude

        longitude = self.longitude

        elevation = self.elevation

        route_id = self.route_id

        milepoint = self.milepoint

        class_ = self.class_

        subclass = self.subclass


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if device_id is not UNSET:
            field_dict["device-id"] = device_id
        if device_name is not UNSET:
            field_dict["device-name"] = device_name
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if elevation is not UNSET:
            field_dict["elevation"] = elevation
        if route_id is not UNSET:
            field_dict["route-id"] = route_id
        if milepoint is not UNSET:
            field_dict["milepoint"] = milepoint
        if class_ is not UNSET:
            field_dict["class"] = class_
        if subclass is not UNSET:
            field_dict["subclass"] = subclass

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        device_id = d.pop("device-id", UNSET)

        device_name = d.pop("device-name", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        elevation = d.pop("elevation", UNSET)

        route_id = d.pop("route-id", UNSET)

        milepoint = d.pop("milepoint", UNSET)

        class_ = d.pop("class", UNSET)

        subclass = d.pop("subclass", UNSET)

        dms_inventory_item = cls(
            device_id=device_id,
            device_name=device_name,
            latitude=latitude,
            longitude=longitude,
            elevation=elevation,
            route_id=route_id,
            milepoint=milepoint,
            class_=class_,
            subclass=subclass,
        )


        dms_inventory_item.additional_properties = d
        return dms_inventory_item

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
