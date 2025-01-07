#State of the program right berfore the function call: n is an integer representing the number of vertices in the graph (2 ≤ n ≤ 500), m is an integer representing the number of directed edges (1 ≤ m ≤ min(n(n - 1), 100000)), and edges is a list of tuples where each tuple (u, v) represents a directed edge from vertex u to vertex v (1 ≤ u, v ≤ n, u ≠ v).
def func_1(n, m, edges):
    graph = defaultdict(list)
    for (u, v) in edges:
        graph[u].append(v)
        
    #State of the program after the  for loop has been executed: `n` is an integer (2 ≤ n ≤ 500); `m` is an integer (1 ≤ m ≤ min(n(n - 1), 100000)); `edges` must contain `m` edges; `graph` is a defaultdict(list) containing directed edges as per the tuples in `edges`. For each edge (u, v) in `edges`, `v` is appended to `graph[u]`, creating a representation of the directed graph.
    if (not has_cycle(graph)) :
        return 'YES'
        #The program returns 'YES', indicating a successful outcome based on the directed graph represented by 'graph' which is built from the provided edges, with no cycles present in the graph.
    #State of the program after the if block has been executed: *`n` is an integer (2 ≤ n ≤ 500); `m` is an integer (1 ≤ m ≤ min(n(n - 1), 100000)); `edges` must contain `m` edges; `graph` is a defaultdict(list) containing directed edges as per the tuples in `edges`. For each edge (u, v) in `edges`, `v` is appended to `graph[u]`, creating a representation of the directed graph. The graph contains at least one cycle.
    for (u, v) in edges:
        graph[u].remove(v)
        
        if not has_cycle(graph):
            return 'YES'
        
        graph[u].append(v)
        
    #State of the program after the  for loop has been executed: `n` is an integer (2 ≤ n ≤ 500), `m` is an integer (1 ≤ m ≤ min(n(n - 1), 100000)), `edges` contains `m` edges, `graph` is a defaultdict(list) representing the edges after all edges have been processed, and the graph still contains at least one cycle.
    return 'NO'
    #The program returns 'NO', indicating that the graph contains at least one cycle
#Overall this is what the function does:The function accepts an integer `n` representing the number of vertices, an integer `m` representing the number of directed edges, and a list of tuples `edges` that represent the directed edges in a graph. It constructs a directed graph and checks for cycles. If the graph is acyclic at the initial state or after removing any single edge, it returns 'YES'. If all checks indicate that the graph contains at least one cycle, the function returns 'NO'. The function does not handle the case where `edges` is empty or when `m` is less than 1, which could lead to unexpected behavior. Therefore, it assumes valid input according to the constraints provided.

#State of the program right berfore the function call: graph is a dictionary where keys are integers representing vertices (1 to n) and values are lists of integers representing directed edges from those vertices; n is an integer representing the number of vertices in the graph, with the condition that n is at least 2.
def has_cycle(graph):
    in_degree = {i: (0) for i in range(1, n + 1)}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
        
    #State of the program after the  for loop has been executed: `in_degree` contains the in-degrees of all vertices in the graph, where each value corresponds to the number of incoming edges for each vertex, and `n` is the total number of vertices in the graph. If the graph is empty (i.e., has no keys), the `in_degree` will remain as initialized, with each vertex having an in-degree of 0.
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    count = 0
    while queue:
        node = queue.popleft()
        
        count += 1
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
        
    #State of the program after the loop has been executed: `in_degree` contains the updated in-degrees of all vertices after processing all reachable vertices from the original nodes in `queue`; `queue` is empty, indicating that all vertices with in-degrees of 0 have been processed; `n` remains the total number of vertices; `count` reflects the total number of vertices that have been processed from `queue`.
    return count != n
    #The program returns whether the total number of vertices processed from queue is not equal to the total number of vertices, indicating whether all vertices have been processed
#Overall this is what the function does:The function accepts a dictionary `graph` representing a directed graph with integer keys as vertices and lists of integers as directed edges. It returns a boolean value indicating whether the graph contains a cycle; specifically, it returns True if there is a cycle (not all vertices can be processed due to unprocessed vertices), and False if the graph is acyclic (all vertices can be processed). The function assumes that `n` (the number of vertices) is at least 2, but it does not handle cases where vertices have no edges, which may lead to misleading results in the context of cycle detection.

