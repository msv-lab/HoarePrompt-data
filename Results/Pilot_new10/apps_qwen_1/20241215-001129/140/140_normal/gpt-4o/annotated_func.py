#State of the program right berfore the function call: n is an integer representing the number of vertices in the directed graph, m is an integer representing the number of edges, and edges is a list of tuples where each tuple (u, v) represents a directed edge from vertex u to vertex v.
def func_1(n, m, edges):
    graph = defaultdict(list)
    for (u, v) in edges:
        graph[u].append(v)
        
    #State of the program after the  for loop has been executed: `n` is an integer representing the number of vertices in the directed graph, `m` is an integer representing the number of edges, `edges` is a list of tuples where each tuple (u, v) represents a directed edge from vertex u to vertex v, `graph` is a defaultdict where the default factory is list, and for each (u, v) in `edges`, the list associated with the key u in `graph` now includes the vertex v.
    if (not has_cycle(graph)) :
        return 'YES'
        #The program returns 'YES'
    #State of the program after the if block has been executed: `n` is an integer representing the number of vertices in the directed graph, `m` is an integer representing the number of edges, `edges` is a list of tuples where each tuple (u, v) represents a directed edge from vertex u to vertex v, `graph` is a defaultdict where the default factory is list, and for each (u, v) in `edges`, the list associated with the key u in `graph` now includes the vertex v, and the graph contains at least one cycle
    for (u, v) in edges:
        graph[u].remove(v)
        
        if not has_cycle(graph):
            return 'YES'
        
        graph[u].append(v)
        
    #State of the program after the  for loop has been executed: `n` is the number of vertices in the directed graph, `m` is the number of edges (reduced by the number of iterations), `edges` is an empty list, `graph` is a defaultdict where the default factory is list, and for each `(u, v)` in the original `edges`, the list associated with the key `u` in `graph` no longer includes `v`, the graph does not contain any cycles.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts three parameters: `n`, `m`, and `edges`, where `n` is the number of vertices in a directed graph, `m` is the number of edges, and `edges` is a list of tuples representing directed edges. The function constructs a graph using the given edges and checks if the graph contains a cycle. If the graph initially does not contain a cycle, the function returns 'YES'. Otherwise, it attempts to remove each edge temporarily, checking if the graph still contains a cycle after each removal. If removing any edge results in a graph without a cycle, the function returns 'YES'. If no such edge is found, the function returns 'NO'.

#State of the program right berfore the function call: graph is a dictionary where keys are integers representing vertices, and values are lists of integers representing the vertices that each key vertex has outgoing edges to; n and m are integers such that 2 ≤ n ≤ 500 and 1 ≤ m ≤ min(n(n - 1), 100000), representing the number of vertices and edges in the graph, respectively.
def has_cycle(graph):
    in_degree = {i: (0) for i in range(1, n + 1)}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
        
    #State of the program after the  for loop has been executed: `graph` remains a dictionary where keys are integers representing vertices, and values are lists of integers representing the vertices that each key vertex has outgoing edges to; `n` and `m` remain as originally defined, but they do not change; `in_degree` is a dictionary where each key from 1 to `n` is mapped to an integer representing the total number of incoming edges to that vertex, and this integer is incremented by the number of times each vertex `v` appears in the lists of vertices that have outgoing edges from any vertex `u`.
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    count = 0
    while queue:
        node = queue.popleft()
        
        count += 1
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
        
    #State of the program after the loop has been executed: `graph[node]` is an empty list for all nodes, `queue` is an empty deque containing no nodes, `in_degree` is a dictionary where the value of each key (from 1 to `n`) is 0, and `count` is the total number of nodes with an in-degree of 0 that were processed during the entire execution of the loop.
    return count != n
    #The program returns a boolean value indicating whether not all nodes have an in-degree of 0
#Overall this is what the function does:The function `has_cycle` accepts a graph represented as a dictionary where keys are integers representing vertices, and values are lists of integers representing the vertices that each key vertex has outgoing edges to. It also accepts integers `n` and `m`, representing the number of vertices and edges in the graph, respectively. The function determines whether the graph contains at least one cycle by checking the in-degrees of the vertices. It returns `True` if there is at least one vertex with an in-degree not equal to 0, indicating the presence of a cycle, and `False` otherwise.

