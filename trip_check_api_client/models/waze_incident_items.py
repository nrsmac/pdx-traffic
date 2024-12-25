from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.waze_incident_type import WazeIncidentType





T = TypeVar("T", bound="WazeIncidentItems")


@_attrs_define
class WazeIncidentItems:
    """ Class to hold the arrays of different TLE incident metadata items

        Attributes:
            waze_incd_type_list (Union[Unset, list['WazeIncidentType']]): List of possible Waze incident types
     """

    waze_incd_type_list: Union[Unset, list['WazeIncidentType']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.waze_incident_type import WazeIncidentType
        waze_incd_type_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.waze_incd_type_list, Unset):
            waze_incd_type_list = []
            for waze_incd_type_list_item_data in self.waze_incd_type_list:
                waze_incd_type_list_item = waze_incd_type_list_item_data.to_dict()
                waze_incd_type_list.append(waze_incd_type_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if waze_incd_type_list is not UNSET:
            field_dict["Waze-incd-type-list"] = waze_incd_type_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.waze_incident_type import WazeIncidentType
        d = src_dict.copy()
        waze_incd_type_list = []
        _waze_incd_type_list = d.pop("Waze-incd-type-list", UNSET)
        for waze_incd_type_list_item_data in (_waze_incd_type_list or []):
            waze_incd_type_list_item = WazeIncidentType.from_dict(waze_incd_type_list_item_data)



            waze_incd_type_list.append(waze_incd_type_list_item)


        waze_incident_items = cls(
            waze_incd_type_list=waze_incd_type_list,
        )


        waze_incident_items.additional_properties = d
        return waze_incident_items

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
