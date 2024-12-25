from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.incd_lane import IncdLane





T = TypeVar("T", bound="IncdOffHwyLanes")


@_attrs_define
class IncdOffHwyLanes:
    """ Off Highway Lanes

        Attributes:
            affected_lanes (Union[Unset, list['IncdLane']]): Off highway affected lanes
     """

    affected_lanes: Union[Unset, list['IncdLane']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.incd_lane import IncdLane
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
        if affected_lanes is not UNSET:
            field_dict["affected-lanes"] = affected_lanes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.incd_lane import IncdLane
        d = src_dict.copy()
        affected_lanes = []
        _affected_lanes = d.pop("affected-lanes", UNSET)
        for affected_lanes_item_data in (_affected_lanes or []):
            affected_lanes_item = IncdLane.from_dict(affected_lanes_item_data)



            affected_lanes.append(affected_lanes_item)


        incd_off_hwy_lanes = cls(
            affected_lanes=affected_lanes,
        )


        incd_off_hwy_lanes.additional_properties = d
        return incd_off_hwy_lanes

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
