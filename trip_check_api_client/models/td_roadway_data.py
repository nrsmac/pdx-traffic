from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.tdr_detector_data_item import TDRDetectorDataItem
  from ..models.organization_info import OrganizationInfo





T = TypeVar("T", bound="TDRoadwayData")


@_attrs_define
class TDRoadwayData:
    """ Traffic Detector Roadway Data

        Attributes:
            organization_information (Union[Unset, OrganizationInfo]): Organization Information
            detector_data_items (Union[Unset, list['TDRDetectorDataItem']]): List of Detector Data Items
     """

    organization_information: Union[Unset, 'OrganizationInfo'] = UNSET
    detector_data_items: Union[Unset, list['TDRDetectorDataItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.tdr_detector_data_item import TDRDetectorDataItem
        from ..models.organization_info import OrganizationInfo
        organization_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_information, Unset):
            organization_information = self.organization_information.to_dict()

        detector_data_items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.detector_data_items, Unset):
            detector_data_items = []
            for detector_data_items_item_data in self.detector_data_items:
                detector_data_items_item = detector_data_items_item_data.to_dict()
                detector_data_items.append(detector_data_items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_information is not UNSET:
            field_dict["organization-information"] = organization_information
        if detector_data_items is not UNSET:
            field_dict["detector-data-items"] = detector_data_items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tdr_detector_data_item import TDRDetectorDataItem
        from ..models.organization_info import OrganizationInfo
        d = src_dict.copy()
        _organization_information = d.pop("organization-information", UNSET)
        organization_information: Union[Unset, OrganizationInfo]
        if isinstance(_organization_information,  Unset):
            organization_information = UNSET
        else:
            organization_information = OrganizationInfo.from_dict(_organization_information)




        detector_data_items = []
        _detector_data_items = d.pop("detector-data-items", UNSET)
        for detector_data_items_item_data in (_detector_data_items or []):
            detector_data_items_item = TDRDetectorDataItem.from_dict(detector_data_items_item_data)



            detector_data_items.append(detector_data_items_item)


        td_roadway_data = cls(
            organization_information=organization_information,
            detector_data_items=detector_data_items,
        )


        td_roadway_data.additional_properties = d
        return td_roadway_data

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
