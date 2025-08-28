from enum import Enum, auto

class State(Enum):
    HOME = auto()
    LIGHT_TRAFFIC = auto()
    MEDIUM_TRAFFIC = auto()
    HEAVY_TRAFFIC = auto()
    AT_STATION = auto()
    ON_TRAIN = auto()

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value