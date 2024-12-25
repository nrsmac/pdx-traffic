from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.rwis_status_site_road_weather import RwisStatusSiteRoadWeather
  from ..models.rwis_status_site_surface_condition import RwisStatusSiteSurfaceCondition





T = TypeVar("T", bound="RwisStatusSiteWeatherStation")


@_attrs_define
class RwisStatusSiteWeatherStation:
    """ RWIS Status Site Weather Station

        Attributes:
            station_id (Union[Unset, int]): RWIS Site identifier
            road_weather (Union[Unset, RwisStatusSiteRoadWeather]): RWIS Status Site Road and Weather Info
            surface_condition (Union[Unset, RwisStatusSiteSurfaceCondition]): RWIS Status Site Surface Conditions Info
     """

    station_id: Union[Unset, int] = UNSET
    road_weather: Union[Unset, 'RwisStatusSiteRoadWeather'] = UNSET
    surface_condition: Union[Unset, 'RwisStatusSiteSurfaceCondition'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.rwis_status_site_road_weather import RwisStatusSiteRoadWeather
        from ..models.rwis_status_site_surface_condition import RwisStatusSiteSurfaceCondition
        station_id = self.station_id

        road_weather: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.road_weather, Unset):
            road_weather = self.road_weather.to_dict()

        surface_condition: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.surface_condition, Unset):
            surface_condition = self.surface_condition.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if station_id is not UNSET:
            field_dict["station-id"] = station_id
        if road_weather is not UNSET:
            field_dict["RoadWeather"] = road_weather
        if surface_condition is not UNSET:
            field_dict["SurfaceCondition"] = surface_condition

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.rwis_status_site_road_weather import RwisStatusSiteRoadWeather
        from ..models.rwis_status_site_surface_condition import RwisStatusSiteSurfaceCondition
        d = src_dict.copy()
        station_id = d.pop("station-id", UNSET)

        _road_weather = d.pop("RoadWeather", UNSET)
        road_weather: Union[Unset, RwisStatusSiteRoadWeather]
        if isinstance(_road_weather,  Unset):
            road_weather = UNSET
        else:
            road_weather = RwisStatusSiteRoadWeather.from_dict(_road_weather)




        _surface_condition = d.pop("SurfaceCondition", UNSET)
        surface_condition: Union[Unset, RwisStatusSiteSurfaceCondition]
        if isinstance(_surface_condition,  Unset):
            surface_condition = UNSET
        else:
            surface_condition = RwisStatusSiteSurfaceCondition.from_dict(_surface_condition)




        rwis_status_site_weather_station = cls(
            station_id=station_id,
            road_weather=road_weather,
            surface_condition=surface_condition,
        )


        rwis_status_site_weather_station.additional_properties = d
        return rwis_status_site_weather_station

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
