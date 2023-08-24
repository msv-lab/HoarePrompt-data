n, m = map(int, input().split())
roads = []
adj_list = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    roads.append((u, v))
    adj_list[u].append(v)
    adj_list[v].append(u)

attacked_cities = list(map(int, input().split()))

max_count = -1
teleport_city = n

def dfs(node, parent, attacked_cities):
    count = 0

    for neighbor in adj_list[node]:
        if neighbor != parent:
            count += dfs(neighbor, node, attacked_cities)
        
    if node in attacked_cities:
        count += 1

    return count

for city in attacked_cities:
    count = dfs(city, -1, attacked_cities)

    if count > max_count or (count == max_count and city < teleport_city):
        max_count = count
        teleport_city = city

print(teleport_city)
print(max_count)