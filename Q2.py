#Take drone's body and payload weight from user and calculate the total weight of the drone
#Print whether the total weight is above 2 kg or not

bw = float(input("Enter the weight of the drone's body (in g): "))
pw = float(input("Enter the weight of the drone's payload (in g): "))

#total weight calculation
tw = bw + pw

print(f"The total weight of the drone is {tw/1000} kg.")

if tw > 2000:
    print("The total weight is above 2 kg.")
else:
    print("The total weight is not above 2 kg.")