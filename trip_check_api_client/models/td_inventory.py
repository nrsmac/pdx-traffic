from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.organization_info import OrganizationInfo
  from ..models.tdi_traffic_detector import TDITrafficDetector





T = TypeVar("T", bound="TDInventory")


@_attrs_define
class TDInventory:
    """ Traffic Detector Inventory List

        Attributes:
            organization_information (Union[Unset, OrganizationInfo]): Organization Information
            traffic_detector_list (Union[Unset, list['TDITrafficDetector']]): List of Traffic Detectors
     """

    organization_information: Union[Unset, 'OrganizationInfo'] = UNSET
    traffic_detector_list: Union[Unset, list['TDITrafficDetector']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_info import OrganizationInfo
        from ..models.tdi_traffic_detector import TDITrafficDetector
        organization_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_information, Unset):
            organization_information = self.organization_information.to_dict()

        traffic_detector_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.traffic_detector_list, Unset):
            traffic_detector_list = []
            for traffic_detector_list_item_data in self.traffic_detector_list:
                traffic_detector_list_item = traffic_detector_list_item_data.to_dict()
                traffic_detector_list.append(traffic_detector_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_information is not UNSET:
            field_dict["organization-information"] = organization_information
        if traffic_detector_list is not UNSET:
            field_dict["traffic-detector-list"] = traffic_detector_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.organization_info import OrganizationInfo
        from ..models.tdi_traffic_detector import TDITrafficDetector
        d = src_dict.copy()
        _organization_information = d.pop("organization-information", UNSET)
        organization_information: Union[Unset, OrganizationInfo]
        if isinstance(_organization_information,  Unset):
            organization_information = UNSET
        else:
            organization_information = OrganizationInfo.from_dict(_organization_information)




        traffic_detector_list = []
        _traffic_detector_list = d.pop("traffic-detector-list", UNSET)
        for traffic_detector_list_item_data in (_traffic_detector_list or []):
            traffic_detector_list_item = TDITrafficDetector.from_dict(traffic_detector_list_item_data)



            traffic_detector_list.append(traffic_detector_list_item)


        td_inventory = cls(
            organization_information=organization_information,
            traffic_detector_list=traffic_detector_list,
        )


        td_inventory.additional_properties = d
        return td_inventory

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
