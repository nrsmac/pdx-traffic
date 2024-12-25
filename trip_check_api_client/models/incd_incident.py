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
  from ..models.incd_ift_file import IncdIFTFile
  from ..models.incd_travel_lanes import IncdTravelLanes
  from ..models.incd_schedule import IncdSchedule
  from ..models.incd_location import IncdLocation
  from ..models.incd_off_hwy_lanes import IncdOffHwyLanes





T = TypeVar("T", bound="IncdIncident")


@_attrs_define
class IncdIncident:
    """ INCD Incident class

        Attributes:
            incident_id (Union[Unset, str]): TripCheck Incident Identifer
            event_id (Union[Unset, str]): TOCS Event identifier
            event_type_id (Union[Unset, str]): Event Type identifier
            event_subtype_id (Union[Unset, str]): Event Subtype identifier
            update_time (Union[Unset, datetime.datetime]): Date of last update
            create_time (Union[Unset, datetime.datetime]): Date of creation
            is_active (Union[Unset, str]): Is Active Flag
            impact_id (Union[Unset, str]): Impact Id
            impact_desc (Union[Unset, str]): Impact Desc
            headline (Union[Unset, str]): Headline message of the incident
            comments (Union[Unset, str]): Comments regarding the incident
            location (Union[Unset, IncdLocation]): Location
            travel_lanes (Union[Unset, IncdTravelLanes]): Travel Lanes
            off_hwy_lanes (Union[Unset, IncdOffHwyLanes]): Off Highway Lanes
            schedule (Union[Unset, IncdSchedule]): Response Schedule
            info_url (Union[Unset, str]): URL for further incident Information
            files (Union[Unset, list['IncdIFTFile']]): List of IFT Files
     """

    incident_id: Union[Unset, str] = UNSET
    event_id: Union[Unset, str] = UNSET
    event_type_id: Union[Unset, str] = UNSET
    event_subtype_id: Union[Unset, str] = UNSET
    update_time: Union[Unset, datetime.datetime] = UNSET
    create_time: Union[Unset, datetime.datetime] = UNSET
    is_active: Union[Unset, str] = UNSET
    impact_id: Union[Unset, str] = UNSET
    impact_desc: Union[Unset, str] = UNSET
    headline: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    location: Union[Unset, 'IncdLocation'] = UNSET
    travel_lanes: Union[Unset, 'IncdTravelLanes'] = UNSET
    off_hwy_lanes: Union[Unset, 'IncdOffHwyLanes'] = UNSET
    schedule: Union[Unset, 'IncdSchedule'] = UNSET
    info_url: Union[Unset, str] = UNSET
    files: Union[Unset, list['IncdIFTFile']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.incd_ift_file import IncdIFTFile
        from ..models.incd_travel_lanes import IncdTravelLanes
        from ..models.incd_schedule import IncdSchedule
        from ..models.incd_location import IncdLocation
        from ..models.incd_off_hwy_lanes import IncdOffHwyLanes
        incident_id = self.incident_id

        event_id = self.event_id

        event_type_id = self.event_type_id

        event_subtype_id = self.event_subtype_id

        update_time: Union[Unset, str] = UNSET
        if not isinstance(self.update_time, Unset):
            update_time = self.update_time.isoformat()

        create_time: Union[Unset, str] = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        is_active = self.is_active

        impact_id = self.impact_id

        impact_desc = self.impact_desc

        headline = self.headline

        comments = self.comments

        location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        travel_lanes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.travel_lanes, Unset):
            travel_lanes = self.travel_lanes.to_dict()

        off_hwy_lanes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.off_hwy_lanes, Unset):
            off_hwy_lanes = self.off_hwy_lanes.to_dict()

        schedule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        info_url = self.info_url

        files: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if incident_id is not UNSET:
            field_dict["incident-id"] = incident_id
        if event_id is not UNSET:
            field_dict["event-id"] = event_id
        if event_type_id is not UNSET:
            field_dict["event-type-id"] = event_type_id
        if event_subtype_id is not UNSET:
            field_dict["event-subtype-id"] = event_subtype_id
        if update_time is not UNSET:
            field_dict["update-time"] = update_time
        if create_time is not UNSET:
            field_dict["create-time"] = create_time
        if is_active is not UNSET:
            field_dict["is-active"] = is_active
        if impact_id is not UNSET:
            field_dict["impact-id"] = impact_id
        if impact_desc is not UNSET:
            field_dict["impact-desc"] = impact_desc
        if headline is not UNSET:
            field_dict["headline"] = headline
        if comments is not UNSET:
            field_dict["comments"] = comments
        if location is not UNSET:
            field_dict["location"] = location
        if travel_lanes is not UNSET:
            field_dict["travel-lanes"] = travel_lanes
        if off_hwy_lanes is not UNSET:
            field_dict["off-hwy-lanes"] = off_hwy_lanes
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if info_url is not UNSET:
            field_dict["info-url"] = info_url
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.incd_ift_file import IncdIFTFile
        from ..models.incd_travel_lanes import IncdTravelLanes
        from ..models.incd_schedule import IncdSchedule
        from ..models.incd_location import IncdLocation
        from ..models.incd_off_hwy_lanes import IncdOffHwyLanes
        d = src_dict.copy()
        incident_id = d.pop("incident-id", UNSET)

        event_id = d.pop("event-id", UNSET)

        event_type_id = d.pop("event-type-id", UNSET)

        event_subtype_id = d.pop("event-subtype-id", UNSET)

        _update_time = d.pop("update-time", UNSET)
        update_time: Union[Unset, datetime.datetime]
        if isinstance(_update_time,  Unset):
            update_time = UNSET
        else:
            update_time = isoparse(_update_time)




        _create_time = d.pop("create-time", UNSET)
        create_time: Union[Unset, datetime.datetime]
        if isinstance(_create_time,  Unset):
            create_time = UNSET
        else:
            create_time = isoparse(_create_time)




        is_active = d.pop("is-active", UNSET)

        impact_id = d.pop("impact-id", UNSET)

        impact_desc = d.pop("impact-desc", UNSET)

        headline = d.pop("headline", UNSET)

        comments = d.pop("comments", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, IncdLocation]
        if isinstance(_location,  Unset):
            location = UNSET
        else:
            location = IncdLocation.from_dict(_location)




        _travel_lanes = d.pop("travel-lanes", UNSET)
        travel_lanes: Union[Unset, IncdTravelLanes]
        if isinstance(_travel_lanes,  Unset):
            travel_lanes = UNSET
        else:
            travel_lanes = IncdTravelLanes.from_dict(_travel_lanes)




        _off_hwy_lanes = d.pop("off-hwy-lanes", UNSET)
        off_hwy_lanes: Union[Unset, IncdOffHwyLanes]
        if isinstance(_off_hwy_lanes,  Unset):
            off_hwy_lanes = UNSET
        else:
            off_hwy_lanes = IncdOffHwyLanes.from_dict(_off_hwy_lanes)




        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, IncdSchedule]
        if isinstance(_schedule,  Unset):
            schedule = UNSET
        else:
            schedule = IncdSchedule.from_dict(_schedule)




        info_url = d.pop("info-url", UNSET)

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in (_files or []):
            files_item = IncdIFTFile.from_dict(files_item_data)



            files.append(files_item)


        incd_incident = cls(
            incident_id=incident_id,
            event_id=event_id,
            event_type_id=event_type_id,
            event_subtype_id=event_subtype_id,
            update_time=update_time,
            create_time=create_time,
            is_active=is_active,
            impact_id=impact_id,
            impact_desc=impact_desc,
            headline=headline,
            comments=comments,
            location=location,
            travel_lanes=travel_lanes,
            off_hwy_lanes=off_hwy_lanes,
            schedule=schedule,
            info_url=info_url,
            files=files,
        )


        incd_incident.additional_properties = d
        return incd_incident

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
