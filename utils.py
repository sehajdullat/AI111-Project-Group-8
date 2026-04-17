import numpy as np
import random
from config import LANES, LAMBDA, PREDICTION_HORIZON, EMERGENCY_PROBABILITY

def generate_arrivals():
    return {lane: np.random.poisson(LAMBDA[lane]) for lane in LANES}

def generate_emergency():
    emergency = {}
    for lane in LANES:
        if random.random() < EMERGENCY_PROBABILITY:
            emergency[lane] = random.randint(1, 2)
        else:
            emergency[lane] = 0
    return emergency

def expected_future_arrivals(lane):
    return LAMBDA[lane] * PREDICTION_HORIZON

def compute_score(queue, lane):
    return queue[lane] + expected_future_arrivals(lane)

def get_priority_order(queue, scores, emergency):
    emergency_lanes = [lane for lane in LANES if emergency[lane] > 0]
    normal_lanes = [lane for lane in LANES if emergency[lane] == 0]

    emergency_sorted = sorted(emergency_lanes, key=lambda l: emergency[l], reverse=True)
    normal_sorted = sorted(normal_lanes, key=lambda l: scores[l], reverse=True)

    return emergency_sorted + normal_sorted
