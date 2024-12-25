from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="RWRoadConditions")


@_attrs_define
class RWRoadConditions:
    """ RoadConditions

        Attributes:
            road_cond_id (Union[Unset, float]): Road Conditions Id
     """

    road_cond_id: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        road_cond_id = self.road_cond_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if road_cond_id is not UNSET:
            field_dict["road-cond-id"] = road_cond_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        road_cond_id = d.pop("road-cond-id", UNSET)

        rw_road_conditions = cls(
            road_cond_id=road_cond_id,
        )


        rw_road_conditions.additional_properties = d
        return rw_road_conditions

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
