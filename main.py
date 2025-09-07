import random
import copy

from states import States
from actions import Actions
from transitions import T
from costs import C

VALID_ACTIONS = set(
    [
        (States.HOME, Actions.TAKE_BIKE),
        (States.HOME, Actions.TAKE_CAR),
        (States.HOME, Actions.TAKE_TRAIN),
        (States.LIGHT_TRAFFIC, Actions.DRIVE_IN_LIGHT_TRAFFIC),
        (States.MEDIUM_TRAFFIC, Actions.DRIVE_IN_MEDIUM_TRAFFIC),
        (States.HEAVY_TRAFFIC, Actions.DRIVE_IN_HEAVY_TRAFFIC),
        (States.ON_TRAIN, Actions.SIT_ON_TRAIN),
        (States.AT_STATION, Actions.WAIT_FOR_TRAIN),
        (States.AT_STATION, Actions.GO_BACK_HOME)
    ]
)

GAMMA = 0.5

def Q(s, a, values):
    if (s, a) not in VALID_ACTIONS:
        raise Exception(f"Invalid action from state: {a}, {s}")
    
    immediate_cost = C(s,a)
    future_cost = 0
    transition_probabilities, potential_successor_states = zip(*T(s,a).items())

    for transition_probability, successor_state in zip(transition_probabilities, potential_successor_states):
        future_cost += (transition_probability * values[successor_state])
    return immediate_cost + future_cost

def update_values(values):
    for s in States:
        if s == States.AT_WORK:
            continue
        valid_actions_from_state = [a for a in Actions if (s, a) in VALID_ACTIONS]
        values[s] = min(Q(s, a, values) for a in valid_actions_from_state)  


if __name__ == "__main__":
    values = {s: 100 for s in States}
    values[States.AT_WORK] = 0

    print("Initial Values: ", values)

    i = 1
    old_values = copy.deepcopy(values)
    update_values(values)
    new_values = copy.deepcopy(values)
    while any(abs(old_values[s] - new_values[s]) > 0.000001 for s in States):
        old_values = copy.deepcopy(values)
        update_values(values)
        new_values = copy.deepcopy(values)
        i += 1

    print(f"\nThreshold reached after {i} iterations. Stopping.\n")
    print("Final Values: ", values)