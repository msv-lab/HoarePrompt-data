import math

def calculate_distance(lat1, lon1, lat2, lon2):
    # Convert degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    # Difference in latitudes and longitudes
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Haversine formula to calculate distance
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = 6381 * c
    
    return distance


# Read input
N, M = map(int, input().split())
start, target = input().split()

# Initialize distances to infinity
dist = {}
for i in range(N):
    airport, lat, lon = input().split()
    lat = float(lat)
    lon = float(lon)
    dist[airport] = float('inf')

# Start from the starting airport
dist[start] = 0

# Dijkstra's algorithm
visited = set()
while len(visited) < N:
    min_dist = float('inf')
    u = None
    
    # Find the next airport to visit
    for airport in dist:
        if airport not in visited and dist[airport] < min_dist:
            min_dist = dist[airport]
            u = airport
    
    visited.add(u)
    
    # Update distances to neighboring airports
    for v in range(N):
        airport1, lat1, lon1 = airport
        airport2, lat2, lon2 = airports[v]
        distance = calculate_distance(lat1, lon1, lat2, lon2)
        
        if dist[airport2] > dist[airport1] + distance:
            dist[airport2] = dist[airport1] + distance

# Check if the target is reachable
if dist[target] == float('inf'):
    print(-1)
else:
    # Calculate the total shame
    total_shame = dist[target] + 100 * (len(visisted) - 1)
    print(total_shame)