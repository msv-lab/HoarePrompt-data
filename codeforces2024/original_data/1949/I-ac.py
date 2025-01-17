def main():
    n = int(input())  # Number of disks
    x = [None] * n  # x-coordinates of disk centers
    y = [None] * n  # y-coordinates of disk centers
    r = [None] * n  # Radii of disks
    visited = [False] * n  # Track visited disks
    coef = [None] * n  # Coefficients to determine bipartite nature

    # Read input for each disk
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())

    tot = 0  # Total sum of coefficients
    bipartite = True  # Flag to check if graph is bipartite

    # Depth-First Search function
    def dfs(i):
        nonlocal tot, bipartite
        if not visited[i]:
            visited[i] = True  # Mark current disk as visited
            tot += coef[i]  # Add coefficient to total
            for j in range(n):
                # Calculate distance between centers
                dx = x[i] - x[j]
                dy = y[i] - y[j]
                # Check if disks i and j are tangent
                if (r[i] + r[j]) ** 2 == dx ** 2 + dy ** 2:
                    if not visited[j]:
                        coef[j] = -coef[i]  # Assign opposite coefficient
                        dfs(j)  # Recursively visit neighbor
                    else:
                        # Check if already visited neighbor has opposite coefficient
                        bipartite = bipartite and coef[j] == -coef[i]

    ok = False  # Flag to determine if solution is possible
    for i in range(n):
        if not visited[i]:
            coef[i] = 1  # Start with coefficient 1
            tot = 0  # Reset total for new component
            bipartite = True  # Reset bipartite flag
            dfs(i)  # Perform DFS
            # Check if component is bipartite and total is non-zero
            ok = ok or (bipartite and tot != 0)

    # Output result based on the flag
    if ok:
        print("YES")
    else:
        print("NO")

main()