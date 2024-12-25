from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="RWEndLocation")


@_attrs_define
class RWEndLocation:
    """ End Location

        Attributes:
            end_lat (Union[Unset, float]): End geographic latitude
            end_long (Union[Unset, float]): End geographic longitude
            end_milepost (Union[Unset, float]): End milepost
     """

    end_lat: Union[Unset, float] = UNSET
    end_long: Union[Unset, float] = UNSET
    end_milepost: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        end_lat = self.end_lat

        end_long = self.end_long

        end_milepost = self.end_milepost


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if end_lat is not UNSET:
            field_dict["end-lat"] = end_lat
        if end_long is not UNSET:
            field_dict["end-long"] = end_long
        if end_milepost is not UNSET:
            field_dict["end-milepost"] = end_milepost

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        end_lat = d.pop("end-lat", UNSET)

        end_long = d.pop("end-long", UNSET)

        end_milepost = d.pop("end-milepost", UNSET)

        rw_end_location = cls(
            end_lat=end_lat,
            end_long=end_long,
            end_milepost=end_milepost,
        )


        rw_end_location.additional_properties = d
        return rw_end_location

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
