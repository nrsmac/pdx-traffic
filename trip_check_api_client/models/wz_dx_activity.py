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
  from ..models.wz_dx_lane import WZDxLane
  from ..models.wz_dx_end_location import WZDxEndLocation
  from ..models.wz_dx_begin_location import WZDxBeginLocation
  from ..models.wz_dx_start_dates import WZDxStartDates
  from ..models.wz_dx_end_dates import WZDxEndDates





T = TypeVar("T", bound="WZDxActivity")


@_attrs_define
class WZDxActivity:
    """ Work Zone Activity

        Attributes:
            identifier (Union[Unset, str]): A unique identifier of the work zone activity
            sub_identifier (Union[Unset, int]): The subidentifier is the identifier of the entirety of the work zone project
            start_date_time (Union[Unset, WZDxStartDates]): WZDx Events Start Dates
            end_date_time (Union[Unset, WZDxEndDates]): WZDx Events End Dates
            begin_location (Union[Unset, WZDxBeginLocation]): Work Zone Event Begin Location
            end_location (Union[Unset, WZDxEndLocation]): Work Zone Event End Location
            wz_status (Union[Unset, str]): Work zone status
            total_lanes (Union[Unset, int]): Total lanes along roadway segment
            lanes (Union[Unset, list['WZDxLane']]): List of Lanes
            workers_present (Union[Unset, str]): Workers Present
            reduced_spd_posted (Union[Unset, str]): Reduced Speed Posted
            road_restrictions (Union[Unset, str]): Road Restrictions
            description (Union[Unset, str]): Short description of the work zone
            issuing_organization (Union[Unset, str]): Issuing organization
            time_stamp_event_creation (Union[Unset, datetime.datetime]): Datetime of event creation
            time_stamp_event_update (Union[Unset, datetime.datetime]): Datetime of event update
     """

    identifier: Union[Unset, str] = UNSET
    sub_identifier: Union[Unset, int] = UNSET
    start_date_time: Union[Unset, 'WZDxStartDates'] = UNSET
    end_date_time: Union[Unset, 'WZDxEndDates'] = UNSET
    begin_location: Union[Unset, 'WZDxBeginLocation'] = UNSET
    end_location: Union[Unset, 'WZDxEndLocation'] = UNSET
    wz_status: Union[Unset, str] = UNSET
    total_lanes: Union[Unset, int] = UNSET
    lanes: Union[Unset, list['WZDxLane']] = UNSET
    workers_present: Union[Unset, str] = UNSET
    reduced_spd_posted: Union[Unset, str] = UNSET
    road_restrictions: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    issuing_organization: Union[Unset, str] = UNSET
    time_stamp_event_creation: Union[Unset, datetime.datetime] = UNSET
    time_stamp_event_update: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.wz_dx_lane import WZDxLane
        from ..models.wz_dx_end_location import WZDxEndLocation
        from ..models.wz_dx_begin_location import WZDxBeginLocation
        from ..models.wz_dx_start_dates import WZDxStartDates
        from ..models.wz_dx_end_dates import WZDxEndDates
        identifier = self.identifier

        sub_identifier = self.sub_identifier

        start_date_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.start_date_time, Unset):
            start_date_time = self.start_date_time.to_dict()

        end_date_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.end_date_time, Unset):
            end_date_time = self.end_date_time.to_dict()

        begin_location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.begin_location, Unset):
            begin_location = self.begin_location.to_dict()

        end_location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.end_location, Unset):
            end_location = self.end_location.to_dict()

        wz_status = self.wz_status

        total_lanes = self.total_lanes

        lanes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.lanes, Unset):
            lanes = []
            for lanes_item_data in self.lanes:
                lanes_item = lanes_item_data.to_dict()
                lanes.append(lanes_item)



        workers_present = self.workers_present

        reduced_spd_posted = self.reduced_spd_posted

        road_restrictions = self.road_restrictions

        description = self.description

        issuing_organization = self.issuing_organization

        time_stamp_event_creation: Union[Unset, str] = UNSET
        if not isinstance(self.time_stamp_event_creation, Unset):
            time_stamp_event_creation = self.time_stamp_event_creation.isoformat()

        time_stamp_event_update: Union[Unset, str] = UNSET
        if not isinstance(self.time_stamp_event_update, Unset):
            time_stamp_event_update = self.time_stamp_event_update.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if identifier is not UNSET:
            field_dict["Identifier"] = identifier
        if sub_identifier is not UNSET:
            field_dict["SubIdentifier"] = sub_identifier
        if start_date_time is not UNSET:
            field_dict["StartDateTime"] = start_date_time
        if end_date_time is not UNSET:
            field_dict["EndDateTime"] = end_date_time
        if begin_location is not UNSET:
            field_dict["BeginLocation"] = begin_location
        if end_location is not UNSET:
            field_dict["EndLocation"] = end_location
        if wz_status is not UNSET:
            field_dict["WZStatus"] = wz_status
        if total_lanes is not UNSET:
            field_dict["TotalLanes"] = total_lanes
        if lanes is not UNSET:
            field_dict["Lanes"] = lanes
        if workers_present is not UNSET:
            field_dict["WorkersPresent"] = workers_present
        if reduced_spd_posted is not UNSET:
            field_dict["ReducedSpdPosted"] = reduced_spd_posted
        if road_restrictions is not UNSET:
            field_dict["RoadRestrictions"] = road_restrictions
        if description is not UNSET:
            field_dict["Description"] = description
        if issuing_organization is not UNSET:
            field_dict["IssuingOrganization"] = issuing_organization
        if time_stamp_event_creation is not UNSET:
            field_dict["TimeStampEventCreation"] = time_stamp_event_creation
        if time_stamp_event_update is not UNSET:
            field_dict["TimeStampEventUpdate"] = time_stamp_event_update

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.wz_dx_lane import WZDxLane
        from ..models.wz_dx_end_location import WZDxEndLocation
        from ..models.wz_dx_begin_location import WZDxBeginLocation
        from ..models.wz_dx_start_dates import WZDxStartDates
        from ..models.wz_dx_end_dates import WZDxEndDates
        d = src_dict.copy()
        identifier = d.pop("Identifier", UNSET)

        sub_identifier = d.pop("SubIdentifier", UNSET)

        _start_date_time = d.pop("StartDateTime", UNSET)
        start_date_time: Union[Unset, WZDxStartDates]
        if isinstance(_start_date_time,  Unset):
            start_date_time = UNSET
        else:
            start_date_time = WZDxStartDates.from_dict(_start_date_time)




        _end_date_time = d.pop("EndDateTime", UNSET)
        end_date_time: Union[Unset, WZDxEndDates]
        if isinstance(_end_date_time,  Unset):
            end_date_time = UNSET
        else:
            end_date_time = WZDxEndDates.from_dict(_end_date_time)




        _begin_location = d.pop("BeginLocation", UNSET)
        begin_location: Union[Unset, WZDxBeginLocation]
        if isinstance(_begin_location,  Unset):
            begin_location = UNSET
        else:
            begin_location = WZDxBeginLocation.from_dict(_begin_location)




        _end_location = d.pop("EndLocation", UNSET)
        end_location: Union[Unset, WZDxEndLocation]
        if isinstance(_end_location,  Unset):
            end_location = UNSET
        else:
            end_location = WZDxEndLocation.from_dict(_end_location)




        wz_status = d.pop("WZStatus", UNSET)

        total_lanes = d.pop("TotalLanes", UNSET)

        lanes = []
        _lanes = d.pop("Lanes", UNSET)
        for lanes_item_data in (_lanes or []):
            lanes_item = WZDxLane.from_dict(lanes_item_data)



            lanes.append(lanes_item)


        workers_present = d.pop("WorkersPresent", UNSET)

        reduced_spd_posted = d.pop("ReducedSpdPosted", UNSET)

        road_restrictions = d.pop("RoadRestrictions", UNSET)

        description = d.pop("Description", UNSET)

        issuing_organization = d.pop("IssuingOrganization", UNSET)

        _time_stamp_event_creation = d.pop("TimeStampEventCreation", UNSET)
        time_stamp_event_creation: Union[Unset, datetime.datetime]
        if isinstance(_time_stamp_event_creation,  Unset):
            time_stamp_event_creation = UNSET
        else:
            time_stamp_event_creation = isoparse(_time_stamp_event_creation)




        _time_stamp_event_update = d.pop("TimeStampEventUpdate", UNSET)
        time_stamp_event_update: Union[Unset, datetime.datetime]
        if isinstance(_time_stamp_event_update,  Unset):
            time_stamp_event_update = UNSET
        else:
            time_stamp_event_update = isoparse(_time_stamp_event_update)




        wz_dx_activity = cls(
            identifier=identifier,
            sub_identifier=sub_identifier,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            begin_location=begin_location,
            end_location=end_location,
            wz_status=wz_status,
            total_lanes=total_lanes,
            lanes=lanes,
            workers_present=workers_present,
            reduced_spd_posted=reduced_spd_posted,
            road_restrictions=road_restrictions,
            description=description,
            issuing_organization=issuing_organization,
            time_stamp_event_creation=time_stamp_event_creation,
            time_stamp_event_update=time_stamp_event_update,
        )


        wz_dx_activity.additional_properties = d
        return wz_dx_activity

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
