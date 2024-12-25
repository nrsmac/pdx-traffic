from enum import Enum

class IncidentsIncidentType(str, Enum):
    ACCIDENT = "ACCIDENT"
    CONSTRUCTION = "CONSTRUCTION"
    HAZARD = "HAZARD"
    ROAD_CLOSED = "ROAD_CLOSED"

    def __str__(self) -> str:
        return str(self.value)
