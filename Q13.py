#Q13 Movement calculator with user input coordinates

#taking both coordinates together
x, y = map(int, input("Enter the starting coordinates (x y): ").split())
movement = input("Enter movement (horizontal/vertical): ").lower()
steps = int(input("Enter number of steps: "))

print("\nDrone Movement:")
# Horizontal movement
if movement == "horizontal":

    for i in range(steps):
        x += 1
        print(f"({x}, {y})")

# Vertical movement
elif movement == "vertical":

    for i in range(steps):
        y += 1
        print(f"({x}, {y})")

# Invalid input
else:
    print("Invalid movement.")
