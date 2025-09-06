from enum import Enum, auto

class Actions(Enum):
    TAKE_BIKE = auto()
    TAKE_CAR = auto()
    TAKE_TRAIN = auto()
    DRIVE_IN_LIGHT_TRAFFIC = auto()
    DRIVE_IN_MEDIUM_TRAFFIC = auto()
    DRIVE_IN_HEAVY_TRAFFIC = auto()
    WAIT_FOR_TRAIN = auto()
    GO_BACK_HOME = auto()
    SIT_ON_TRAIN = auto()
