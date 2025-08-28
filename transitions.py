
from states import State
from actions import Action

def T(s: State, a: Action) -> State:

    if (s, a) == (State.HOME, Action.TAKE_BIKE):
        return {1.0: State.AT_WORK}
    
    if (s, a) == (State.HOME, Action.TAKE_CAR):
        return {0.2: State.LIGHT_TRAFFIC, 
                0.7: State.MEDIUM_TRAFFIC, 
                0.1: State.HEAVY_TRAFFIC}

    if (s, a) == (State.LIGHT_TRAFFIC, Action.SIT_IN_LIGHT_TRAFFIC):
        return {1.0: State.AT_WORK}
    
    if (s, a) == (State.MEDIUM_TRAFFIC, Action.SIT_IN_MEDIUM_TRAFFIC):
        return {1.0: State.AT_WORK}
    
    if (s, a) == (State.HEAVY_TRAFFIC, Action.SIT_IN_HEAVY_TRAFFIC):
        return {1.0: State.AT_WORK}

    if (s, a) == (State.HOME, Action.TAKE_TRAIN):
        return {0.9: State.ON_TRAIN, 0.1: State.AT_STATION}
    
    if (s, a) == (State.ON_TRAIN, Action.SIT_ON_TRAIN):
        return {1.0: State.AT_WORK}

    if (s, a) == (State.AT_STATION, Action.WAIT_FOR_TRAIN):
        return {0.9: State.ON_TRAIN, 0.1: State.AT_STATION}

    if (s, a) == {State.AT_STATION, Action.GO_BACK_HOME}:
        return {1.0: State.HOME}
