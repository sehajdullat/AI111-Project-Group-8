from config import TIME_STEPS
from utils import generate_arrivals, generate_emergency
from simulation import select_lane, update_queue
from display import display

def main():
    for step in range(1, TIME_STEPS + 1):

        arrivals = generate_arrivals()
        emergency = generate_emergency()

        active_lane, scores, priority_order, is_emergency = select_lane(emergency)

        update_queue(arrivals, active_lane)

        display(step, arrivals, active_lane, scores, emergency, is_emergency, priority_order)

if __name__ == "__main__":
    main()
