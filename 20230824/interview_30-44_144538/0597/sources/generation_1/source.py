def find_teleport_city(n, m, roads, attacked_cities):
    # Create an adjacency list to represent the road system
    adj_list = [[] for _ in range(n+1)]
    for u, v in roads:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Perform a depth-first search to find the city with the maximum number of attacked cities
    def dfs(node, parent, attacked_cities):
        count = 0
        for neighbor in adj_list[node]:
            if neighbor != parent:
                count += dfs(neighbor, node, attacked_cities)
        if node in attacked_cities:
            count += 1
        return count
    
    max_count = -1
    teleport_city = -1
    
    for city in attacked_cities:
        count = dfs(city, -1, attacked_cities)
        if count > max_count:
            max_count = count
            teleport_city = city
    
    return teleport_city, max_count

# Read the input
n, m = map(int, input().split())
roads = []
for _ in range(n-1):
    u, v = map(int, input().split())
    roads.append((u, v))
attacked_cities = list(map(int, input().split()))

# Find the teleport city and the minimum possible time
teleport_city, min_time = find_teleport_city(n, m, roads, attacked_cities)

# Print the results
print(teleport_city)
print(min_time)