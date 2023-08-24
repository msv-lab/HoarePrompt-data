import itertools

def select_stations(n, stations, k):
    # Create a dictionary to store the index of each station
    station_indices = {station: index + 1 for index, station in enumerate(stations)}
    
    # Generate all combinations of k stations
    combinations = itertools.combinations(stations, k)
    
    # Initialize variables for minimum average commute time and selected stations
    min_avg_commute_time = float('inf')
    selected_stations = []
    
    # Iterate over all combinations and calculate the average commute time
    for combination in combinations:
        avg_commute_time = sum(abs(station_indices[combination[i]] - station_indices[combination[j]]) for i in range(k) for j in range(i + 1, k)) / (k * (k - 1) / 2)
        if avg_commute_time < min_avg_commute_time:
            min_avg_commute_time = avg_commute_time
            selected_stations = [station_indices[station] for station in combination]
    
    # Sort the selected stations in ascending order
    selected_stations.sort()
    
    # Return the selected stations
    return selected_stations

# Read the input
n = int(input())
stations = list(map(int, input().split()))
k = int(input())

# Select the stations
selected_stations = select_stations(n, stations, k)

# Print the selected stations
print(" ".join(map(str, selected_stations)))