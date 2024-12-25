from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.tdr_metered_lane import TDRMeteredLane





T = TypeVar("T", bound="TDRMeteredLaneList")


@_attrs_define
class TDRMeteredLaneList:
    """ Metered Lane

        Attributes:
            metered_lane (Union[Unset, TDRMeteredLane]): Metered Lane
     """

    metered_lane: Union[Unset, 'TDRMeteredLane'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.tdr_metered_lane import TDRMeteredLane
        metered_lane: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metered_lane, Unset):
            metered_lane = self.metered_lane.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if metered_lane is not UNSET:
            field_dict["metered-lane"] = metered_lane

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tdr_metered_lane import TDRMeteredLane
        d = src_dict.copy()
        _metered_lane = d.pop("metered-lane", UNSET)
        metered_lane: Union[Unset, TDRMeteredLane]
        if isinstance(_metered_lane,  Unset):
            metered_lane = UNSET
        else:
            metered_lane = TDRMeteredLane.from_dict(_metered_lane)




        tdr_metered_lane_list = cls(
            metered_lane=metered_lane,
        )


        tdr_metered_lane_list.additional_properties = d
        return tdr_metered_lane_list

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
