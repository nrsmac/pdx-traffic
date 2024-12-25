from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="RWDrivingRestriction")


@_attrs_define
class RWDrivingRestriction:
    """ Driving Restriction

        Attributes:
            restriction_id (Union[Unset, str]): Restriction Id
            restriction_start_milepost (Union[Unset, float]): Restriction Start Milepost
            restriction_end_milepost (Union[Unset, float]): Restriction End Milepost
     """

    restriction_id: Union[Unset, str] = UNSET
    restriction_start_milepost: Union[Unset, float] = UNSET
    restriction_end_milepost: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        restriction_id = self.restriction_id

        restriction_start_milepost = self.restriction_start_milepost

        restriction_end_milepost = self.restriction_end_milepost


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if restriction_id is not UNSET:
            field_dict["restriction-id"] = restriction_id
        if restriction_start_milepost is not UNSET:
            field_dict["restriction-start-milepost"] = restriction_start_milepost
        if restriction_end_milepost is not UNSET:
            field_dict["restriction-end-milepost"] = restriction_end_milepost

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        restriction_id = d.pop("restriction-id", UNSET)

        restriction_start_milepost = d.pop("restriction-start-milepost", UNSET)

        restriction_end_milepost = d.pop("restriction-end-milepost", UNSET)

        rw_driving_restriction = cls(
            restriction_id=restriction_id,
            restriction_start_milepost=restriction_start_milepost,
            restriction_end_milepost=restriction_end_milepost,
        )


        rw_driving_restriction.additional_properties = d
        return rw_driving_restriction

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
