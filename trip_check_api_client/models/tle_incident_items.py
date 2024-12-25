from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.tle_travel_impact import TleTravelImpact
  from ..models.tle_incident_type import TleIncidentType





T = TypeVar("T", bound="TleIncidentItems")


@_attrs_define
class TleIncidentItems:
    """ Class to hold the arrays of different TLE incident metadata items

        Attributes:
            tle_incd_type_list (Union[Unset, list['TleIncidentType']]): List of possible TLE incident types
            tle_travel_impact_list (Union[Unset, list['TleTravelImpact']]): List of possible TLE impact categories
     """

    tle_incd_type_list: Union[Unset, list['TleIncidentType']] = UNSET
    tle_travel_impact_list: Union[Unset, list['TleTravelImpact']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.tle_travel_impact import TleTravelImpact
        from ..models.tle_incident_type import TleIncidentType
        tle_incd_type_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tle_incd_type_list, Unset):
            tle_incd_type_list = []
            for tle_incd_type_list_item_data in self.tle_incd_type_list:
                tle_incd_type_list_item = tle_incd_type_list_item_data.to_dict()
                tle_incd_type_list.append(tle_incd_type_list_item)



        tle_travel_impact_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tle_travel_impact_list, Unset):
            tle_travel_impact_list = []
            for tle_travel_impact_list_item_data in self.tle_travel_impact_list:
                tle_travel_impact_list_item = tle_travel_impact_list_item_data.to_dict()
                tle_travel_impact_list.append(tle_travel_impact_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if tle_incd_type_list is not UNSET:
            field_dict["TLE-incd-type-list"] = tle_incd_type_list
        if tle_travel_impact_list is not UNSET:
            field_dict["TLE-travel-impact-list"] = tle_travel_impact_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tle_travel_impact import TleTravelImpact
        from ..models.tle_incident_type import TleIncidentType
        d = src_dict.copy()
        tle_incd_type_list = []
        _tle_incd_type_list = d.pop("TLE-incd-type-list", UNSET)
        for tle_incd_type_list_item_data in (_tle_incd_type_list or []):
            tle_incd_type_list_item = TleIncidentType.from_dict(tle_incd_type_list_item_data)



            tle_incd_type_list.append(tle_incd_type_list_item)


        tle_travel_impact_list = []
        _tle_travel_impact_list = d.pop("TLE-travel-impact-list", UNSET)
        for tle_travel_impact_list_item_data in (_tle_travel_impact_list or []):
            tle_travel_impact_list_item = TleTravelImpact.from_dict(tle_travel_impact_list_item_data)



            tle_travel_impact_list.append(tle_travel_impact_list_item)


        tle_incident_items = cls(
            tle_incd_type_list=tle_incd_type_list,
            tle_travel_impact_list=tle_travel_impact_list,
        )


        tle_incident_items.additional_properties = d
        return tle_incident_items

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
