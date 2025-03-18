def func_1(n, edges, start):
    tree = defaultdict(list)
    for (u, v) in edges:
        tree[u].append(v)
        tree[v].append(u)
    leaves = [node for node in tree if len(tree[node]) == 1]

    def bfs(start, target):
        queue = deque([(start, 0)])
        visited = set([start])
        while queue:
            (current, dist) = queue.popleft()
            if current == target:
                return dist
            for neighbor in tree[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        return -1
    dist1 = bfs(start, leaves[0])
    dist2 = bfs(start, leaves[1])
    if dist1 % 2 == 1 or dist2 % 2 == 1:
        return 'Ron'
    else:
        return 'Hermione'
(n, t) = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
starts = list(map(int, input().split()))
start = starts[0]
print(func_1(n, edges, start))