from enum import Enum

class IncidentsIncidentLocationDirection(str, Enum):
    BOTH_DIRECTIONS = "BOTH_DIRECTIONS"
    ONE_DIRECTION = "ONE_DIRECTION"

    def __str__(self) -> str:
        return str(self.value)
