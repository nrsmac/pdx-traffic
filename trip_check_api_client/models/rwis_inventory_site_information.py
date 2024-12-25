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
  from ..models.rwis_inventory_site_sensor import RwisInventorySiteSensor





T = TypeVar("T", bound="RwisInventorySiteInformation")


@_attrs_define
class RwisInventorySiteInformation:
    """ RWIS Inventory Item

        Attributes:
            station_id (Union[Unset, int]): RWIS Station identifier
            station_name (Union[Unset, str]): RWIS Station name
            device_update_time (Union[Unset, datetime.datetime]): Last update time of RWIS
            latitude (Union[Unset, float]): Latitude of RWIS
            longitude (Union[Unset, float]): Longitude of RWIS location
            elevation (Union[Unset, int]): Elevation of RWIS location
            route_id (Union[Unset, str]): Route where RWIS is located
            milepoint (Union[Unset, float]): Milepoint of RWIS location
            ess_inventory_list (Union[Unset, list['RwisInventorySiteSensor']]): RWIS sensor list
     """

    station_id: Union[Unset, int] = UNSET
    station_name: Union[Unset, str] = UNSET
    device_update_time: Union[Unset, datetime.datetime] = UNSET
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    elevation: Union[Unset, int] = UNSET
    route_id: Union[Unset, str] = UNSET
    milepoint: Union[Unset, float] = UNSET
    ess_inventory_list: Union[Unset, list['RwisInventorySiteSensor']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.rwis_inventory_site_sensor import RwisInventorySiteSensor
        station_id = self.station_id

        station_name = self.station_name

        device_update_time: Union[Unset, str] = UNSET
        if not isinstance(self.device_update_time, Unset):
            device_update_time = self.device_update_time.isoformat()

        latitude = self.latitude

        longitude = self.longitude

        elevation = self.elevation

        route_id = self.route_id

        milepoint = self.milepoint

        ess_inventory_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ess_inventory_list, Unset):
            ess_inventory_list = []
            for ess_inventory_list_item_data in self.ess_inventory_list:
                ess_inventory_list_item = ess_inventory_list_item_data.to_dict()
                ess_inventory_list.append(ess_inventory_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if station_id is not UNSET:
            field_dict["station-id"] = station_id
        if station_name is not UNSET:
            field_dict["station-name"] = station_name
        if device_update_time is not UNSET:
            field_dict["device-update-time"] = device_update_time
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if elevation is not UNSET:
            field_dict["elevation"] = elevation
        if route_id is not UNSET:
            field_dict["route-id"] = route_id
        if milepoint is not UNSET:
            field_dict["milepoint"] = milepoint
        if ess_inventory_list is not UNSET:
            field_dict["ess-inventory-list"] = ess_inventory_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.rwis_inventory_site_sensor import RwisInventorySiteSensor
        d = src_dict.copy()
        station_id = d.pop("station-id", UNSET)

        station_name = d.pop("station-name", UNSET)

        _device_update_time = d.pop("device-update-time", UNSET)
        device_update_time: Union[Unset, datetime.datetime]
        if isinstance(_device_update_time,  Unset):
            device_update_time = UNSET
        else:
            device_update_time = isoparse(_device_update_time)




        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        elevation = d.pop("elevation", UNSET)

        route_id = d.pop("route-id", UNSET)

        milepoint = d.pop("milepoint", UNSET)

        ess_inventory_list = []
        _ess_inventory_list = d.pop("ess-inventory-list", UNSET)
        for ess_inventory_list_item_data in (_ess_inventory_list or []):
            ess_inventory_list_item = RwisInventorySiteSensor.from_dict(ess_inventory_list_item_data)



            ess_inventory_list.append(ess_inventory_list_item)


        rwis_inventory_site_information = cls(
            station_id=station_id,
            station_name=station_name,
            device_update_time=device_update_time,
            latitude=latitude,
            longitude=longitude,
            elevation=elevation,
            route_id=route_id,
            milepoint=milepoint,
            ess_inventory_list=ess_inventory_list,
        )


        rwis_inventory_site_information.additional_properties = d
        return rwis_inventory_site_information

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
