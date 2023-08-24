# Read input
m, k = map(int, input().split())
d = list(map(int, input().split()))
s = list(map(int, input().split()))

# Initialize variables
time = 0
fuel = 0

# Iterate over the roads
for i in range(m):
    # Update the time required to travel to the next city
    time += d[i]
    # Calculate the remaining fuel after traveling
    fuel -= d[i] * k
    
    # If the remaining fuel is negative or zero, refuel
    if fuel <= 0:
        # Calculate the amount of fuel to refuel
        refuel = abs(fuel) + 1
        # Calculate the waiting time to refuel
        wait = (refuel // s[i] + 1) * k
        # Update the time and fuel variables
        time += wait
        fuel = refuel % s[i]
    
    # Add the fuel supply of the next city to the fuel tank
    fuel += s[i] - (refuel % s[i])

# Print the minimum time required to reach the last city
print(time)