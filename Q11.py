#Q11 Recursive Waypoint Distance Calculator
import math

waypoints = [
    (0, 0),
    (3, 4),
    (6, 8),
    (10, 8),
    (10, 0)
]

#defining distance function
def distance(point1, point2):

    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

#recursive function to calculate total distance
def total_distance(waypoints, index=0):

    # Base case
    if index == len(waypoints) - 1:
        return 0

    # Distance of current leg
    current_distance = distance(
        waypoints[index],
        waypoints[index + 1]
    )

    # Add remaining distance recursively
    return current_distance + total_distance(waypoints, index + 1)

#recursive function to find the longest leg
def find_longest_leg(waypoints, index=0, max_dist=0):

    # Base case
    if index == len(waypoints) - 1:
        return max_dist

    # Current leg distance
    current_distance = distance(
        waypoints[index],
        waypoints[index + 1]
    )

    if current_distance > max_dist:
        max_dist = current_distance

    # Recursive call
    return find_longest_leg(
        waypoints,
        index + 1,
        max_dist
    )

#main program
total = total_distance(waypoints)
longest = find_longest_leg(waypoints)

print(f"Total Distance = {total:.2f} units")
print(f"Longest Leg = {longest:.2f} units")