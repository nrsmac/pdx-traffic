from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.rwis_status_site_road_weather_v2 import RwisStatusSiteRoadWeatherV2
  from ..models.rwis_status_site_surface_condition_v2 import RwisStatusSiteSurfaceConditionV2





T = TypeVar("T", bound="RwisStatusSiteWeatherStationV2")


@_attrs_define
class RwisStatusSiteWeatherStationV2:
    """ RWIS Status Site Weather Station V2

        Attributes:
            station_id (Union[Unset, str]): RWIS Site identifier
            road_weather (Union[Unset, RwisStatusSiteRoadWeatherV2]): RWIS Status Site Road Weather V2
            surface_condition (Union[Unset, RwisStatusSiteSurfaceConditionV2]): Surface Conditions
     """

    station_id: Union[Unset, str] = UNSET
    road_weather: Union[Unset, 'RwisStatusSiteRoadWeatherV2'] = UNSET
    surface_condition: Union[Unset, 'RwisStatusSiteSurfaceConditionV2'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.rwis_status_site_road_weather_v2 import RwisStatusSiteRoadWeatherV2
        from ..models.rwis_status_site_surface_condition_v2 import RwisStatusSiteSurfaceConditionV2
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
        from ..models.rwis_status_site_road_weather_v2 import RwisStatusSiteRoadWeatherV2
        from ..models.rwis_status_site_surface_condition_v2 import RwisStatusSiteSurfaceConditionV2
        d = src_dict.copy()
        station_id = d.pop("station-id", UNSET)

        _road_weather = d.pop("RoadWeather", UNSET)
        road_weather: Union[Unset, RwisStatusSiteRoadWeatherV2]
        if isinstance(_road_weather,  Unset):
            road_weather = UNSET
        else:
            road_weather = RwisStatusSiteRoadWeatherV2.from_dict(_road_weather)




        _surface_condition = d.pop("SurfaceCondition", UNSET)
        surface_condition: Union[Unset, RwisStatusSiteSurfaceConditionV2]
        if isinstance(_surface_condition,  Unset):
            surface_condition = UNSET
        else:
            surface_condition = RwisStatusSiteSurfaceConditionV2.from_dict(_surface_condition)




        rwis_status_site_weather_station_v2 = cls(
            station_id=station_id,
            road_weather=road_weather,
            surface_condition=surface_condition,
        )


        rwis_status_site_weather_station_v2.additional_properties = d
        return rwis_status_site_weather_station_v2

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
