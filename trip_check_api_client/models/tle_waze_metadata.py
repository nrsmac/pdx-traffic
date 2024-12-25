from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.waze_incident_items import WazeIncidentItems
  from ..models.organization_info import OrganizationInfo
  from ..models.tle_incident_items import TleIncidentItems





T = TypeVar("T", bound="TLEWazeMetadata")


@_attrs_define
class TLEWazeMetadata:
    """ All Incidents Metadata

        Attributes:
            organization_information (Union[Unset, OrganizationInfo]): Organization Information
            tle_incident_items (Union[Unset, TleIncidentItems]): Class to hold the arrays of different TLE incident metadata
                items
            waze_incident_items (Union[Unset, WazeIncidentItems]): Class to hold the arrays of different TLE incident
                metadata items
     """

    organization_information: Union[Unset, 'OrganizationInfo'] = UNSET
    tle_incident_items: Union[Unset, 'TleIncidentItems'] = UNSET
    waze_incident_items: Union[Unset, 'WazeIncidentItems'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.waze_incident_items import WazeIncidentItems
        from ..models.organization_info import OrganizationInfo
        from ..models.tle_incident_items import TleIncidentItems
        organization_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_information, Unset):
            organization_information = self.organization_information.to_dict()

        tle_incident_items: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tle_incident_items, Unset):
            tle_incident_items = self.tle_incident_items.to_dict()

        waze_incident_items: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.waze_incident_items, Unset):
            waze_incident_items = self.waze_incident_items.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_information is not UNSET:
            field_dict["organization-information"] = organization_information
        if tle_incident_items is not UNSET:
            field_dict["TLE-incident-items"] = tle_incident_items
        if waze_incident_items is not UNSET:
            field_dict["Waze-incident-items"] = waze_incident_items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.waze_incident_items import WazeIncidentItems
        from ..models.organization_info import OrganizationInfo
        from ..models.tle_incident_items import TleIncidentItems
        d = src_dict.copy()
        _organization_information = d.pop("organization-information", UNSET)
        organization_information: Union[Unset, OrganizationInfo]
        if isinstance(_organization_information,  Unset):
            organization_information = UNSET
        else:
            organization_information = OrganizationInfo.from_dict(_organization_information)




        _tle_incident_items = d.pop("TLE-incident-items", UNSET)
        tle_incident_items: Union[Unset, TleIncidentItems]
        if isinstance(_tle_incident_items,  Unset):
            tle_incident_items = UNSET
        else:
            tle_incident_items = TleIncidentItems.from_dict(_tle_incident_items)




        _waze_incident_items = d.pop("Waze-incident-items", UNSET)
        waze_incident_items: Union[Unset, WazeIncidentItems]
        if isinstance(_waze_incident_items,  Unset):
            waze_incident_items = UNSET
        else:
            waze_incident_items = WazeIncidentItems.from_dict(_waze_incident_items)




        tle_waze_metadata = cls(
            organization_information=organization_information,
            tle_incident_items=tle_incident_items,
            waze_incident_items=waze_incident_items,
        )


        tle_waze_metadata.additional_properties = d
        return tle_waze_metadata

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
