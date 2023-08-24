def is_division_possible(n, c, encounters):
    # Create a dictionary to keep track of the latest encounter year for each participant
    latest_encounter = {}
    for i in range(1, n+1):
        latest_encounter[i] = 2008  # Initialize with the current year 2008
    
    for encounter in encounters:
        a, b, y = encounter
        # Update the latest encounter year for participants a and b if the encounter year is earlier
        latest_encounter[a] = min(latest_encounter[a], y)
        latest_encounter[b] = min(latest_encounter[b], y)
    
    # Find the earliest possible year Y by taking the maximum of the minimum latest encounter years for each participant
    earliest_possible_year = max(min(latest_encounter.values()), 1948)
    
    # Check if it is possible to divide the participants based on the earliest possible year Y
    for encounter in encounters:
        a, b, y = encounter
        # If any pair of participants have both encountered in or after the earliest possible year Y, division is impossible
        if y >= earliest_possible_year:
            return "Impossible"
    
    # Return the earliest possible year Y if division is possible
    return earliest_possible_year

# Read the input values
n, c = map(int, input().split())
encounters = []
for _ in range(c):
    a, b, y = map(int, input().split())
    encounters.append((a, b, y))

# Call the is_division_possible function
result = is_division_possible(n, c, encounters)

# Print the result
print(result)