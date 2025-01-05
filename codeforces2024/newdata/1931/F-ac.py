from sys import stdin, stdout

input = stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    
    # Graph representation: G[i] contains nodes that i points to
    G = [set() for _ in range(n + 1)]
    # In-degree array: I[i] is the number of edges pointing to i
    I = [0] * (n + 1)
    
    for _ in range(k):
        a = list(map(int, input().split()))
        # Create directed edges based on the screenshot
        for a, b in zip(a[1:], a[2:]):
            if b not in G[a]:
                G[a].add(b)
                I[b] += 1
    
    # Queue for topological sorting
    Q = [i for i in range(1, n + 1) if I[i] == 0]
    C = 0  # Counter for number of nodes processed
    
    # Process nodes with zero in-degree
    for x in Q:
        C += 1
        for y in G[x]:
            I[y] -= 1
            if I[y] == 0:
                Q.append(y)
    
    # If all nodes are processed, a valid order exists
    stdout.write("YES\n" if C == n else "NO\n")