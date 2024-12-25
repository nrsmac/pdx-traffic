from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.organization_info import OrganizationInfo
  from ..models.incident_metadata_items import IncidentMetadataItems





T = TypeVar("T", bound="IncdMetadata")


@_attrs_define
class IncdMetadata:
    """ All Incidents Metadata

        Attributes:
            organization_information (Union[Unset, OrganizationInfo]): Organization Information
            incident_metadata_items (Union[Unset, IncidentMetadataItems]): Class to hold the arrays of different incident
                metadata items.
     """

    organization_information: Union[Unset, 'OrganizationInfo'] = UNSET
    incident_metadata_items: Union[Unset, 'IncidentMetadataItems'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_info import OrganizationInfo
        from ..models.incident_metadata_items import IncidentMetadataItems
        organization_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_information, Unset):
            organization_information = self.organization_information.to_dict()

        incident_metadata_items: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.incident_metadata_items, Unset):
            incident_metadata_items = self.incident_metadata_items.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_information is not UNSET:
            field_dict["organization-information"] = organization_information
        if incident_metadata_items is not UNSET:
            field_dict["incident-metadata-items"] = incident_metadata_items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.organization_info import OrganizationInfo
        from ..models.incident_metadata_items import IncidentMetadataItems
        d = src_dict.copy()
        _organization_information = d.pop("organization-information", UNSET)
        organization_information: Union[Unset, OrganizationInfo]
        if isinstance(_organization_information,  Unset):
            organization_information = UNSET
        else:
            organization_information = OrganizationInfo.from_dict(_organization_information)




        _incident_metadata_items = d.pop("incident-metadata-items", UNSET)
        incident_metadata_items: Union[Unset, IncidentMetadataItems]
        if isinstance(_incident_metadata_items,  Unset):
            incident_metadata_items = UNSET
        else:
            incident_metadata_items = IncidentMetadataItems.from_dict(_incident_metadata_items)




        incd_metadata = cls(
            organization_information=organization_information,
            incident_metadata_items=incident_metadata_items,
        )


        incd_metadata.additional_properties = d
        return incd_metadata

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
