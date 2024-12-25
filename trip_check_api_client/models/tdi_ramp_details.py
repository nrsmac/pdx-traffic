from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TDIRampDetails")


@_attrs_define
class TDIRampDetails:
    """ Traffic Ramp Details

        Attributes:
            ramp_id (Union[Unset, int]): Lane
            location_id (Union[Unset, int]): Location Id
            ramp_lanes (Union[Unset, int]): Ramp Lanes
     """

    ramp_id: Union[Unset, int] = UNSET
    location_id: Union[Unset, int] = UNSET
    ramp_lanes: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        ramp_id = self.ramp_id

        location_id = self.location_id

        ramp_lanes = self.ramp_lanes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ramp_id is not UNSET:
            field_dict["ramp-id"] = ramp_id
        if location_id is not UNSET:
            field_dict["location-id"] = location_id
        if ramp_lanes is not UNSET:
            field_dict["ramp-lanes"] = ramp_lanes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ramp_id = d.pop("ramp-id", UNSET)

        location_id = d.pop("location-id", UNSET)

        ramp_lanes = d.pop("ramp-lanes", UNSET)

        tdi_ramp_details = cls(
            ramp_id=ramp_id,
            location_id=location_id,
            ramp_lanes=ramp_lanes,
        )


        tdi_ramp_details.additional_properties = d
        return tdi_ramp_details

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
