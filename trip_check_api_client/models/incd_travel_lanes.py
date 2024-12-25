from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.incd_lane import IncdLane





T = TypeVar("T", bound="IncdTravelLanes")


@_attrs_define
class IncdTravelLanes:
    """ Travel Lanes

        Attributes:
            decreasing_direction (Union[Unset, str]): Decreasing Direction
            decreasing_lane_count (Union[Unset, int]): Decreasing Lane Count
            increasing_direction (Union[Unset, str]): Increasing Direction
            increasing_lane_count (Union[Unset, int]): Increasing Lane Count
            lane_edge_reference (Union[Unset, str]): Lane Edge Reference
            affected_lanes (Union[Unset, list['IncdLane']]): Travel affected highway lanes
     """

    decreasing_direction: Union[Unset, str] = UNSET
    decreasing_lane_count: Union[Unset, int] = UNSET
    increasing_direction: Union[Unset, str] = UNSET
    increasing_lane_count: Union[Unset, int] = UNSET
    lane_edge_reference: Union[Unset, str] = UNSET
    affected_lanes: Union[Unset, list['IncdLane']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.incd_lane import IncdLane
        decreasing_direction = self.decreasing_direction

        decreasing_lane_count = self.decreasing_lane_count

        increasing_direction = self.increasing_direction

        increasing_lane_count = self.increasing_lane_count

        lane_edge_reference = self.lane_edge_reference

        affected_lanes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.affected_lanes, Unset):
            affected_lanes = []
            for affected_lanes_item_data in self.affected_lanes:
                affected_lanes_item = affected_lanes_item_data.to_dict()
                affected_lanes.append(affected_lanes_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if decreasing_direction is not UNSET:
            field_dict["decreasing-direction"] = decreasing_direction
        if decreasing_lane_count is not UNSET:
            field_dict["decreasing-lane-count"] = decreasing_lane_count
        if increasing_direction is not UNSET:
            field_dict["increasing-direction"] = increasing_direction
        if increasing_lane_count is not UNSET:
            field_dict["increasing-lane-count"] = increasing_lane_count
        if lane_edge_reference is not UNSET:
            field_dict["lane-edge-reference"] = lane_edge_reference
        if affected_lanes is not UNSET:
            field_dict["affected-lanes"] = affected_lanes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.incd_lane import IncdLane
        d = src_dict.copy()
        decreasing_direction = d.pop("decreasing-direction", UNSET)

        decreasing_lane_count = d.pop("decreasing-lane-count", UNSET)

        increasing_direction = d.pop("increasing-direction", UNSET)

        increasing_lane_count = d.pop("increasing-lane-count", UNSET)

        lane_edge_reference = d.pop("lane-edge-reference", UNSET)

        affected_lanes = []
        _affected_lanes = d.pop("affected-lanes", UNSET)
        for affected_lanes_item_data in (_affected_lanes or []):
            affected_lanes_item = IncdLane.from_dict(affected_lanes_item_data)



            affected_lanes.append(affected_lanes_item)


        incd_travel_lanes = cls(
            decreasing_direction=decreasing_direction,
            decreasing_lane_count=decreasing_lane_count,
            increasing_direction=increasing_direction,
            increasing_lane_count=increasing_lane_count,
            lane_edge_reference=lane_edge_reference,
            affected_lanes=affected_lanes,
        )


        incd_travel_lanes.additional_properties = d
        return incd_travel_lanes

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
