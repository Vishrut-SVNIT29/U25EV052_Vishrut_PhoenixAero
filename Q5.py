#Q5 Flight path analyzer

#storing altitudes in a list
altitudes = [0, 15, 42, 78, 120, 118, 115, 50, 20, 0] 

#finding the maximum altitude and its index
max_alt = max(altitudes)
sec = altitudes.index(max_alt)  
print(f"Maximum Altitude: {max_alt}")
print(f"Index of Maximum Altitude: {sec}")

#calculating the average altitude
avg_alt = sum(altitudes) / len(altitudes)
print(f"Average Altitude: {avg_alt}")

#climb rates list
climb_rates = []
for i in range(len(altitudes) - 1):
    climb_rates.append(altitudes[i + 1] - altitudes[i])
print(f"\nClimb Rates: {climb_rates}")

#steep climb and descent
steep_climb = max(climb_rates)
steep_descent = min(climb_rates)
print(f"Steepest Climb Rate: {steep_climb}")
print(f"Steepest Descent Rate: {steep_descent}")

#removing zero altitudes
trimmed_path = []
for altitude in altitudes:
    if altitude != 0:
        trimmed_path.append(altitude)
print(f"\nTrimmed Flight Path: {trimmed_path}")