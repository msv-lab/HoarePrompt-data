from collections import defaultdict
from queue import Queue

n, k, d = map(int, input().split())
police_stations = list(map(int, input().split()))

adj_list = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

distances = [float("inf")] * (n+1)
for police_station in police_stations:
    distances[police_station] = 0

q = Queue()
for police_station in police_stations:
    q.put(police_station)

visited = [False] * (n+1)
while not q.empty():
    city = q.get()
    visited[city] = True
    for neighbor in adj_list[city]:
        if not visited[neighbor]:
            distances[neighbor] = distances[city] + 1
            q.put(neighbor)

max_distance = max(distances[1:])
if max_distance > d:
    print(0)
else:
    ans = []
    for city in range(1, n+1):
        for neighbor in adj_list[city]:
            if distances[city] + 1 + distances[neighbor] <= 2 * d:
                ans.append((city, neighbor))
    print(len(ans))
    for a, b in ans:
        print(f"{a} {b}")