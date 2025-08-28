import random


def take_bike():
    return 45

WAIT_PROB, RIDE_PROB = 0.1, 0.9
def take_train():
    if random.random() < WAIT_PROB:
        return 10 + take_train()
    else:
        return 35

LIGHT_TRAFFIC_PROB, MEDIUM_TRAFFIC_PROB, HEAVY_TRAFFIC_PROB = 0.2, 0.7, 0.1
def take_car():
    if random.random() < LIGHT_TRAFFIC_PROB:
        return 21
    elif random.random() < MEDIUM_TRAFFIC_PROB:
        return 31
    else:
        return 70
