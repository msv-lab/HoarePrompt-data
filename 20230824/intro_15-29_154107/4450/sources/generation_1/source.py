def floyd_warshall(graph, n):
    # Initialize the matrix of shortest paths
    shortest_paths = [[float('inf')] * n for _ in range(n)]

    # Assign the weight of direct edges to the matrix
    for i in range(n):
        shortest_paths[i][i] = 0
        for j, weight in graph[i]:
            shortest_paths[i][j] = weight
            shortest_paths[j][i] = weight

    # Calculate shortest paths using Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(i):
                shortest_paths[i][j] = min(shortest_paths[i][j], shortest_paths[i][k] + shortest_paths[k][j])
                shortest_paths[j][i] = shortest_paths[i][j]

    return shortest_paths

def kth_smallest_shortest_path(n, m, k, edges):
    # Create the adjacency list representation of the graph
    graph = [[] for _ in range(n)]
    for x, y, w in edges:
        graph[x-1].append((y-1, w))
        graph[y-1].append((x-1, w))

    # Calculate the shortest paths using Floyd-Warshall algorithm
    shortest_paths = floyd_warshall(graph, n)

    # Create a list of all unique shortest path lengths
    path_lengths = set()
    for i in range(n):
        for j in range(i):
            path_lengths.add(shortest_paths[i][j])

    # Sort the path lengths and return the k-th element
    sorted_path_lengths = sorted(path_lengths)
    return sorted_path_lengths[k-1]

# Read the input values
n, m, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function to find the k-th smallest shortest path
result = kth_smallest_shortest_path(n, m, k, edges)

# Print the result
print(result)