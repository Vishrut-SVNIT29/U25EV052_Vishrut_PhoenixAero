#Q1 Drone movement program
#Take number from user and roll, pitch or yaw the drone accordingly

print("Enter a number to control the drone movement:")
print("1: Roll")
print("2: Pitch")
print("3: Yaw")          

c = int(input("Enter your choice (1-3): "))

#if-else-if ladder for the choice entered
if c == 1:
    print("Slow down left motors for left roll or right motors for right roll")
elif c == 2:
    print("Slow down front motors for pitch forward or back motors for pitch backward")
elif c == 3:
    print("Slow down counter-clockwise motors for yaw left or clockwise motors for yaw right")
else:
    print("Invalid choice!")