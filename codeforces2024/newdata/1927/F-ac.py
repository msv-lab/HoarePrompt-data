from collections import deque

def find(n):
    # This function finds the root of the node `n` in the Union-Find structure.
    # It also performs path compression to make future queries faster.
    ans = []
    while uf[n] != n:
        ans.append(n)
        n = uf[n]
    for an in ans:
        uf[an] = n
    return n

t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    uf = [i for i in range(N + 1)]  # Initialize Union-Find structure
    ed = [[] for _ in range(N + 1)]  # Adjacency list for the graph
    qu = []  # List to store edges

    for _ in range(M):
        a, b, c = map(int, input().split())
        qu.append((a, b, c))
        ed[a].append(b)
        ed[b].append(a)

    qu.sort(key=lambda x: x[2])  # Sort edges by weight

    x, y, z = 0, 0, 0  # Variables to store the cycle's edge

    while qu:
        a, b, c = qu.pop()  # Process the heaviest edge first
        p_a, p_b = find(a), find(b)

        if p_a == p_b:
            # If a cycle is detected, store the edge
            x, y, z = a, b, c
        elif p_a > p_b:
            uf[p_a] = p_b  # Union operation
        else:
            uf[p_b] = p_a

    v = [0] * (N + 1)  # Visited array for BFS
    ed[y].remove(x)  # Remove the edge to find the cycle path
    q = deque()
    q.append(y)
    v[y] = 1

    while q:
        n = q.popleft()
        if n == x:
            break
        for ne in ed[n]:
            if not v[ne]:
                v[ne] = v[n] + 1
                q.append(ne)

    pt = [x]  # Path of the cycle

    while pt[-1] != y:
        n = pt[-1]
        for ne in ed[n]:
            if v[ne] == v[n] - 1:
                pt.append(ne)
                break

    print(z, len(pt))  # Output the weight of the lightest edge and the cycle length
    print(*pt)  # Output the vertices in the cycle