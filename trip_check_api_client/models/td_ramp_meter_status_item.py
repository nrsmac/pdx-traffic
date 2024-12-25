from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.tdr_device_status_header import TDRDeviceStatusHeader
  from ..models.tdr_metered_lane_list import TDRMeteredLaneList





T = TypeVar("T", bound="TDRampMeterStatusItem")


@_attrs_define
class TDRampMeterStatusItem:
    """ Ramp Meter Status Item

        Attributes:
            device_status_header (Union[Unset, TDRDeviceStatusHeader]): Device Status Header
            metered_lane_list (Union[Unset, list['TDRMeteredLaneList']]): Metered Lane List
            mainline_flow_rate (Union[Unset, int]): Mainline Volume
            mainline_vehicle_occupancy (Union[Unset, int]): Mainline Occupancy
            mainline_vehicle_speed (Union[Unset, int]): Mainline Vehicle Speed
     """

    device_status_header: Union[Unset, 'TDRDeviceStatusHeader'] = UNSET
    metered_lane_list: Union[Unset, list['TDRMeteredLaneList']] = UNSET
    mainline_flow_rate: Union[Unset, int] = UNSET
    mainline_vehicle_occupancy: Union[Unset, int] = UNSET
    mainline_vehicle_speed: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.tdr_device_status_header import TDRDeviceStatusHeader
        from ..models.tdr_metered_lane_list import TDRMeteredLaneList
        device_status_header: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.device_status_header, Unset):
            device_status_header = self.device_status_header.to_dict()

        metered_lane_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.metered_lane_list, Unset):
            metered_lane_list = []
            for metered_lane_list_item_data in self.metered_lane_list:
                metered_lane_list_item = metered_lane_list_item_data.to_dict()
                metered_lane_list.append(metered_lane_list_item)



        mainline_flow_rate = self.mainline_flow_rate

        mainline_vehicle_occupancy = self.mainline_vehicle_occupancy

        mainline_vehicle_speed = self.mainline_vehicle_speed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if device_status_header is not UNSET:
            field_dict["device-status-header"] = device_status_header
        if metered_lane_list is not UNSET:
            field_dict["metered-lane-list"] = metered_lane_list
        if mainline_flow_rate is not UNSET:
            field_dict["mainline-flow-rate"] = mainline_flow_rate
        if mainline_vehicle_occupancy is not UNSET:
            field_dict["mainline-vehicle-occupancy"] = mainline_vehicle_occupancy
        if mainline_vehicle_speed is not UNSET:
            field_dict["mainline-vehicle-speed"] = mainline_vehicle_speed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tdr_device_status_header import TDRDeviceStatusHeader
        from ..models.tdr_metered_lane_list import TDRMeteredLaneList
        d = src_dict.copy()
        _device_status_header = d.pop("device-status-header", UNSET)
        device_status_header: Union[Unset, TDRDeviceStatusHeader]
        if isinstance(_device_status_header,  Unset):
            device_status_header = UNSET
        else:
            device_status_header = TDRDeviceStatusHeader.from_dict(_device_status_header)




        metered_lane_list = []
        _metered_lane_list = d.pop("metered-lane-list", UNSET)
        for metered_lane_list_item_data in (_metered_lane_list or []):
            metered_lane_list_item = TDRMeteredLaneList.from_dict(metered_lane_list_item_data)



            metered_lane_list.append(metered_lane_list_item)


        mainline_flow_rate = d.pop("mainline-flow-rate", UNSET)

        mainline_vehicle_occupancy = d.pop("mainline-vehicle-occupancy", UNSET)

        mainline_vehicle_speed = d.pop("mainline-vehicle-speed", UNSET)

        td_ramp_meter_status_item = cls(
            device_status_header=device_status_header,
            metered_lane_list=metered_lane_list,
            mainline_flow_rate=mainline_flow_rate,
            mainline_vehicle_occupancy=mainline_vehicle_occupancy,
            mainline_vehicle_speed=mainline_vehicle_speed,
        )


        td_ramp_meter_status_item.additional_properties = d
        return td_ramp_meter_status_item

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
