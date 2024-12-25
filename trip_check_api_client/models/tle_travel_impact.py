from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TleTravelImpact")


@_attrs_define
class TleTravelImpact:
    """ Class to hold details about an individual TLE severity category

        Attributes:
            impact_id (Union[Unset, int]): Id of TLE impact category
            impact_desc (Union[Unset, str]): Description of TLE impact category
     """

    impact_id: Union[Unset, int] = UNSET
    impact_desc: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        impact_id = self.impact_id

        impact_desc = self.impact_desc


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if impact_id is not UNSET:
            field_dict["impact-id"] = impact_id
        if impact_desc is not UNSET:
            field_dict["impact-desc"] = impact_desc

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        impact_id = d.pop("impact-id", UNSET)

        impact_desc = d.pop("impact-desc", UNSET)

        tle_travel_impact = cls(
            impact_id=impact_id,
            impact_desc=impact_desc,
        )


        tle_travel_impact.additional_properties = d
        return tle_travel_impact

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
