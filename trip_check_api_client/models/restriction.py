from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="Restriction")


@_attrs_define
class Restriction:
    """ List of all driving restriction identifiers and descriptions

        Attributes:
            restriction_id (Union[Unset, str]): Id of driving restriction
            restriction_desc (Union[Unset, str]): Description of driving restriction
     """

    restriction_id: Union[Unset, str] = UNSET
    restriction_desc: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        restriction_id = self.restriction_id

        restriction_desc = self.restriction_desc


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if restriction_id is not UNSET:
            field_dict["restriction-id"] = restriction_id
        if restriction_desc is not UNSET:
            field_dict["restriction-desc"] = restriction_desc

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        restriction_id = d.pop("restriction-id", UNSET)

        restriction_desc = d.pop("restriction-desc", UNSET)

        restriction = cls(
            restriction_id=restriction_id,
            restriction_desc=restriction_desc,
        )


        restriction.additional_properties = d
        return restriction

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
