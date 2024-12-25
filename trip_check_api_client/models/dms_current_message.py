from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="DmsCurrentMessage")


@_attrs_define
class DmsCurrentMessage:
    """ Current message on the sign

        Attributes:
            phase_1_line_1 (Union[Unset, str]): Message 1 Line 1
            phase_1_line_2 (Union[Unset, str]): Message 1 Line 2
            phase_1_line_3 (Union[Unset, str]): Message 1 Line 3
            phase_2_line_1 (Union[Unset, str]): Message 2 Line 1
            phase_2_line_2 (Union[Unset, str]): Message 2 Line 2
            phase_2_line_3 (Union[Unset, str]): Message 2 Line 3
     """

    phase_1_line_1: Union[Unset, str] = UNSET
    phase_1_line_2: Union[Unset, str] = UNSET
    phase_1_line_3: Union[Unset, str] = UNSET
    phase_2_line_1: Union[Unset, str] = UNSET
    phase_2_line_2: Union[Unset, str] = UNSET
    phase_2_line_3: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        phase_1_line_1 = self.phase_1_line_1

        phase_1_line_2 = self.phase_1_line_2

        phase_1_line_3 = self.phase_1_line_3

        phase_2_line_1 = self.phase_2_line_1

        phase_2_line_2 = self.phase_2_line_2

        phase_2_line_3 = self.phase_2_line_3


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if phase_1_line_1 is not UNSET:
            field_dict["phase1Line1"] = phase_1_line_1
        if phase_1_line_2 is not UNSET:
            field_dict["phase1Line2"] = phase_1_line_2
        if phase_1_line_3 is not UNSET:
            field_dict["phase1Line3"] = phase_1_line_3
        if phase_2_line_1 is not UNSET:
            field_dict["phase2Line1"] = phase_2_line_1
        if phase_2_line_2 is not UNSET:
            field_dict["phase2Line2"] = phase_2_line_2
        if phase_2_line_3 is not UNSET:
            field_dict["phase2Line3"] = phase_2_line_3

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        phase_1_line_1 = d.pop("phase1Line1", UNSET)

        phase_1_line_2 = d.pop("phase1Line2", UNSET)

        phase_1_line_3 = d.pop("phase1Line3", UNSET)

        phase_2_line_1 = d.pop("phase2Line1", UNSET)

        phase_2_line_2 = d.pop("phase2Line2", UNSET)

        phase_2_line_3 = d.pop("phase2Line3", UNSET)

        dms_current_message = cls(
            phase_1_line_1=phase_1_line_1,
            phase_1_line_2=phase_1_line_2,
            phase_1_line_3=phase_1_line_3,
            phase_2_line_1=phase_2_line_1,
            phase_2_line_2=phase_2_line_2,
            phase_2_line_3=phase_2_line_3,
        )


        dms_current_message.additional_properties = d
        return dms_current_message

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
