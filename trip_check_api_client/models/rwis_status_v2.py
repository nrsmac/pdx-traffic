from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.rwis_status_site_weather_station_v2 import RwisStatusSiteWeatherStationV2
  from ..models.organization_info import OrganizationInfo





T = TypeVar("T", bound="RwisStatusV2")


@_attrs_define
class RwisStatusV2:
    """ RWIS Status V2

        Attributes:
            organization_information (Union[Unset, OrganizationInfo]): Organization Information
            weather_stations (Union[Unset, list['RwisStatusSiteWeatherStationV2']]): List of RWIS Status Weather Stations
     """

    organization_information: Union[Unset, 'OrganizationInfo'] = UNSET
    weather_stations: Union[Unset, list['RwisStatusSiteWeatherStationV2']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.rwis_status_site_weather_station_v2 import RwisStatusSiteWeatherStationV2
        from ..models.organization_info import OrganizationInfo
        organization_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_information, Unset):
            organization_information = self.organization_information.to_dict()

        weather_stations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.weather_stations, Unset):
            weather_stations = []
            for weather_stations_item_data in self.weather_stations:
                weather_stations_item = weather_stations_item_data.to_dict()
                weather_stations.append(weather_stations_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_information is not UNSET:
            field_dict["organization-information"] = organization_information
        if weather_stations is not UNSET:
            field_dict["WeatherStations"] = weather_stations

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.rwis_status_site_weather_station_v2 import RwisStatusSiteWeatherStationV2
        from ..models.organization_info import OrganizationInfo
        d = src_dict.copy()
        _organization_information = d.pop("organization-information", UNSET)
        organization_information: Union[Unset, OrganizationInfo]
        if isinstance(_organization_information,  Unset):
            organization_information = UNSET
        else:
            organization_information = OrganizationInfo.from_dict(_organization_information)




        weather_stations = []
        _weather_stations = d.pop("WeatherStations", UNSET)
        for weather_stations_item_data in (_weather_stations or []):
            weather_stations_item = RwisStatusSiteWeatherStationV2.from_dict(weather_stations_item_data)



            weather_stations.append(weather_stations_item)


        rwis_status_v2 = cls(
            organization_information=organization_information,
            weather_stations=weather_stations,
        )


        rwis_status_v2.additional_properties = d
        return rwis_status_v2

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
