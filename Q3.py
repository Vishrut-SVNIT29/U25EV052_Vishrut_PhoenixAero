#Q3 Perform operations using drone specifications

#Maximum weight the drone can take off with (in kg)
max_takeoff_weight = 4.5

#Weight of the drone frame (in kg)
frame_weight = 1.2

#Weight of the battery (in kg)
battery_weight = 0.8

#Number of propellers
num_propellers = 4

#Weight of one motor (in kg)
motor_weight = 0.075

#GPS availability
is_gps_enabled = True

#Weight of GPS module (in kg)
gps_module_weight = 0.05

#calculating maximum payload capacity
drone_weight = frame_weight + battery_weight + (num_propellers * motor_weight) + gps_module_weight
max_payload_capacity = max_takeoff_weight - drone_weight
print("Maximum payload capacity of the drone is:", max_payload_capacity, "kg")

#printing the datatype of each variable
print("\nData Types:")
print(type(max_takeoff_weight))
print(type(frame_weight))
print(type(battery_weight))
print(type(num_propellers))
print(type(motor_weight))
print(type(is_gps_enabled))
print(type(gps_module_weight))
print(type(drone_weight))
print(type(max_payload_capacity))

#checking if camera can be carried as payload
camera_weight = 1.8
print("\nCan carry 1.8 kg camera?")
print(max_payload_capacity >= camera_weight)

#converting max payload capacity to grams and storing in int
max_payload_capacity_grams = int(max_payload_capacity * 1000)
print("\nMax payload capacity in grams:", max_payload_capacity_grams)