def assign_edges(n, edges):
    left_edges = []
    right_edges = []
    for edge in edges:
        u, v = edge
        # Check if the edge is already assigned to either left or right tree
        if (u, v) in left_edges or (v, u) in left_edges or (v, u) in right_edges:
            left_edges.append((u, v))
        elif (u, v) in right_edges or (v, u) in right_edges or (u, v) in left_edges:
            right_edges.append((u, v))
        else:
            # Check if adding the edge to left tree will create a cycle
            if has_cycle(left_edges + [(u, v)]) or has_cycle(right_edges + [(u, v)]):
                return "impossible"
            else:
                right_edges.append((u, v))
    assignment = ""
    # Assign "L" to edges in left_edges and "R" to edges in right_edges
    for edge in left_edges:
        if edge in left_edges or edge[::-1] in right_edges:
            assignment += "L"
        else:
            assignment += "R"
    return assignment

def has_cycle(edges):
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    visited = set()
    for node in graph:
        if node not in visited:
            if dfs(node, -1, visited, graph):
                return True
    return False

def dfs(node, parent, visited, graph):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor != parent:
            if neighbor in visited and neighbor != parent or dfs(neighbor, node, visited, graph):
                return True
    return False

# Read inputs
n = int(input())
edges = []
for _ in range(2 * (n - 1)):
    u, v = map(int, input().split())
    edges.append((u, v))

# Assign edges to trees
assignment = assign_edges(n, edges)

# Output the result
print(assignment)