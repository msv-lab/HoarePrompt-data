# Read input values
a, b, f, k = map(int, input().split())

# Initialize the number of refuels
refuels = 0
# Initial fuel in the tank
fuel = b

# Calculate the total distance to travel
total_distance = 2 * a * k

# Current position of the bus
current_position = 0

# Loop through each journey
for i in range(k):
    if i % 2 == 0:  # Even index: moving from 0 to a
        distance_to_travel = a
        distance_to_fuel_station = f
        distance_after_fuel_station = a - f
    else:  # Odd index: moving from a to 0
        distance_to_travel = a
        distance_to_fuel_station = a - f
        distance_after_fuel_station = f
    
    # Check fuel before reaching the fuel station
    if fuel < distance_to_fuel_station:
        print(-1)
        exit()
    
    # Use fuel to reach the fuel station
    fuel -= distance_to_fuel_station
    
    # Check if the bus needs to refuel at the fuel station
    if fuel < distance_after_fuel_station:
        refuels += 1
        fuel = b
    
    # Use fuel to complete the journey
    fuel -= distance_after_fuel_station
    
    # Update the current position of the bus
    current_position = (current_position + distance_to_travel) % (2 * a)

# Output the total number of refuels
print(refuels)
