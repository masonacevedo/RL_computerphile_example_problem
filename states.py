from enum import Enum

class State(Enum):
    HOME = "home"
    LIGHT_TRAFFIC = "light_traffic"
    MEDIUM_TRAFFIC = "medium_traffic"
    HEAVY_TRAFFIC = "heavy_traffic"
    AT_STATION = "at_station"
    ON_TRAIN = "on_train"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value