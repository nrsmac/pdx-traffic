from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TleIncidentType")


@_attrs_define
class TleIncidentType:
    """ Class to hold details about an individual TLE incident type

        Attributes:
            type_id (Union[Unset, int]): Id of TLE incident type
            type_ (Union[Unset, str]): Description of TLE incident type
     """

    type_id: Union[Unset, int] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        type_id = self.type_id

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_id is not UNSET:
            field_dict["type-id"] = type_id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_id = d.pop("type-id", UNSET)

        type_ = d.pop("type", UNSET)

        tle_incident_type = cls(
            type_id=type_id,
            type_=type_,
        )


        tle_incident_type.additional_properties = d
        return tle_incident_type

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