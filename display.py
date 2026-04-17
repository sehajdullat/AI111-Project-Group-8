from config import LANES
from simulation import queue, expected_wait

def display(step, arrivals, active_lane, scores, emergency, is_emergency, priority_order):

    print("\n" + "="*55)
    print(f"🚦 TRAFFIC SIGNAL SYSTEM | TIME STEP {step}")
    print("="*55)

    print("\n📋 Lane Details:")
    print("-"*55)
    print(f"{'Lane':<8}{'Queue':<8}{'Arr':<6}{'Emerg':<8}{'Score':<8}{'Wait':<8}")
    print("-"*55)

    for lane in LANES:
        print(f"{lane:<8}{queue[lane]:<8}{arrivals[lane]:<6}{emergency[lane]:<8}{scores[lane]:<8.1f}{expected_wait(lane):<8.2f}")

    print("-"*55)

    print("\n🚑 Emergency Vehicles:")
    for lane in LANES:
        print(f"  {lane:<6} : {emergency[lane]}")

    print("\n📊 Priority Order:")
    for i, lane in enumerate(priority_order, 1):
        if emergency[lane] > 0:
            print(f"  {i}. {lane:<6} → 🚑 {emergency[lane]} emergency")
        else:
            print(f"  {i}. {lane:<6} → Score = {scores[lane]:.1f}")

    if is_emergency:
        print(f"\n🚑 GREEN SIGNAL → {active_lane} (Emergency Priority)")
    else:
        print(f"\n🟢 GREEN SIGNAL → {active_lane}")

    print("="*55)
