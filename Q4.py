#Q4 Drone Telemetry Log Parser

telemetry = "DRONE_ID:PX4_001|ALT:120.5m|SPEED:18.3kmph|BATT:67%|STATUS:HOVERING|GPS:23.0225N,72.5714E"
#splitting the telemetry string wherever "|" occurs
data = telemetry.split("|")

#extracting values
drone_id = data[0].split(":")[1]
altitude = data[1].split(":")[1]
speed = data[2].split(":")[1]
battery = data[3].split(":")[1]
status = data[4].split(":")[1]
gps = data[5].split(":")[1]

print("Drone ID :", drone_id)
print("Altitude :", altitude)
print("Speed :", speed)
print("Battery :", battery)
print("Status :", status)
print("GPS Coordinates :", gps)

#checking status of hover
contains_hover = "hover" in status.lower()
print("Contains Hover :", contains_hover)

#replacing "HOVERING" with "RETURNING HOME" in the status
status = status.replace("HOVERING", "RETURNING HOME")
print("Updated Status :", status)

#printing formatted summary
latitude, longitude = gps.split(",")
print("\nFormatted Summary:")
print(f"[{drone_id}] Alt: {altitude} | Batt: {battery} | Coords: {latitude}, {longitude}")
print(f"Current Status: {status}")