import math
from collections import defaultdict

# Helper function to calculate Euclidean distance
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to build the graph and check for conditions
def can_change_radii(n, disks):
    # Build a graph of tangent disks
    graph = defaultdict(list)
    for i in range(n):
        x1, y1, r1 = disks[i]
        for j in range(i + 1, n):
            x2, y2, r2 = disks[j]
            d = distance(x1, y1, x2, y2)
            # Check if disks are tangent
            if abs(d - (r1 + r2)) < 1e-6 or abs(d - abs(r1 - r2)) < 1e-6:
                graph[i].append(j)
                graph[j].append(i)
    
    # Use DFS to explore connected components
    visited = [False] * n

    def dfs(node):
        stack = [node]
        component = []
        while stack:
            u = stack.pop()
            if not visited[u]:
                visited[u] = True
                component.append(u)
                for v in graph[u]:
                    if not visited[v]:
                        stack.append(v)
        return component

    # Check each component
    for i in range(n):
        if not visited[i]:
            component = dfs(i)
            # Analyze if we can adjust radii in this component
            # Placeholder for the actual logic to determine radius adjustment
            # Here you need to implement the logic to see if the sum of radii can decrease
            # while maintaining tangency. This part can be complex and may involve math/geometry.
            if not is_adjustment_possible(component, disks):
                return "NO"

    return "YES"

# Function to check if radius adjustment is possible (to be implemented)
def is_adjustment_possible(component, disks):
    # Implement logic to check if the radii can be adjusted in this component
    return True  # Placeholder

# Input reading
n = int(input())
disks = [tuple(map(int, input().split())) for _ in range(n)]
print(can_change_radii(n, disks))
