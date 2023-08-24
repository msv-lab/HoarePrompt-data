def is_division_possible(n, c, encounters):
    # Create a dictionary to keep track of encounter years for each participant pair
    all_encounter_years = {}
    
    # Initialize the dictionary with an empty list for each participant pair
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            all_encounter_years[(i, j)] = []
    
    # Update the dictionary with the encounter years for each participant pair
    for encounter in encounters:
        a, b, y = encounter
        all_encounter_years[(a, b)].append(y)
    
    # Find the maximum latest encounter year for each participant
    max_latest_encounter_year = {}
    for i in range(1, n+1):
        max_latest_encounter_year[i] = max(all_encounter_years[(i, j)] for j in range(i+1, n+1))
    
    # Find the earliest possible year Y by taking the minimum of the maximum latest encounter years
    earliest_possible_year = min(max_latest_encounter_year.values())
    
    # Check if it is possible to divide the participants based on the earliest possible year Y
    for encounter in encounters:
        a, b, y = encounter
        # If any pair of participants have both encountered either before the earliest possible year or after the earliest possible year, division is impossible
        if y < earliest_possible_year or y > earliest_possible_year:
            return earliest_possible_year
    
    # Return "Impossible" if division is impossible
    return "Impossible"

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