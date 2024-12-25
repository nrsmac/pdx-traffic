from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.parking_lots import ParkingLots
  from ..models.organization_info import OrganizationInfo





T = TypeVar("T", bound="MFParking")


@_attrs_define
class MFParking:
    """ Multnomah Falls Parking Data output class

        Attributes:
            organization_information (Union[Unset, OrganizationInfo]): Organization Information
            parking_lots (Union[Unset, ParkingLots]): Parking Lot Information and Data class
     """

    organization_information: Union[Unset, 'OrganizationInfo'] = UNSET
    parking_lots: Union[Unset, 'ParkingLots'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.parking_lots import ParkingLots
        from ..models.organization_info import OrganizationInfo
        organization_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_information, Unset):
            organization_information = self.organization_information.to_dict()

        parking_lots: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parking_lots, Unset):
            parking_lots = self.parking_lots.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_information is not UNSET:
            field_dict["organization-information"] = organization_information
        if parking_lots is not UNSET:
            field_dict["parkingLots"] = parking_lots

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.parking_lots import ParkingLots
        from ..models.organization_info import OrganizationInfo
        d = src_dict.copy()
        _organization_information = d.pop("organization-information", UNSET)
        organization_information: Union[Unset, OrganizationInfo]
        if isinstance(_organization_information,  Unset):
            organization_information = UNSET
        else:
            organization_information = OrganizationInfo.from_dict(_organization_information)




        _parking_lots = d.pop("parkingLots", UNSET)
        parking_lots: Union[Unset, ParkingLots]
        if isinstance(_parking_lots,  Unset):
            parking_lots = UNSET
        else:
            parking_lots = ParkingLots.from_dict(_parking_lots)




        mf_parking = cls(
            organization_information=organization_information,
            parking_lots=parking_lots,
        )


        mf_parking.additional_properties = d
        return mf_parking

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
