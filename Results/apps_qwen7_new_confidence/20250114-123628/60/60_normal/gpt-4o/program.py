def can_sort_array(n, arr, swaps):
    def dfs(start, visited, graph):
        stack = [start]
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

    # Create a graph where each node is connected if a swap is allowed
    graph = {i: [] for i in range(n)}
    for i in range(n - 1):
        if swaps[i] == '1':
            graph[i].append(i + 1)
            graph[i + 1].append(i)

    visited = set()
    for i in range(n):
        if i not in visited:
            # Collect all indices in the connected component
            component = set()
            dfs(i, component, graph)
            # Extract values from the array corresponding to this component
            values = [arr[j] for j in component]
            # Sort these values
            values.sort()
            # Check if sorting these values matches the sorted order of indices
            sorted_indices = sorted(component)
            for idx, sorted_index in enumerate(sorted_indices):
                if arr[sorted_index] != values[idx]:
                    return "NO"
            visited.update(component)
    return "YES"

# Read input
n = int(input())
arr = list(map(int, input().split()))
swaps = input().strip()

# Output the result
print(can_sort_array(n, arr, swaps))
