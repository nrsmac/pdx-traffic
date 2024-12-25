from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.rw_location import RWLocation
  from ..models.rw_road_conditions import RWRoadConditions
  from ..models.rw_weather_conditions import RWWeatherConditions
  from ..models.rw_driving_restriction import RWDrivingRestriction
  from ..models.rw_comm_vehicle_restriction import RWCommVehicleRestriction





T = TypeVar("T", bound="RWReport")


@_attrs_define
class RWReport:
    """ Road and Weather Report

        Attributes:
            station_id (Union[Unset, int]): Unique station segment identifier
            entry_time (Union[Unset, datetime.datetime]): The station segment report entry time
            expiry_time (Union[Unset, datetime.datetime]): The station segment report expiration time
            location (Union[Unset, RWLocation]): Location
            air_temperature (Union[Unset, float]): Temperature of the air in Celsius at the time the report was reported.
            snowfall_accum_rate (Union[Unset, float]): Amount of new roadside snow in centimeters since the last scheduled
                reporting time
            adjacent_snow_depth (Union[Unset, float]): Total depth of roadside snow in centimeters
            weather_conditions (Union[Unset, RWWeatherConditions]): WeatherConditions
            road_conditions (Union[Unset, RWRoadConditions]): RoadConditions
            commercial_vehicle_restriction (Union[Unset, RWCommVehicleRestriction]): Commercial Vehicle Restriction
            driving_restriction (Union[Unset, RWDrivingRestriction]): Driving Restriction
            comments (Union[Unset, str]): Comments
     """

    station_id: Union[Unset, int] = UNSET
    entry_time: Union[Unset, datetime.datetime] = UNSET
    expiry_time: Union[Unset, datetime.datetime] = UNSET
    location: Union[Unset, 'RWLocation'] = UNSET
    air_temperature: Union[Unset, float] = UNSET
    snowfall_accum_rate: Union[Unset, float] = UNSET
    adjacent_snow_depth: Union[Unset, float] = UNSET
    weather_conditions: Union[Unset, 'RWWeatherConditions'] = UNSET
    road_conditions: Union[Unset, 'RWRoadConditions'] = UNSET
    commercial_vehicle_restriction: Union[Unset, 'RWCommVehicleRestriction'] = UNSET
    driving_restriction: Union[Unset, 'RWDrivingRestriction'] = UNSET
    comments: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.rw_location import RWLocation
        from ..models.rw_road_conditions import RWRoadConditions
        from ..models.rw_weather_conditions import RWWeatherConditions
        from ..models.rw_driving_restriction import RWDrivingRestriction
        from ..models.rw_comm_vehicle_restriction import RWCommVehicleRestriction
        station_id = self.station_id

        entry_time: Union[Unset, str] = UNSET
        if not isinstance(self.entry_time, Unset):
            entry_time = self.entry_time.isoformat()

        expiry_time: Union[Unset, str] = UNSET
        if not isinstance(self.expiry_time, Unset):
            expiry_time = self.expiry_time.isoformat()

        location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        air_temperature = self.air_temperature

        snowfall_accum_rate = self.snowfall_accum_rate

        adjacent_snow_depth = self.adjacent_snow_depth

        weather_conditions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.weather_conditions, Unset):
            weather_conditions = self.weather_conditions.to_dict()

        road_conditions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.road_conditions, Unset):
            road_conditions = self.road_conditions.to_dict()

        commercial_vehicle_restriction: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.commercial_vehicle_restriction, Unset):
            commercial_vehicle_restriction = self.commercial_vehicle_restriction.to_dict()

        driving_restriction: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.driving_restriction, Unset):
            driving_restriction = self.driving_restriction.to_dict()

        comments = self.comments


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if station_id is not UNSET:
            field_dict["station-id"] = station_id
        if entry_time is not UNSET:
            field_dict["entry-time"] = entry_time
        if expiry_time is not UNSET:
            field_dict["expiry-time"] = expiry_time
        if location is not UNSET:
            field_dict["location"] = location
        if air_temperature is not UNSET:
            field_dict["air-temperature"] = air_temperature
        if snowfall_accum_rate is not UNSET:
            field_dict["snowfall-accum-rate"] = snowfall_accum_rate
        if adjacent_snow_depth is not UNSET:
            field_dict["adjacent-snow-depth"] = adjacent_snow_depth
        if weather_conditions is not UNSET:
            field_dict["weather-conditions"] = weather_conditions
        if road_conditions is not UNSET:
            field_dict["road-conditions"] = road_conditions
        if commercial_vehicle_restriction is not UNSET:
            field_dict["commercial-vehicle-restriction"] = commercial_vehicle_restriction
        if driving_restriction is not UNSET:
            field_dict["driving-restriction"] = driving_restriction
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.rw_location import RWLocation
        from ..models.rw_road_conditions import RWRoadConditions
        from ..models.rw_weather_conditions import RWWeatherConditions
        from ..models.rw_driving_restriction import RWDrivingRestriction
        from ..models.rw_comm_vehicle_restriction import RWCommVehicleRestriction
        d = src_dict.copy()
        station_id = d.pop("station-id", UNSET)

        _entry_time = d.pop("entry-time", UNSET)
        entry_time: Union[Unset, datetime.datetime]
        if isinstance(_entry_time,  Unset):
            entry_time = UNSET
        else:
            entry_time = isoparse(_entry_time)




        _expiry_time = d.pop("expiry-time", UNSET)
        expiry_time: Union[Unset, datetime.datetime]
        if isinstance(_expiry_time,  Unset):
            expiry_time = UNSET
        else:
            expiry_time = isoparse(_expiry_time)




        _location = d.pop("location", UNSET)
        location: Union[Unset, RWLocation]
        if isinstance(_location,  Unset):
            location = UNSET
        else:
            location = RWLocation.from_dict(_location)




        air_temperature = d.pop("air-temperature", UNSET)

        snowfall_accum_rate = d.pop("snowfall-accum-rate", UNSET)

        adjacent_snow_depth = d.pop("adjacent-snow-depth", UNSET)

        _weather_conditions = d.pop("weather-conditions", UNSET)
        weather_conditions: Union[Unset, RWWeatherConditions]
        if isinstance(_weather_conditions,  Unset):
            weather_conditions = UNSET
        else:
            weather_conditions = RWWeatherConditions.from_dict(_weather_conditions)




        _road_conditions = d.pop("road-conditions", UNSET)
        road_conditions: Union[Unset, RWRoadConditions]
        if isinstance(_road_conditions,  Unset):
            road_conditions = UNSET
        else:
            road_conditions = RWRoadConditions.from_dict(_road_conditions)




        _commercial_vehicle_restriction = d.pop("commercial-vehicle-restriction", UNSET)
        commercial_vehicle_restriction: Union[Unset, RWCommVehicleRestriction]
        if isinstance(_commercial_vehicle_restriction,  Unset):
            commercial_vehicle_restriction = UNSET
        else:
            commercial_vehicle_restriction = RWCommVehicleRestriction.from_dict(_commercial_vehicle_restriction)




        _driving_restriction = d.pop("driving-restriction", UNSET)
        driving_restriction: Union[Unset, RWDrivingRestriction]
        if isinstance(_driving_restriction,  Unset):
            driving_restriction = UNSET
        else:
            driving_restriction = RWDrivingRestriction.from_dict(_driving_restriction)




        comments = d.pop("comments", UNSET)

        rw_report = cls(
            station_id=station_id,
            entry_time=entry_time,
            expiry_time=expiry_time,
            location=location,
            air_temperature=air_temperature,
            snowfall_accum_rate=snowfall_accum_rate,
            adjacent_snow_depth=adjacent_snow_depth,
            weather_conditions=weather_conditions,
            road_conditions=road_conditions,
            commercial_vehicle_restriction=commercial_vehicle_restriction,
            driving_restriction=driving_restriction,
            comments=comments,
        )


        rw_report.additional_properties = d
        return rw_report

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
