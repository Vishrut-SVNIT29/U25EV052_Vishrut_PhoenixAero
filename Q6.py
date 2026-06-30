#Q6 Waypoint mission planner

#tuple of waypoints
waypoints = (
    ("WP1", 23.0225, 72.5714, 50),
    ("WP2", 23.0312, 72.5801, 80),
    ("WP3", 23.0401, 72.5900, 100),
    ("WP4", 23.0225, 72.5714, 0),
)
#total waypoints
print(f"Total Waypoints: {len(waypoints)}")

#printing waypoints separately
for waypoint in waypoints:
    #tuple unpacking
    name, latitude, longitude, altitude = waypoint
    print(f"{name} -> Latitude: {latitude}, Longitude: {longitude}, Altitude: {altitude} m")

#waypoint with maximum altitude
hwp = waypoints[0]
for waypoint in waypoints:
    if waypoint[3] > hwp[3]:
        hwp = waypoint
print(f"Waypoint with maximum altitude: {hwp[0]}")

#checking wp2
cwp = ("WP2", 23.0312, 72.5801, 80)
print(f"\nChecking if WP2 exists in waypoints: {'Yes' if cwp in waypoints else 'No'}")

#modifying wp1
try:
    # Tuples are immutable, so this will raise an error
    waypoints[0][3] = 60

except TypeError:
    print("\nWaypoint data is immutable — mission integrity protected!")