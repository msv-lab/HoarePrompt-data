#State of the program right berfore the function call: n is an integer representing the number of vertices in the graph (2 ≤ n ≤ 500); m is an integer representing the number of directed edges (1 ≤ m ≤ min(n(n - 1), 100000)); edges is a list of tuples, where each tuple (u, v) represents a directed edge from vertex u to vertex v, with 1 ≤ u, v ≤ n and u ≠ v.
def func_1(n, m, edges):
    graph = defaultdict(list)
    for (u, v) in edges:
        graph[u].append(v)
        
    #State of the program after the  for loop has been executed: `n` is an integer (2 ≤ n ≤ 500), `m` is an integer (1 ≤ m ≤ min(n(n - 1), 100000)), `edges` is a list of tuples representing directed edges, `graph` is a defaultdict of lists where each vertex u has a list of vertices v that it points to, and `graph` contains all edges from the list `edges`.
    if (not has_cycle(graph)) :
        return 'YES'
        #The program returns 'YES', indicating a valid condition in the directed graph represented by 'graph' without cycles.
    #State of the program after the if block has been executed: *`n` is an integer (2 ≤ n ≤ 500), `m` is an integer (1 ≤ m ≤ min(n(n - 1), 100000)), `edges` is a list of tuples representing directed edges, `graph` is a defaultdict of lists where each vertex u has a list of vertices v that it points to, and `graph` contains all edges from the list `edges`. The graph contains at least one cycle.
    for (u, v) in edges:
        graph[u].remove(v)
        
        if not has_cycle(graph):
            return 'YES'
        
        graph[u].append(v)
        
    #State of the program after the  for loop has been executed: `n` is an integer (2 ≤ n ≤ 500), `m` is an integer (1 ≤ m ≤ min(n(n - 1), 100000)), `edges` is a list of tuples containing all edges, `graph` contains all edges from `edges`, and the graph contains at least one cycle.
    return 'NO'
    #The program returns 'NO' indicating a specific condition about the graph with at least one cycle
#Overall this is what the function does:The function accepts two integers `n` (the number of vertices, where 2 ≤ n ≤ 500) and `m` (the number of directed edges, where 1 ≤ m ≤ min(n(n - 1), 100000)), along with a list of tuples `edges` representing directed edges between the vertices. It checks for cycles in the directed graph formed by these edges. If the graph does not contain any cycles, it returns 'YES'. If at least one cycle is detected, it attempts to remove edges one by one and checks again for cycles. If it finds that removing an edge results in a cycle-free graph, it returns 'YES'. If all edges are checked and cycles still exist, it ultimately returns 'NO'. The function does not handle cases where the input lists may be empty or when the edges contain invalid vertices, which could lead to unexpected behavior.

#State of the program right berfore the function call: graph is a dictionary where keys are integers representing vertices (1 to n) and values are lists of integers representing directed edges from each vertex. n is an integer representing the number of vertices in the graph, where 2 ≤ n ≤ 500.
def has_cycle(graph):
    in_degree = {i: (0) for i in range(1, n + 1)}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
        
    #State of the program after the  for loop has been executed: `in_degree[v]` is equal to the total number of incoming edges directed to vertex `v` for all vertices `v` in `graph`; `graph` is a dictionary where keys are integers representing vertices and values are lists of integers representing directed edges from each vertex; `u` is each vertex in `graph` during the iteration.
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    count = 0
    while queue:
        node = queue.popleft()
        
        count += 1
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
        
    #State of the program after the loop has been executed: `in_degree[v]` for all vertices `v` in `graph` is equal to the total number of incoming edges directed to vertex `v` after processing all nodes in `queue`; `queue` is empty, indicating all nodes with zero in-degrees have been processed, and `count` is equal to the total number of nodes in the graph that had zero incoming edges initially, plus any additional nodes that had their in-degree reduced to zero during the loop execution. If `queue` was initially empty, then `in_degree[v]` remains unchanged, `queue` is empty, and `count` is 0.
    return count != n
    #The program returns True if the total number of nodes processed (count) is not equal to the total number of nodes in the graph (n)
#Overall this is what the function does:The function accepts a dictionary `graph` representing a directed graph, where keys are integers (vertices) and values are lists of integers (edges). It determines whether the graph contains a cycle by checking if the total number of processed nodes (count) equals the total number of vertices (n). It returns True if there is a cycle, indicated by `count` being not equal to `n`, and False if there is no cycle, meaning all nodes were processed successfully. The function is designed to handle graphs with 2 to 500 vertices.

