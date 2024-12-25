from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TDRMeteredLane")


@_attrs_define
class TDRMeteredLane:
    """ Metered Lane

        Attributes:
            meter_implemented_action (Union[Unset, int]): Meter Implemented Action
            implemented_meter_command_source (Union[Unset, int]): Implemented Meter Command Source
            meter_implemented_plan (Union[Unset, int]): Meter Implemented Plan
            meter_implemented_rate (Union[Unset, int]): Meter Implemented Rate
            meter_implemented_vehicles_per_green (Union[Unset, int]): Implemented Vehicles Per Green
            meter_requested_action (Union[Unset, int]): Meter Requested Action
            meter_requested_plan (Union[Unset, int]): Meter Requested Plan
            meter_requested_rate (Union[Unset, int]): Meter Requested Rate
            meter_requested_vehicles_per_green (Union[Unset, int]): Meter Requested Vehicles Per Green
            metered_lane_vehicle_count (Union[Unset, int]): Metered Lane Vehicle Count
     """

    meter_implemented_action: Union[Unset, int] = UNSET
    implemented_meter_command_source: Union[Unset, int] = UNSET
    meter_implemented_plan: Union[Unset, int] = UNSET
    meter_implemented_rate: Union[Unset, int] = UNSET
    meter_implemented_vehicles_per_green: Union[Unset, int] = UNSET
    meter_requested_action: Union[Unset, int] = UNSET
    meter_requested_plan: Union[Unset, int] = UNSET
    meter_requested_rate: Union[Unset, int] = UNSET
    meter_requested_vehicles_per_green: Union[Unset, int] = UNSET
    metered_lane_vehicle_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        meter_implemented_action = self.meter_implemented_action

        implemented_meter_command_source = self.implemented_meter_command_source

        meter_implemented_plan = self.meter_implemented_plan

        meter_implemented_rate = self.meter_implemented_rate

        meter_implemented_vehicles_per_green = self.meter_implemented_vehicles_per_green

        meter_requested_action = self.meter_requested_action

        meter_requested_plan = self.meter_requested_plan

        meter_requested_rate = self.meter_requested_rate

        meter_requested_vehicles_per_green = self.meter_requested_vehicles_per_green

        metered_lane_vehicle_count = self.metered_lane_vehicle_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if meter_implemented_action is not UNSET:
            field_dict["meter-implemented-action"] = meter_implemented_action
        if implemented_meter_command_source is not UNSET:
            field_dict["implemented-meter-command-source"] = implemented_meter_command_source
        if meter_implemented_plan is not UNSET:
            field_dict["meter-implemented-plan"] = meter_implemented_plan
        if meter_implemented_rate is not UNSET:
            field_dict["meter-implemented-rate"] = meter_implemented_rate
        if meter_implemented_vehicles_per_green is not UNSET:
            field_dict["meter-implemented-vehicles-per-green"] = meter_implemented_vehicles_per_green
        if meter_requested_action is not UNSET:
            field_dict["meter-requested-action"] = meter_requested_action
        if meter_requested_plan is not UNSET:
            field_dict["meter-requested-plan"] = meter_requested_plan
        if meter_requested_rate is not UNSET:
            field_dict["meter-requested-rate"] = meter_requested_rate
        if meter_requested_vehicles_per_green is not UNSET:
            field_dict["meter-requested-vehicles-per-green"] = meter_requested_vehicles_per_green
        if metered_lane_vehicle_count is not UNSET:
            field_dict["metered-lane-vehicle-count"] = metered_lane_vehicle_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        meter_implemented_action = d.pop("meter-implemented-action", UNSET)

        implemented_meter_command_source = d.pop("implemented-meter-command-source", UNSET)

        meter_implemented_plan = d.pop("meter-implemented-plan", UNSET)

        meter_implemented_rate = d.pop("meter-implemented-rate", UNSET)

        meter_implemented_vehicles_per_green = d.pop("meter-implemented-vehicles-per-green", UNSET)

        meter_requested_action = d.pop("meter-requested-action", UNSET)

        meter_requested_plan = d.pop("meter-requested-plan", UNSET)

        meter_requested_rate = d.pop("meter-requested-rate", UNSET)

        meter_requested_vehicles_per_green = d.pop("meter-requested-vehicles-per-green", UNSET)

        metered_lane_vehicle_count = d.pop("metered-lane-vehicle-count", UNSET)

        tdr_metered_lane = cls(
            meter_implemented_action=meter_implemented_action,
            implemented_meter_command_source=implemented_meter_command_source,
            meter_implemented_plan=meter_implemented_plan,
            meter_implemented_rate=meter_implemented_rate,
            meter_implemented_vehicles_per_green=meter_implemented_vehicles_per_green,
            meter_requested_action=meter_requested_action,
            meter_requested_plan=meter_requested_plan,
            meter_requested_rate=meter_requested_rate,
            meter_requested_vehicles_per_green=meter_requested_vehicles_per_green,
            metered_lane_vehicle_count=metered_lane_vehicle_count,
        )


        tdr_metered_lane.additional_properties = d
        return tdr_metered_lane

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
