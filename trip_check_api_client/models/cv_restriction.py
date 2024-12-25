from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="CVRestriction")


@_attrs_define
class CVRestriction:
    """ List of all commercial vehicle restriction identifiers, types, and descriptions

        Attributes:
            restriction_id (Union[Unset, int]): Id of commercial vehicle restriction
            restriction_desc (Union[Unset, str]): Description of commercial vehicle restriction
            restriction_type (Union[Unset, str]): Type of commercial vehicle restriction
     """

    restriction_id: Union[Unset, int] = UNSET
    restriction_desc: Union[Unset, str] = UNSET
    restriction_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        restriction_id = self.restriction_id

        restriction_desc = self.restriction_desc

        restriction_type = self.restriction_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if restriction_id is not UNSET:
            field_dict["restriction-id"] = restriction_id
        if restriction_desc is not UNSET:
            field_dict["restriction-desc"] = restriction_desc
        if restriction_type is not UNSET:
            field_dict["restriction-type"] = restriction_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        restriction_id = d.pop("restriction-id", UNSET)

        restriction_desc = d.pop("restriction-desc", UNSET)

        restriction_type = d.pop("restriction-type", UNSET)

        cv_restriction = cls(
            restriction_id=restriction_id,
            restriction_desc=restriction_desc,
            restriction_type=restriction_type,
        )


        cv_restriction.additional_properties = d
        return cv_restriction

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
