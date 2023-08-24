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
    dist[airport] = (lat, lon, float('inf'))

# Start from the starting airport
dist[start] = (float(dist[start][0]), float(dist[start][1]), 0)

# Dijkstra's algorithm
visited = set()
while len(visited) < N:
    min_dist = float('inf')
    u = None
    
    # Find the next airport to visit
    for airport in dist:
        if airport not in visited and dist[airport][2] < min_dist:
            min_dist = dist[airport][2]
            u = airport
    
    visited.add(u)
    
    # Update distances to neighboring airports
    for airport in dist:
        if airport != u:
            airport1, lat1, lon1 = u, dist[u][0], dist[u][1]
            airport2, lat2, lon2 = airport, dist[airport][0], dist[airport][1]
            distance = calculate_distance(lat1, lon1, lat2, lon2)
        
            if dist[airport2][2] > dist[airport1][2] + distance:
                dist[airport2] = (lat2, lon2, dist[airport1][2] + distance)

# Check if the target is reachable
if dist[target][2] == float('inf'):
    print(-1)
else:
    # Calculate the total shame
    total_shame = dist[target][2] + 100 * (len(visited) - 1)
    print(total_shame)