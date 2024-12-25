from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.tdr_detector_data_detail import TDRDetectorDataDetail





T = TypeVar("T", bound="TDRDetectorList")


@_attrs_define
class TDRDetectorList:
    """ Traffic Detector Inventory Location

        Attributes:
            detector_data_detail (Union[Unset, TDRDetectorDataDetail]): Detector Station
     """

    detector_data_detail: Union[Unset, 'TDRDetectorDataDetail'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.tdr_detector_data_detail import TDRDetectorDataDetail
        detector_data_detail: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.detector_data_detail, Unset):
            detector_data_detail = self.detector_data_detail.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if detector_data_detail is not UNSET:
            field_dict["detector-data-detail"] = detector_data_detail

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tdr_detector_data_detail import TDRDetectorDataDetail
        d = src_dict.copy()
        _detector_data_detail = d.pop("detector-data-detail", UNSET)
        detector_data_detail: Union[Unset, TDRDetectorDataDetail]
        if isinstance(_detector_data_detail,  Unset):
            detector_data_detail = UNSET
        else:
            detector_data_detail = TDRDetectorDataDetail.from_dict(_detector_data_detail)




        tdr_detector_list = cls(
            detector_data_detail=detector_data_detail,
        )


        tdr_detector_list.additional_properties = d
        return tdr_detector_list

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
