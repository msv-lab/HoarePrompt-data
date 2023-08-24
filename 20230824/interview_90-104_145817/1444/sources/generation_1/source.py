def select_stations(n, stations, k):
    # Sort the stations by coordinate
    sorted_stations = sorted(stations)
    
    # Select the k stations with minimum distance between each other
    selected_stations = sorted_stations[:k-1] + sorted_stations[-1:]
    
    # Find the indices of the selected stations in the original list
    indices = [stations.index(station) + 1 for station in selected_stations]
    
    # Return the indices in arbitrary order
    return indices

# Read the input
n = int(input())
stations = list(map(int, input().split()))
k = int(input())

# Select the stations
selected_stations = select_stations(n, stations, k)

# Print the selected stations
print(" ".join(map(str, selected_stations)))