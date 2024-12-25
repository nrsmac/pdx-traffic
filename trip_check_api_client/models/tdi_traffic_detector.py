from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.tdi_detector_station import TDIDetectorStation
  from ..models.tdi_location import TDILocation





T = TypeVar("T", bound="TDITrafficDetector")


@_attrs_define
class TDITrafficDetector:
    """ Traffic Detector

        Attributes:
            location (Union[Unset, TDILocation]): Traffic Detector Inventory Location
            detector_station (Union[Unset, TDIDetectorStation]): Detector Station
     """

    location: Union[Unset, 'TDILocation'] = UNSET
    detector_station: Union[Unset, 'TDIDetectorStation'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.tdi_detector_station import TDIDetectorStation
        from ..models.tdi_location import TDILocation
        location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        detector_station: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.detector_station, Unset):
            detector_station = self.detector_station.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if location is not UNSET:
            field_dict["location"] = location
        if detector_station is not UNSET:
            field_dict["detector-station"] = detector_station

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tdi_detector_station import TDIDetectorStation
        from ..models.tdi_location import TDILocation
        d = src_dict.copy()
        _location = d.pop("location", UNSET)
        location: Union[Unset, TDILocation]
        if isinstance(_location,  Unset):
            location = UNSET
        else:
            location = TDILocation.from_dict(_location)




        _detector_station = d.pop("detector-station", UNSET)
        detector_station: Union[Unset, TDIDetectorStation]
        if isinstance(_detector_station,  Unset):
            detector_station = UNSET
        else:
            detector_station = TDIDetectorStation.from_dict(_detector_station)




        tdi_traffic_detector = cls(
            location=location,
            detector_station=detector_station,
        )


        tdi_traffic_detector.additional_properties = d
        return tdi_traffic_detector

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
