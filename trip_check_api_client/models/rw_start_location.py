from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="RWStartLocation")


@_attrs_define
class RWStartLocation:
    """ Begin Location

        Attributes:
            start_lat (Union[Unset, float]): Start geographic latitude
            start_long (Union[Unset, float]): Start geographic longitude
            start_milepost (Union[Unset, float]): Start milepost
     """

    start_lat: Union[Unset, float] = UNSET
    start_long: Union[Unset, float] = UNSET
    start_milepost: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        start_lat = self.start_lat

        start_long = self.start_long

        start_milepost = self.start_milepost


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if start_lat is not UNSET:
            field_dict["start-lat"] = start_lat
        if start_long is not UNSET:
            field_dict["start-long"] = start_long
        if start_milepost is not UNSET:
            field_dict["start-milepost"] = start_milepost

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        start_lat = d.pop("start-lat", UNSET)

        start_long = d.pop("start-long", UNSET)

        start_milepost = d.pop("start-milepost", UNSET)

        rw_start_location = cls(
            start_lat=start_lat,
            start_long=start_long,
            start_milepost=start_milepost,
        )


        rw_start_location.additional_properties = d
        return rw_start_location

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
