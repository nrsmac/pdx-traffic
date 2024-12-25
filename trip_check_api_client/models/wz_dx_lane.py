from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="WZDxLane")


@_attrs_define
class WZDxLane:
    """ Open Lanes

        Attributes:
            lane_edge_reference (Union[Unset, str]): Lane Edge Reference
            lane_number (Union[Unset, str]): Lane Number
            lane_status (Union[Unset, str]): Lane Status
            lane_type (Union[Unset, str]): Lane Type
     """

    lane_edge_reference: Union[Unset, str] = UNSET
    lane_number: Union[Unset, str] = UNSET
    lane_status: Union[Unset, str] = UNSET
    lane_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        lane_edge_reference = self.lane_edge_reference

        lane_number = self.lane_number

        lane_status = self.lane_status

        lane_type = self.lane_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if lane_edge_reference is not UNSET:
            field_dict["LaneEdgeReference"] = lane_edge_reference
        if lane_number is not UNSET:
            field_dict["LaneNumber"] = lane_number
        if lane_status is not UNSET:
            field_dict["LaneStatus"] = lane_status
        if lane_type is not UNSET:
            field_dict["LaneType"] = lane_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        lane_edge_reference = d.pop("LaneEdgeReference", UNSET)

        lane_number = d.pop("LaneNumber", UNSET)

        lane_status = d.pop("LaneStatus", UNSET)

        lane_type = d.pop("LaneType", UNSET)

        wz_dx_lane = cls(
            lane_edge_reference=lane_edge_reference,
            lane_number=lane_number,
            lane_status=lane_status,
            lane_type=lane_type,
        )


        wz_dx_lane.additional_properties = d
        return wz_dx_lane

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
