from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.organization_info import OrganizationInfo
  from ..models.local_event import LocalEvent





T = TypeVar("T", bound="LocalEvents")


@_attrs_define
class LocalEvents:
    """ TLE Events

        Attributes:
            organization_information (Union[Unset, OrganizationInfo]): Organization Information
            incidents (Union[Unset, list['LocalEvent']]): List of TLE Events
     """

    organization_information: Union[Unset, 'OrganizationInfo'] = UNSET
    incidents: Union[Unset, list['LocalEvent']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_info import OrganizationInfo
        from ..models.local_event import LocalEvent
        organization_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_information, Unset):
            organization_information = self.organization_information.to_dict()

        incidents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.incidents, Unset):
            incidents = []
            for incidents_item_data in self.incidents:
                incidents_item = incidents_item_data.to_dict()
                incidents.append(incidents_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_information is not UNSET:
            field_dict["organization-information"] = organization_information
        if incidents is not UNSET:
            field_dict["Incidents"] = incidents

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.organization_info import OrganizationInfo
        from ..models.local_event import LocalEvent
        d = src_dict.copy()
        _organization_information = d.pop("organization-information", UNSET)
        organization_information: Union[Unset, OrganizationInfo]
        if isinstance(_organization_information,  Unset):
            organization_information = UNSET
        else:
            organization_information = OrganizationInfo.from_dict(_organization_information)




        incidents = []
        _incidents = d.pop("Incidents", UNSET)
        for incidents_item_data in (_incidents or []):
            incidents_item = LocalEvent.from_dict(incidents_item_data)



            incidents.append(incidents_item)


        local_events = cls(
            organization_information=organization_information,
            incidents=incidents,
        )


        local_events.additional_properties = d
        return local_events

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
