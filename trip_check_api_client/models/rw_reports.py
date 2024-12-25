from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.organization_info import OrganizationInfo
  from ..models.rw_report import RWReport





T = TypeVar("T", bound="RWReports")


@_attrs_define
class RWReports:
    """ Road and Weather Reports

        Attributes:
            organization_information (Union[Unset, OrganizationInfo]): Organization Information
            road_weather_reports (Union[Unset, list['RWReport']]): List of Reports
     """

    organization_information: Union[Unset, 'OrganizationInfo'] = UNSET
    road_weather_reports: Union[Unset, list['RWReport']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_info import OrganizationInfo
        from ..models.rw_report import RWReport
        organization_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_information, Unset):
            organization_information = self.organization_information.to_dict()

        road_weather_reports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.road_weather_reports, Unset):
            road_weather_reports = []
            for road_weather_reports_item_data in self.road_weather_reports:
                road_weather_reports_item = road_weather_reports_item_data.to_dict()
                road_weather_reports.append(road_weather_reports_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_information is not UNSET:
            field_dict["organization-information"] = organization_information
        if road_weather_reports is not UNSET:
            field_dict["road-weather-reports"] = road_weather_reports

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.organization_info import OrganizationInfo
        from ..models.rw_report import RWReport
        d = src_dict.copy()
        _organization_information = d.pop("organization-information", UNSET)
        organization_information: Union[Unset, OrganizationInfo]
        if isinstance(_organization_information,  Unset):
            organization_information = UNSET
        else:
            organization_information = OrganizationInfo.from_dict(_organization_information)




        road_weather_reports = []
        _road_weather_reports = d.pop("road-weather-reports", UNSET)
        for road_weather_reports_item_data in (_road_weather_reports or []):
            road_weather_reports_item = RWReport.from_dict(road_weather_reports_item_data)



            road_weather_reports.append(road_weather_reports_item)


        rw_reports = cls(
            organization_information=organization_information,
            road_weather_reports=road_weather_reports,
        )


        rw_reports.additional_properties = d
        return rw_reports

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
