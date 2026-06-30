#Q9 Auto Return-to-Home System

drone_state = {
    "battery": 18,
    "altitude": 95,
    "signal_strength": 40,
    "distance_from_home": 850,
    "wind_speed": 38,
    "obstacle_detected": True
}
trigger = False

if drone_state["battery"] < 20:
    print("CRITICAL: RTH triggered — Low Battery")
    trigger = True

if drone_state["signal_strength"] < 30:
    print("CRITICAL: RTH triggered — Signal Lost")
    trigger = True

if drone_state["wind_speed"] > 35:
    print("WARNING: RTH triggered — High Wind")
    trigger = True

if drone_state["obstacle_detected"]:
    print("CAUTION: Obstacle detected — Rerouting")
    trigger = True

if not trigger:
    print("All systems nominal")

#descent simulation
print("\nDrone Descending...\n")
while drone_state["altitude"] > 0:
    
    print(f"Altitude: {drone_state['altitude']} m | Battery: {drone_state['battery']}%")
    drone_state["altitude"] -= 15

    if drone_state["altitude"] < 0:
        drone_state["altitude"] = 0

    drone_state["battery"] -= 1
print(f"Altitude: {drone_state['altitude']} m | Battery: {drone_state['battery']}%")