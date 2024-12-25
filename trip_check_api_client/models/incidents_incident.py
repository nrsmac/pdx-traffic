from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.incidents_incident_subtype import IncidentsIncidentSubtype
from ..models.incidents_incident_type import IncidentsIncidentType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.incidents_incident_location import IncidentsIncidentLocation
  from ..models.incidents_incident_schedule import IncidentsIncidentSchedule
  from ..models.incidents_incident_parent_event import IncidentsIncidentParentEvent
  from ..models.incidents_incident_source import IncidentsIncidentSource





T = TypeVar("T", bound="IncidentsIncident")


@_attrs_define
class IncidentsIncident:
    """ Encapsulates all of the information pertaining to a single incident.

        Attributes:
            parent_event (Union[Unset, IncidentsIncidentParentEvent]): For events with multiple closures such as marathons
                or festivals, you can associate the incident to an event object.
            id (Union[Unset, str]): Specifies an alphanumeric or numeric identifier.
                The ID must be globally unique to your feed and remain stable over an incident’s lifetime.
            creationtime (Union[Unset, datetime.datetime]): Datetime when the incident was created.
            updatetime (Union[Unset, datetime.datetime]): Datetime when the incident was last updated.
            source (Union[Unset, IncidentsIncidentSource]): Encapsulates the elements that specify the source of information
                for a single incident.
            type_ (Union[Unset, IncidentsIncidentType]): Specifies the type of incident.
            subtype (Union[Unset, IncidentsIncidentSubtype]): Further refinement of the information in the "type" element.
            description (Union[Unset, str]): Describes the incident, including the possible cause and consequences of the
                disruption.
            location (Union[Unset, IncidentsIncidentLocation]): Encapsulates the location information for the incident.
            starttime (Union[Unset, datetime.datetime]): Specifies the start datetime for the period of disruption.
            endtime (Union[Unset, datetime.datetime]): Specifies the end datetime for the period of disruption.
            schedule (Union[Unset, IncidentsIncidentSchedule]): The schedule encapsulates all start and end times for an
                recurring incident.
     """

    parent_event: Union[Unset, 'IncidentsIncidentParentEvent'] = UNSET
    id: Union[Unset, str] = UNSET
    creationtime: Union[Unset, datetime.datetime] = UNSET
    updatetime: Union[Unset, datetime.datetime] = UNSET
    source: Union[Unset, 'IncidentsIncidentSource'] = UNSET
    type_: Union[Unset, IncidentsIncidentType] = UNSET
    subtype: Union[Unset, IncidentsIncidentSubtype] = UNSET
    description: Union[Unset, str] = UNSET
    location: Union[Unset, 'IncidentsIncidentLocation'] = UNSET
    starttime: Union[Unset, datetime.datetime] = UNSET
    endtime: Union[Unset, datetime.datetime] = UNSET
    schedule: Union[Unset, 'IncidentsIncidentSchedule'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.incidents_incident_location import IncidentsIncidentLocation
        from ..models.incidents_incident_schedule import IncidentsIncidentSchedule
        from ..models.incidents_incident_parent_event import IncidentsIncidentParentEvent
        from ..models.incidents_incident_source import IncidentsIncidentSource
        parent_event: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_event, Unset):
            parent_event = self.parent_event.to_dict()

        id = self.id

        creationtime: Union[Unset, str] = UNSET
        if not isinstance(self.creationtime, Unset):
            creationtime = self.creationtime.isoformat()

        updatetime: Union[Unset, str] = UNSET
        if not isinstance(self.updatetime, Unset):
            updatetime = self.updatetime.isoformat()

        source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        subtype: Union[Unset, str] = UNSET
        if not isinstance(self.subtype, Unset):
            subtype = self.subtype.value


        description = self.description

        location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        starttime: Union[Unset, str] = UNSET
        if not isinstance(self.starttime, Unset):
            starttime = self.starttime.isoformat()

        endtime: Union[Unset, str] = UNSET
        if not isinstance(self.endtime, Unset):
            endtime = self.endtime.isoformat()

        schedule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if parent_event is not UNSET:
            field_dict["parent_event"] = parent_event
        if id is not UNSET:
            field_dict["id"] = id
        if creationtime is not UNSET:
            field_dict["creationtime"] = creationtime
        if updatetime is not UNSET:
            field_dict["updatetime"] = updatetime
        if source is not UNSET:
            field_dict["source"] = source
        if type_ is not UNSET:
            field_dict["type"] = type_
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if description is not UNSET:
            field_dict["description"] = description
        if location is not UNSET:
            field_dict["location"] = location
        if starttime is not UNSET:
            field_dict["starttime"] = starttime
        if endtime is not UNSET:
            field_dict["endtime"] = endtime
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.incidents_incident_location import IncidentsIncidentLocation
        from ..models.incidents_incident_schedule import IncidentsIncidentSchedule
        from ..models.incidents_incident_parent_event import IncidentsIncidentParentEvent
        from ..models.incidents_incident_source import IncidentsIncidentSource
        d = src_dict.copy()
        _parent_event = d.pop("parent_event", UNSET)
        parent_event: Union[Unset, IncidentsIncidentParentEvent]
        if isinstance(_parent_event,  Unset):
            parent_event = UNSET
        else:
            parent_event = IncidentsIncidentParentEvent.from_dict(_parent_event)




        id = d.pop("id", UNSET)

        _creationtime = d.pop("creationtime", UNSET)
        creationtime: Union[Unset, datetime.datetime]
        if isinstance(_creationtime,  Unset):
            creationtime = UNSET
        else:
            creationtime = isoparse(_creationtime)




        _updatetime = d.pop("updatetime", UNSET)
        updatetime: Union[Unset, datetime.datetime]
        if isinstance(_updatetime,  Unset):
            updatetime = UNSET
        else:
            updatetime = isoparse(_updatetime)




        _source = d.pop("source", UNSET)
        source: Union[Unset, IncidentsIncidentSource]
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = IncidentsIncidentSource.from_dict(_source)




        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, IncidentsIncidentType]
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = IncidentsIncidentType(_type_)




        _subtype = d.pop("subtype", UNSET)
        subtype: Union[Unset, IncidentsIncidentSubtype]
        if isinstance(_subtype,  Unset):
            subtype = UNSET
        else:
            subtype = IncidentsIncidentSubtype(_subtype)




        description = d.pop("description", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, IncidentsIncidentLocation]
        if isinstance(_location,  Unset):
            location = UNSET
        else:
            location = IncidentsIncidentLocation.from_dict(_location)




        _starttime = d.pop("starttime", UNSET)
        starttime: Union[Unset, datetime.datetime]
        if isinstance(_starttime,  Unset):
            starttime = UNSET
        else:
            starttime = isoparse(_starttime)




        _endtime = d.pop("endtime", UNSET)
        endtime: Union[Unset, datetime.datetime]
        if isinstance(_endtime,  Unset):
            endtime = UNSET
        else:
            endtime = isoparse(_endtime)




        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, IncidentsIncidentSchedule]
        if isinstance(_schedule,  Unset):
            schedule = UNSET
        else:
            schedule = IncidentsIncidentSchedule.from_dict(_schedule)




        incidents_incident = cls(
            parent_event=parent_event,
            id=id,
            creationtime=creationtime,
            updatetime=updatetime,
            source=source,
            type_=type_,
            subtype=subtype,
            description=description,
            location=location,
            starttime=starttime,
            endtime=endtime,
            schedule=schedule,
        )


        incidents_incident.additional_properties = d
        return incidents_incident

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
