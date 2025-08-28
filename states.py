from enum import Enum, auto

class States(Enum):
    HOME = auto()
    LIGHT_TRAFFIC = auto()
    MEDIUM_TRAFFIC = auto()
    HEAVY_TRAFFIC = auto()
    AT_STATION = auto()
    ON_TRAIN = auto()
    AT_WORK = auto()
