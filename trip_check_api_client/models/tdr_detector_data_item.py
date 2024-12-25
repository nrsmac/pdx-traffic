from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.tdr_detector_list import TDRDetectorList





T = TypeVar("T", bound="TDRDetectorDataItem")


@_attrs_define
class TDRDetectorDataItem:
    """ Traffic Detector

        Attributes:
            detector_list (Union[Unset, TDRDetectorList]): Traffic Detector Inventory Location
     """

    detector_list: Union[Unset, 'TDRDetectorList'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.tdr_detector_list import TDRDetectorList
        detector_list: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.detector_list, Unset):
            detector_list = self.detector_list.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if detector_list is not UNSET:
            field_dict["detector-list"] = detector_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tdr_detector_list import TDRDetectorList
        d = src_dict.copy()
        _detector_list = d.pop("detector-list", UNSET)
        detector_list: Union[Unset, TDRDetectorList]
        if isinstance(_detector_list,  Unset):
            detector_list = UNSET
        else:
            detector_list = TDRDetectorList.from_dict(_detector_list)




        tdr_detector_data_item = cls(
            detector_list=detector_list,
        )


        tdr_detector_data_item.additional_properties = d
        return tdr_detector_data_item

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
