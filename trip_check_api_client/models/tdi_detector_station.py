from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.tdi_ramp_details import TDIRampDetails
  from ..models.tdi_roadway_detector import TDIRoadwayDetector





T = TypeVar("T", bound="TDIDetectorStation")


@_attrs_define
class TDIDetectorStation:
    """ Detector Station

        Attributes:
            station_id (Union[Unset, int]): Station identifier
            jurisdiction_id (Union[Unset, int]): Jurisdiction identifier
            item_code (Union[Unset, str]): Item Code
            station_lanes (Union[Unset, int]): Station Lanes
            station_class (Union[Unset, str]): Station Class
            controller_description (Union[Unset, str]): Item Code
            roadway_detector_list (Union[Unset, list['TDIRoadwayDetector']]): List of Roadway Detectors
            ramp_list (Union[Unset, list['TDIRampDetails']]): List of Ramps
     """

    station_id: Union[Unset, int] = UNSET
    jurisdiction_id: Union[Unset, int] = UNSET
    item_code: Union[Unset, str] = UNSET
    station_lanes: Union[Unset, int] = UNSET
    station_class: Union[Unset, str] = UNSET
    controller_description: Union[Unset, str] = UNSET
    roadway_detector_list: Union[Unset, list['TDIRoadwayDetector']] = UNSET
    ramp_list: Union[Unset, list['TDIRampDetails']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.tdi_ramp_details import TDIRampDetails
        from ..models.tdi_roadway_detector import TDIRoadwayDetector
        station_id = self.station_id

        jurisdiction_id = self.jurisdiction_id

        item_code = self.item_code

        station_lanes = self.station_lanes

        station_class = self.station_class

        controller_description = self.controller_description

        roadway_detector_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.roadway_detector_list, Unset):
            roadway_detector_list = []
            for roadway_detector_list_item_data in self.roadway_detector_list:
                roadway_detector_list_item = roadway_detector_list_item_data.to_dict()
                roadway_detector_list.append(roadway_detector_list_item)



        ramp_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ramp_list, Unset):
            ramp_list = []
            for ramp_list_item_data in self.ramp_list:
                ramp_list_item = ramp_list_item_data.to_dict()
                ramp_list.append(ramp_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if station_id is not UNSET:
            field_dict["station-id"] = station_id
        if jurisdiction_id is not UNSET:
            field_dict["jurisdiction-id"] = jurisdiction_id
        if item_code is not UNSET:
            field_dict["item-code"] = item_code
        if station_lanes is not UNSET:
            field_dict["station-lanes"] = station_lanes
        if station_class is not UNSET:
            field_dict["station-class"] = station_class
        if controller_description is not UNSET:
            field_dict["controller-description"] = controller_description
        if roadway_detector_list is not UNSET:
            field_dict["roadway-detector-list"] = roadway_detector_list
        if ramp_list is not UNSET:
            field_dict["ramp-list"] = ramp_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tdi_ramp_details import TDIRampDetails
        from ..models.tdi_roadway_detector import TDIRoadwayDetector
        d = src_dict.copy()
        station_id = d.pop("station-id", UNSET)

        jurisdiction_id = d.pop("jurisdiction-id", UNSET)

        item_code = d.pop("item-code", UNSET)

        station_lanes = d.pop("station-lanes", UNSET)

        station_class = d.pop("station-class", UNSET)

        controller_description = d.pop("controller-description", UNSET)

        roadway_detector_list = []
        _roadway_detector_list = d.pop("roadway-detector-list", UNSET)
        for roadway_detector_list_item_data in (_roadway_detector_list or []):
            roadway_detector_list_item = TDIRoadwayDetector.from_dict(roadway_detector_list_item_data)



            roadway_detector_list.append(roadway_detector_list_item)


        ramp_list = []
        _ramp_list = d.pop("ramp-list", UNSET)
        for ramp_list_item_data in (_ramp_list or []):
            ramp_list_item = TDIRampDetails.from_dict(ramp_list_item_data)



            ramp_list.append(ramp_list_item)


        tdi_detector_station = cls(
            station_id=station_id,
            jurisdiction_id=jurisdiction_id,
            item_code=item_code,
            station_lanes=station_lanes,
            station_class=station_class,
            controller_description=controller_description,
            roadway_detector_list=roadway_detector_list,
            ramp_list=ramp_list,
        )


        tdi_detector_station.additional_properties = d
        return tdi_detector_station

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
