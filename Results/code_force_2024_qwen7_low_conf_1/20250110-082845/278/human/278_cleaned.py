def func_1(n, edges):
    graph = defaultdict(list)
    for (u, v) in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * (n + 1)
    components = []

    def bfs(start):
        queue = deque([start])
        component = []
        while queue:
            node = queue.popleft()
            if not visited[node]:
                visited[node] = True
                component.append(node)
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
        return component
    for i in range(1, n + 1):
        if not visited[i]:
            components.append(bfs(i))
    return components

def func_2(n, m, c, edges):
    components = func_1(n, edges)
    if len(components) == 1:
        return -1
    min_cost = float('inf')
    for i in range(len(components)):
        for j in range(i + 1, len(components)):
            cost_i = len(components[i]) ** 2
            cost_j = len(components[j]) ** 2
            min_cost = min(min_cost, cost_i + cost_j + c)
    return min_cost
t = int(input())
for _ in range(t):
    (n, m, c) = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(func_2(n, m, c, edges))