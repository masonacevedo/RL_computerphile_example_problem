
from states import States
from actions import Actions

def T(s: States, a: Actions) -> States:

    if (s, a) == (States.HOME, Actions.TAKE_BIKE):
        return {1.0: States.AT_WORK}
    
    if (s, a) == (States.HOME, Actions.TAKE_CAR):
        return {0.2: States.LIGHT_TRAFFIC, 
                0.7: States.MEDIUM_TRAFFIC, 
                0.1: States.HEAVY_TRAFFIC}

    if (s, a) == (States.LIGHT_TRAFFIC, Actions.DRIVE_IN_LIGHT_TRAFFIC):
        return {1.0: States.AT_WORK}
    
    if (s, a) == (States.MEDIUM_TRAFFIC, Actions.DRIVE_IN_MEDIUM_TRAFFIC):
        return {1.0: States.AT_WORK}
    
    if (s, a) == (States.HEAVY_TRAFFIC, Actions.DRIVE_IN_HEAVY_TRAFFIC):
        return {1.0: States.AT_WORK}

    if (s, a) == (States.HOME, Actions.TAKE_TRAIN):
        return {0.9: States.ON_TRAIN, 0.1: States.AT_STATION}
    
    if (s, a) == (States.ON_TRAIN, Actions.SIT_ON_TRAIN):
        return {1.0: States.AT_WORK}

    if (s, a) == (States.AT_STATION, Actions.WAIT_FOR_TRAIN):
        return {0.9: States.ON_TRAIN, 0.1: States.AT_STATION}

    if (s, a) == (States.AT_STATION, Actions.GO_BACK_HOME):
        return {1.0: States.HOME}
