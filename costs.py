
from states import State
from actions import Action

def C(s: State, a: Action) -> State:

    if (s, a) == (State.HOME, Action.TAKE_BIKE):
        return 45
    
    if (s, a) == (State.HOME, Action.TAKE_CAR):
        return 1

    if (s, a) == (State.LIGHT_TRAFFIC, Action.SIT_IN_LIGHT_TRAFFIC):
        return 20
    
    if (s, a) == (State.MEDIUM_TRAFFIC, Action.SIT_IN_MEDIUM_TRAFFIC):
        return 30
    
    if (s, a) == (State.HEAVY_TRAFFIC, Action.SIT_IN_HEAVY_TRAFFIC):
        return 70

    if (s, a) == (State.HOME, Action.TAKE_TRAIN):
        return 2
    
    if (s, a) == (State.ON_TRAIN, Action.SIT_ON_TRAIN):
        return 35

    if (s, a) == (State.AT_STATION, Action.WAIT_FOR_TRAIN):
        return 3

    if (s, a) == {State.AT_STATION, Action.GO_BACK_HOME}:
        return 2
