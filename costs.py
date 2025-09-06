
from states import States
from actions import Actions

def C(s: States, a: Actions) -> States:

    if (s, a) == (States.HOME, Actions.TAKE_BIKE):
        return 45
    
    if (s, a) == (States.HOME, Actions.TAKE_CAR):
        return 1

    if (s, a) == (States.LIGHT_TRAFFIC, Actions.DRIVE_IN_LIGHT_TRAFFIC):
        return 20
    
    if (s, a) == (States.MEDIUM_TRAFFIC, Actions.DRIVE_IN_MEDIUM_TRAFFIC):
        return 30
    
    if (s, a) == (States.HEAVY_TRAFFIC, Actions.DRIVE_IN_HEAVY_TRAFFIC):
        return 70

    if (s, a) == (States.HOME, Actions.TAKE_TRAIN):
        return 2
    
    if (s, a) == (States.ON_TRAIN, Actions.SIT_ON_TRAIN):
        return 35

    if (s, a) == (States.AT_STATION, Actions.WAIT_FOR_TRAIN):
        return 3

    if (s, a) == (States.AT_STATION, Actions.GO_BACK_HOME):
        return 2
