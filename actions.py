from enum import Enum, auto

class Action(Enum):
    TAKE_BIKE = auto()
    TAKE_CAR = auto()
    SIT_IN_LIGHT_TRAFFIC = auto()
    SIT_IN_MEDIUM_TRAFFIC = auto()
    SIT_IN_HEAVY_TRAFFIC = auto()
    GO_TO_STATION = auto()
    WAIT_FOR_TRAIN = auto()
    GO_BACK_HOME = auto()
    SIT_ON_TRAIN = auto()

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value