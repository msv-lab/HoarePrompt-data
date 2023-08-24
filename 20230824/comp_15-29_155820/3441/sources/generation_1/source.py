def find_max_roads(n, m, roads):
    graph = [[] for _ in range(n)]
    for road in roads:
        x, y = road
        graph[x].append(y)
    
    # Perform DFS on each town
    visited = [False] * n
    max_roads = 0
    for i in range(n):
        if not visited[i]:
            stack = [i]
            while stack:
                town = stack.pop()
                visited[town] = True
                for neighbor in graph[town]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
                        max_roads += 1
    
    return max_roads

# Read input
n, m = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]

# Call function and print result
result = find_max_roads(n, m, roads)
print(result)