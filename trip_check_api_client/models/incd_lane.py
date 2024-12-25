from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="IncdLane")


@_attrs_define
class IncdLane:
    """ Incident Lane

        Attributes:
            lane_id (Union[Unset, str]): Descriptor of which lane is affected
            lane_type (Union[Unset, str]): Type of lane affected
            direction (Union[Unset, str]): Direction of the affected lanes
     """

    lane_id: Union[Unset, str] = UNSET
    lane_type: Union[Unset, str] = UNSET
    direction: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        lane_id = self.lane_id

        lane_type = self.lane_type

        direction = self.direction


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if lane_id is not UNSET:
            field_dict["lane-id"] = lane_id
        if lane_type is not UNSET:
            field_dict["lane-type"] = lane_type
        if direction is not UNSET:
            field_dict["direction"] = direction

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        lane_id = d.pop("lane-id", UNSET)

        lane_type = d.pop("lane-type", UNSET)

        direction = d.pop("direction", UNSET)

        incd_lane = cls(
            lane_id=lane_id,
            lane_type=lane_type,
            direction=direction,
        )


        incd_lane.additional_properties = d
        return incd_lane

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
