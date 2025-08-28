from enum import Enum

class Action(Enum):
    TAKE_BIKE = "take_bike"
    TAKE_CAR = "take_car"
    SIT_IN_LIGHT_TRAFFIC = "sit_in_light_traffic"
    SIT_IN_MEDIUM_TRAFFIC = "sit_in_medium_traffic"
    SIT_IN_HEAVY_TRAFFIC = "sit_in_heavy_traffic"
    GO_TO_STATION = "go_to_station"
    WAIT_FOR_TRAIN = "wait_at_station"
    GO_BACK_HOME = "go_back_home"
    SIT_ON_TRAIN = "sit_on_train"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value