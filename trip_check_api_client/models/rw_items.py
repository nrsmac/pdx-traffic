from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.cv_restriction import CVRestriction
  from ..models.restriction import Restriction
  from ..models.road_condition import RoadCondition
  from ..models.weather_condition import WeatherCondition





T = TypeVar("T", bound="RWItems")


@_attrs_define
class RWItems:
    """ Class to hold the arrays of different road weather metadata items

        Attributes:
            weather_condition_list (Union[Unset, list['WeatherCondition']]): List of all weather condition identifiers and
                descriptions
            road_condition_list (Union[Unset, list['RoadCondition']]): List of all road condition identifiers and
                descriptions
            commercial_vehicle_restriction_list (Union[Unset, list['CVRestriction']]): List of all commercial vehicle
                restriction identifiers, types, and descriptions
            driving_restriction_list (Union[Unset, list['Restriction']]): List of all driving restriction identifiers and
                descriptions
     """

    weather_condition_list: Union[Unset, list['WeatherCondition']] = UNSET
    road_condition_list: Union[Unset, list['RoadCondition']] = UNSET
    commercial_vehicle_restriction_list: Union[Unset, list['CVRestriction']] = UNSET
    driving_restriction_list: Union[Unset, list['Restriction']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.cv_restriction import CVRestriction
        from ..models.restriction import Restriction
        from ..models.road_condition import RoadCondition
        from ..models.weather_condition import WeatherCondition
        weather_condition_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.weather_condition_list, Unset):
            weather_condition_list = []
            for weather_condition_list_item_data in self.weather_condition_list:
                weather_condition_list_item = weather_condition_list_item_data.to_dict()
                weather_condition_list.append(weather_condition_list_item)



        road_condition_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.road_condition_list, Unset):
            road_condition_list = []
            for road_condition_list_item_data in self.road_condition_list:
                road_condition_list_item = road_condition_list_item_data.to_dict()
                road_condition_list.append(road_condition_list_item)



        commercial_vehicle_restriction_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.commercial_vehicle_restriction_list, Unset):
            commercial_vehicle_restriction_list = []
            for commercial_vehicle_restriction_list_item_data in self.commercial_vehicle_restriction_list:
                commercial_vehicle_restriction_list_item = commercial_vehicle_restriction_list_item_data.to_dict()
                commercial_vehicle_restriction_list.append(commercial_vehicle_restriction_list_item)



        driving_restriction_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.driving_restriction_list, Unset):
            driving_restriction_list = []
            for driving_restriction_list_item_data in self.driving_restriction_list:
                driving_restriction_list_item = driving_restriction_list_item_data.to_dict()
                driving_restriction_list.append(driving_restriction_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if weather_condition_list is not UNSET:
            field_dict["weather-condition-list"] = weather_condition_list
        if road_condition_list is not UNSET:
            field_dict["road-condition-list"] = road_condition_list
        if commercial_vehicle_restriction_list is not UNSET:
            field_dict["commercial-vehicle-restriction-list"] = commercial_vehicle_restriction_list
        if driving_restriction_list is not UNSET:
            field_dict["driving-restriction-list"] = driving_restriction_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.cv_restriction import CVRestriction
        from ..models.restriction import Restriction
        from ..models.road_condition import RoadCondition
        from ..models.weather_condition import WeatherCondition
        d = src_dict.copy()
        weather_condition_list = []
        _weather_condition_list = d.pop("weather-condition-list", UNSET)
        for weather_condition_list_item_data in (_weather_condition_list or []):
            weather_condition_list_item = WeatherCondition.from_dict(weather_condition_list_item_data)



            weather_condition_list.append(weather_condition_list_item)


        road_condition_list = []
        _road_condition_list = d.pop("road-condition-list", UNSET)
        for road_condition_list_item_data in (_road_condition_list or []):
            road_condition_list_item = RoadCondition.from_dict(road_condition_list_item_data)



            road_condition_list.append(road_condition_list_item)


        commercial_vehicle_restriction_list = []
        _commercial_vehicle_restriction_list = d.pop("commercial-vehicle-restriction-list", UNSET)
        for commercial_vehicle_restriction_list_item_data in (_commercial_vehicle_restriction_list or []):
            commercial_vehicle_restriction_list_item = CVRestriction.from_dict(commercial_vehicle_restriction_list_item_data)



            commercial_vehicle_restriction_list.append(commercial_vehicle_restriction_list_item)


        driving_restriction_list = []
        _driving_restriction_list = d.pop("driving-restriction-list", UNSET)
        for driving_restriction_list_item_data in (_driving_restriction_list or []):
            driving_restriction_list_item = Restriction.from_dict(driving_restriction_list_item_data)



            driving_restriction_list.append(driving_restriction_list_item)


        rw_items = cls(
            weather_condition_list=weather_condition_list,
            road_condition_list=road_condition_list,
            commercial_vehicle_restriction_list=commercial_vehicle_restriction_list,
            driving_restriction_list=driving_restriction_list,
        )


        rw_items.additional_properties = d
        return rw_items

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
