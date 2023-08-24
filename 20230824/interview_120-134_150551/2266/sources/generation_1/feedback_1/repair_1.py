from collections import defaultdict
from queue import Queue

n, k, d = map(int, input().split())
police_stations = list(map(int, input().split()))

adj_list = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

distances = [float("inf")] * n  # Fix bug 2: Initialize distances list with infinity for all cities
for police_station in police_stations:
    distances[police_station-1] = 0  # Subtract 1 from police station index to match 0-based indexing

q = Queue()
for police_station in police_stations:
    q.put(police_station)

visited = [False] * n  # Fix bug 1: Initialize visited list with n elements instead of n+1

while not q.empty():
    city = q.get()
    visited[city-1] = True  # Subtract 1 from city index to match 0-based indexing
    for neighbor in adj_list[city]:
        if not visited[neighbor-1]:
            distances[neighbor-1] = distances[city-1] + 1  # Subtract 1 from city index to match 0-based indexing
            q.put(neighbor)

max_distance = max(distances)  # Fix bug 3: Consider maximum distance among all cities
if max_distance > d:
    print(0)
else:
    ans = []
    for city in range(1, n+1):
        for neighbor in adj_list[city]:
            if distances[city-1] + distances[neighbor-1] + 1 <= 2 * d - max_distance:  # Fix bug 4: Modify condition to include max_distance
                ans.append((city, neighbor))
                break  # Add break statement to print each road only once
    print(len(ans))
    for a, b in ans:
        print(f"{a} {b}")