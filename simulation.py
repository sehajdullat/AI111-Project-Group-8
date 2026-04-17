from config import LANES, SERVICE_RATE
from utils import compute_score, get_priority_order

queue = {lane: 0 for lane in LANES}

def expected_wait(lane):
    return queue[lane] / SERVICE_RATE

def select_lane(emergency):
    scores = {lane: compute_score(queue, lane) for lane in LANES}
    priority_order = get_priority_order(queue, scores, emergency)

    selected = priority_order[0]
    is_emergency = emergency[selected] > 0

    return selected, scores, priority_order, is_emergency

def update_queue(arrivals, active_lane):
    for lane in LANES:
        queue[lane] += arrivals[lane]

    queue[active_lane] = max(0, queue[active_lane] - SERVICE_RATE)
