import sys
from collections import deque

def bfs(n, adj, start):
    d = [0] * (n + 1)
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                queue.append(v)
    return d

def main():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = int(data[index])
        index += 1
        b = int(data[index])
        index += 1
        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            x = int(data[index])
            index += 1
            y = int(data[index])
            index += 1
            adj[x].append(y)
            adj[y].append(x)
        d_a = bfs(n, adj, a)
        d_b = bfs(n, adj, b)
        max_steps = 0
        for v in range(1, n + 1):
            max_steps = max(max_steps, d_a[v] + d_b[v])
        print(max_steps)

if __name__ == "__main__":
    main()