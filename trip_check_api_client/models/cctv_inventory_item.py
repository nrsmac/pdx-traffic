from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime






T = TypeVar("T", bound="CctvInventoryItem")


@_attrs_define
class CctvInventoryItem:
    """ CCTV Inventory Item

        Attributes:
            device_id (Union[Unset, int]): Camera identifier
            device_name (Union[Unset, str]): Camera name
            latitude (Union[Unset, float]): Geographic latitude
            longitude (Union[Unset, float]): Geographic longitude
            hwy_id (Union[Unset, str]): Highway identifier
            route_id (Union[Unset, str]): Route identifier
            milepoint (Union[Unset, float]): Camera milepoint
            cctv_url (Union[Unset, str]): CCTV image URL
            cctv_other (Union[Unset, str]): CCTV location/description
            last_update_time (Union[Unset, datetime.datetime]): Date of last update
     """

    device_id: Union[Unset, int] = UNSET
    device_name: Union[Unset, str] = UNSET
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    hwy_id: Union[Unset, str] = UNSET
    route_id: Union[Unset, str] = UNSET
    milepoint: Union[Unset, float] = UNSET
    cctv_url: Union[Unset, str] = UNSET
    cctv_other: Union[Unset, str] = UNSET
    last_update_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        device_name = self.device_name

        latitude = self.latitude

        longitude = self.longitude

        hwy_id = self.hwy_id

        route_id = self.route_id

        milepoint = self.milepoint

        cctv_url = self.cctv_url

        cctv_other = self.cctv_other

        last_update_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_update_time, Unset):
            last_update_time = self.last_update_time.isoformat()


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
        if hwy_id is not UNSET:
            field_dict["hwy-id"] = hwy_id
        if route_id is not UNSET:
            field_dict["route-id"] = route_id
        if milepoint is not UNSET:
            field_dict["milepoint"] = milepoint
        if cctv_url is not UNSET:
            field_dict["cctv-url"] = cctv_url
        if cctv_other is not UNSET:
            field_dict["cctv-other"] = cctv_other
        if last_update_time is not UNSET:
            field_dict["last-update-time"] = last_update_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        device_id = d.pop("device-id", UNSET)

        device_name = d.pop("device-name", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        hwy_id = d.pop("hwy-id", UNSET)

        route_id = d.pop("route-id", UNSET)

        milepoint = d.pop("milepoint", UNSET)

        cctv_url = d.pop("cctv-url", UNSET)

        cctv_other = d.pop("cctv-other", UNSET)

        _last_update_time = d.pop("last-update-time", UNSET)
        last_update_time: Union[Unset, datetime.datetime]
        if isinstance(_last_update_time,  Unset):
            last_update_time = UNSET
        else:
            last_update_time = isoparse(_last_update_time)




        cctv_inventory_item = cls(
            device_id=device_id,
            device_name=device_name,
            latitude=latitude,
            longitude=longitude,
            hwy_id=hwy_id,
            route_id=route_id,
            milepoint=milepoint,
            cctv_url=cctv_url,
            cctv_other=cctv_other,
            last_update_time=last_update_time,
        )


        cctv_inventory_item.additional_properties = d
        return cctv_inventory_item

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
