from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime






T = TypeVar("T", bound="RwisStatusSiteRoadWeather")


@_attrs_define
class RwisStatusSiteRoadWeather:
    """ RWIS Status Site Road and Weather Info

        Attributes:
            air_temperature (Union[Unset, int]): Air temperature
            atmospheric_pressure (Union[Unset, int]): Atmospheric pressure
            avg_wind_direction (Union[Unset, int]): Average wind direction
            avg_wind_gust_direction (Union[Unset, int]): Average wind gust direction
            avg_wind_gust_speed (Union[Unset, int]): Average wind gust speed
            avg_wind_speed (Union[Unset, int]): Average wind speed
            dewpoint_temp (Union[Unset, int]): Dewpoint temperature
            last_update_time (Union[Unset, datetime.datetime]): Last update time
            max_temp (Union[Unset, int]): Maximum temperature
            min_temp (Union[Unset, int]): Minimum temperature
            precip_intensity (Union[Unset, str]): Precipitation intensity
            precip_rate (Union[Unset, int]): Precipitation rate
            precip_type (Union[Unset, str]): Precipitation type
            relative_humidity (Union[Unset, int]): Relative humidity
            visibility (Union[Unset, int]): Visibility
     """

    air_temperature: Union[Unset, int] = UNSET
    atmospheric_pressure: Union[Unset, int] = UNSET
    avg_wind_direction: Union[Unset, int] = UNSET
    avg_wind_gust_direction: Union[Unset, int] = UNSET
    avg_wind_gust_speed: Union[Unset, int] = UNSET
    avg_wind_speed: Union[Unset, int] = UNSET
    dewpoint_temp: Union[Unset, int] = UNSET
    last_update_time: Union[Unset, datetime.datetime] = UNSET
    max_temp: Union[Unset, int] = UNSET
    min_temp: Union[Unset, int] = UNSET
    precip_intensity: Union[Unset, str] = UNSET
    precip_rate: Union[Unset, int] = UNSET
    precip_type: Union[Unset, str] = UNSET
    relative_humidity: Union[Unset, int] = UNSET
    visibility: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        air_temperature = self.air_temperature

        atmospheric_pressure = self.atmospheric_pressure

        avg_wind_direction = self.avg_wind_direction

        avg_wind_gust_direction = self.avg_wind_gust_direction

        avg_wind_gust_speed = self.avg_wind_gust_speed

        avg_wind_speed = self.avg_wind_speed

        dewpoint_temp = self.dewpoint_temp

        last_update_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_update_time, Unset):
            last_update_time = self.last_update_time.isoformat()

        max_temp = self.max_temp

        min_temp = self.min_temp

        precip_intensity = self.precip_intensity

        precip_rate = self.precip_rate

        precip_type = self.precip_type

        relative_humidity = self.relative_humidity

        visibility = self.visibility


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if air_temperature is not UNSET:
            field_dict["air-temperature"] = air_temperature
        if atmospheric_pressure is not UNSET:
            field_dict["atmospheric-pressure"] = atmospheric_pressure
        if avg_wind_direction is not UNSET:
            field_dict["avg-wind-direction"] = avg_wind_direction
        if avg_wind_gust_direction is not UNSET:
            field_dict["avg-wind-gust-direction"] = avg_wind_gust_direction
        if avg_wind_gust_speed is not UNSET:
            field_dict["avg-wind-gust-speed"] = avg_wind_gust_speed
        if avg_wind_speed is not UNSET:
            field_dict["avg-wind-speed"] = avg_wind_speed
        if dewpoint_temp is not UNSET:
            field_dict["dewpoint-temp"] = dewpoint_temp
        if last_update_time is not UNSET:
            field_dict["last-update-time"] = last_update_time
        if max_temp is not UNSET:
            field_dict["max-temp"] = max_temp
        if min_temp is not UNSET:
            field_dict["min-temp"] = min_temp
        if precip_intensity is not UNSET:
            field_dict["precip-intensity"] = precip_intensity
        if precip_rate is not UNSET:
            field_dict["precip-rate"] = precip_rate
        if precip_type is not UNSET:
            field_dict["precip-type"] = precip_type
        if relative_humidity is not UNSET:
            field_dict["relative-humidity"] = relative_humidity
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        air_temperature = d.pop("air-temperature", UNSET)

        atmospheric_pressure = d.pop("atmospheric-pressure", UNSET)

        avg_wind_direction = d.pop("avg-wind-direction", UNSET)

        avg_wind_gust_direction = d.pop("avg-wind-gust-direction", UNSET)

        avg_wind_gust_speed = d.pop("avg-wind-gust-speed", UNSET)

        avg_wind_speed = d.pop("avg-wind-speed", UNSET)

        dewpoint_temp = d.pop("dewpoint-temp", UNSET)

        _last_update_time = d.pop("last-update-time", UNSET)
        last_update_time: Union[Unset, datetime.datetime]
        if isinstance(_last_update_time,  Unset):
            last_update_time = UNSET
        else:
            last_update_time = isoparse(_last_update_time)




        max_temp = d.pop("max-temp", UNSET)

        min_temp = d.pop("min-temp", UNSET)

        precip_intensity = d.pop("precip-intensity", UNSET)

        precip_rate = d.pop("precip-rate", UNSET)

        precip_type = d.pop("precip-type", UNSET)

        relative_humidity = d.pop("relative-humidity", UNSET)

        visibility = d.pop("visibility", UNSET)

        rwis_status_site_road_weather = cls(
            air_temperature=air_temperature,
            atmospheric_pressure=atmospheric_pressure,
            avg_wind_direction=avg_wind_direction,
            avg_wind_gust_direction=avg_wind_gust_direction,
            avg_wind_gust_speed=avg_wind_gust_speed,
            avg_wind_speed=avg_wind_speed,
            dewpoint_temp=dewpoint_temp,
            last_update_time=last_update_time,
            max_temp=max_temp,
            min_temp=min_temp,
            precip_intensity=precip_intensity,
            precip_rate=precip_rate,
            precip_type=precip_type,
            relative_humidity=relative_humidity,
            visibility=visibility,
        )


        rwis_status_site_road_weather.additional_properties = d
        return rwis_status_site_road_weather

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
