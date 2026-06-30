#Q7 Fleet health monitor

#fleet dictionary
fleet = {
    "PX4_001": {"battery": 87, "altitude": 120, "status": "active", "payload_kg": 1.2},
    "PX4_002": {"battery": 23, "altitude": 0, "status": "grounded", "payload_kg": 0},
    "PX4_003": {"battery": 56, "altitude": 85, "status": "active", "payload_kg": 0.8},
    "PX4_004": {"battery": 11, "altitude": 30, "status": "returning", "payload_kg": 0.5},
}

#adding PX4_005
fleet["PX4_005"] = {"battery": 95, "altitude": 0, "status": "standby", "payload_kg": 0}
print(f"Added Drone: PX4_005 -> {fleet['PX4_005']}")
#removing PX4_002
removed_drone = fleet.pop("PX4_002")
print(f"Removed Drone: PX4_002 -> {removed_drone}")

#printing all active drones
print("\nActive Drones:")
for drone_id, details in fleet.items():
    if details["status"] == "active":
        print(f"Drone ID: {drone_id}, Battery: {details['battery']}%")

#lowest battery drone
lowest_battery = 101
lowest_drone = ""
for drone_id, details in fleet.items():
    if details["battery"] < lowest_battery:
        lowest_battery = details["battery"]
        lowest_drone = drone_id
print(f"\nDrone with Lowest Battery: {lowest_drone} -> {lowest_battery}%")

#fleet summary
print("\nFleet Summary:")
for drone_id, details in fleet.items():
    print(f"{drone_id} -> {details}")