#State of the program right berfore the function call: n is an integer representing the number of vertices (2 ≤ n ≤ 500), m is an integer representing the number of edges (1 ≤ m ≤ min(n(n - 1), 100000)), and edges is a list of tuples where each tuple (u, v) represents a directed edge from vertex u to vertex v (1 ≤ u, v ≤ n, u ≠ v).
def func_1(n, m, edges):
    graph = defaultdict(list)
    for (u, v) in edges:
        graph[u].append(v)
        
    #State of the program after the  for loop has been executed: `n` is an integer representing the number of vertices (2 ≤ n ≤ 500), `m` is an integer representing the number of edges (1 ≤ m ≤ min(n(n - 1), 100000)), `edges` is a list of tuples, `graph` is a defaultdict(list) where for each edge `(u, v)` in `edges`, `graph[u]` contains `[v]`.
    if (not has_cycle(graph)) :
        return 'YES'
        #The program returns 'YES'
    #State of the program after the if block has been executed: *`n` is an integer representing the number of vertices (2 ≤ n ≤ 500), `m` is an integer representing the number of edges (1 ≤ m ≤ min(n(n - 1), 100000)), `edges` is a list of tuples, `graph` is a defaultdict(list) where for each edge `(u, v)` in `edges`, `graph[u]` contains `[v]`. The graph contains at least one cycle.
    for (u, v) in edges:
        graph[u].remove(v)
        
        if not has_cycle(graph):
            return 'YES'
        
        graph[u].append(v)
        
    #State of the program after the  for loop has been executed: `n` is the number of vertices, `m` is the number of edges, `edges` is a list of tuples representing the edges in the graph, `graph` is a defaultdict(list) where for each vertex `u`, `graph[u]` includes `v` as an additional element, and the graph does not contain any cycle.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts three parameters: `n`, `m`, and `edges`. 

- `n` is an integer representing the number of vertices, with the constraint 2 ≤ n ≤ 500.
- `m` is an integer representing the number of edges, with the constraint 1 ≤ m ≤ min(n(n - 1), 100000).
- `edges` is a list of tuples where each tuple (u, v) represents a directed edge from vertex u to vertex v, with the constraints 1 ≤ u, v ≤ n and u ≠ v.

The function constructs a directed graph using the provided edges. It then checks if the graph contains a cycle using the `has_cycle(graph)` function. If the graph contains no cycle initially, it returns 'YES'. Otherwise, it iterates over each edge in the graph, temporarily removing the edge and checking if the graph still contains a cycle. If removing an edge breaks the cycle, it returns 'YES'. If no such edge is found and the graph remains cyclic, it returns 'NO'.

This function effectively determines whether the graph can be made acyclic by removing a single directed edge. The final state of the program after executing the function is either 'YES', indicating that a single edge can be removed to break all cycles, or 'NO', indicating that no single edge can be removed to break all cycles.

#State of the program right berfore the function call: graph is a dictionary where each key is a vertex (an integer between 1 and n inclusive) and the corresponding value is a list of vertices representing the outgoing edges from that vertex. The graph represents a directed graph with n vertices and m edges.
def has_cycle(graph):
    in_degree = {i: (0) for i in range(1, n + 1)}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
        
    #State of the program after the  for loop has been executed: `graph` is a dictionary where each key is a vertex (an integer between 1 and n inclusive) and the corresponding value is a list of vertices representing the outgoing edges from that vertex; `in_degree` is a dictionary where each key is a vertex (an integer between 1 and n inclusive) and the corresponding value is the total number of incoming edges (in-degree) for that vertex; `u` is a vertex that was iterated over in the loop at least once.
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    count = 0
    while queue:
        node = queue.popleft()
        
        count += 1
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
        
    #State of the program after the loop has been executed: `queue` is empty, `count` is the total number of nodes with an in-degree of 0, `node` is the last node dequeued from the queue, `in_degree` dictionary is updated such that each neighbor's in-degree has been decremented by the number of times they became 0.
    return count != n
    #`The program returns count != n where 'count' is the total number of nodes with an in-degree of 0 and 'n' is the total number of nodes in the graph`
#Overall this is what the function does:The function `has_cycle` accepts a directed graph represented as a dictionary and returns whether the graph contains a cycle. Specifically, it performs a topological sorting using Kahn's algorithm (also known as the in-degree zero queue method). The function first calculates the in-degree of each node. Then, it initializes a queue with all nodes having an in-degree of 0 and counts these nodes. It processes each node in the queue by decrementing the in-degrees of its neighbors. If a neighbor's in-degree becomes 0 during this process, it is added to the queue. After processing all nodes, if the count of nodes with an in-degree of 0 is not equal to the total number of nodes (`n`), then the graph contains a cycle, and the function returns `True`. Otherwise, it returns `False`. This means that the function can handle graphs with cycles and graphs without cycles, including edge cases where the graph might have multiple components or nodes with the same in-degrees.

