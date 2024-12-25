from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime






T = TypeVar("T", bound="WZDxHeader")


@_attrs_define
class WZDxHeader:
    """ This class contains all the WorkZone Activity fields

        Attributes:
            time_stamp_update (Union[Unset, datetime.datetime]): Timestamp Update
            metadata_url (Union[Unset, str]): Metadata URL
            version_no (Union[Unset, str]): Version Number
     """

    time_stamp_update: Union[Unset, datetime.datetime] = UNSET
    metadata_url: Union[Unset, str] = UNSET
    version_no: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        time_stamp_update: Union[Unset, str] = UNSET
        if not isinstance(self.time_stamp_update, Unset):
            time_stamp_update = self.time_stamp_update.isoformat()

        metadata_url = self.metadata_url

        version_no = self.version_no


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if time_stamp_update is not UNSET:
            field_dict["TimeStampUpdate"] = time_stamp_update
        if metadata_url is not UNSET:
            field_dict["MetadataURL"] = metadata_url
        if version_no is not UNSET:
            field_dict["VersionNo"] = version_no

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _time_stamp_update = d.pop("TimeStampUpdate", UNSET)
        time_stamp_update: Union[Unset, datetime.datetime]
        if isinstance(_time_stamp_update,  Unset):
            time_stamp_update = UNSET
        else:
            time_stamp_update = isoparse(_time_stamp_update)




        metadata_url = d.pop("MetadataURL", UNSET)

        version_no = d.pop("VersionNo", UNSET)

        wz_dx_header = cls(
            time_stamp_update=time_stamp_update,
            metadata_url=metadata_url,
            version_no=version_no,
        )


        wz_dx_header.additional_properties = d
        return wz_dx_header

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
