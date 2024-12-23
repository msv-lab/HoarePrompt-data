def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    p = list(map(int, data[1:n+1]))
    b = list(map(int, data[n+1:2*n+1]))

    # Find cycles in the permutation p
    visited = [False] * n
    cycles = []
    for i in range(n):
        if not visited[i]:
            cycle = []
            x = i
            while not visited[x]:
                visited[x] = True
                cycle.append(x)
                x = p[x] - 1
            cycles.append(cycle)
    
    # Check number of components with no reversals
    no_reverse_components = sum(all(b[x] == 0 for x in cycle) for cycle in cycles)
    
    # If there is only one component, no change needed
    if len(cycles) == 1:
        print(0)
    else:
        # Otherwise, we need to ensure at least one reversal in each component
        print(no_reverse_components if no_reverse_components > 0 else 1)

# Use Standard Input format
solve()
