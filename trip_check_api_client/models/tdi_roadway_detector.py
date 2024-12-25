from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TDIRoadwayDetector")


@_attrs_define
class TDIRoadwayDetector:
    """ Roadway Detector

        Attributes:
            detector_id (Union[Unset, int]): Detector Id
            detector_title (Union[Unset, str]): Detector Title
            lane (Union[Unset, int]): Lane
     """

    detector_id: Union[Unset, int] = UNSET
    detector_title: Union[Unset, str] = UNSET
    lane: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        detector_id = self.detector_id

        detector_title = self.detector_title

        lane = self.lane


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if detector_id is not UNSET:
            field_dict["detector-id"] = detector_id
        if detector_title is not UNSET:
            field_dict["detector-title"] = detector_title
        if lane is not UNSET:
            field_dict["lane"] = lane

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        detector_id = d.pop("detector-id", UNSET)

        detector_title = d.pop("detector-title", UNSET)

        lane = d.pop("lane", UNSET)

        tdi_roadway_detector = cls(
            detector_id=detector_id,
            detector_title=detector_title,
            lane=lane,
        )


        tdi_roadway_detector.additional_properties = d
        return tdi_roadway_detector

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
