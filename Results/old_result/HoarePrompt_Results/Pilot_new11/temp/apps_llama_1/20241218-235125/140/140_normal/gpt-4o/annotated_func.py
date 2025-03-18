#State of the program right berfore the function call: n is a positive integer representing the number of vertices in the graph, m is a positive integer representing the number of edges, and edges is a list of pairs of integers where each pair (u, v) represents a directed edge from vertex u to vertex v, such that 1 <= u, v <= n and u!= v.
def func_1(n, m, edges):
    graph = defaultdict(list)
    for (u, v) in edges:
        graph[u].append(v)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `m` is a positive integer, `edges` is a list of pairs of integers representing directed edges, `graph` is a defaultdict of lists where each key `u` has a list of all vertices `v` such that `(u, v)` is in `edges`, and if `edges` is empty, `graph` is a defaultdict of lists with each key `u` having an empty list as its value.
    if (not has_cycle(graph)) :
        return 'YES'
        #The program returns the string 'YES'
    #State of the program after the if block has been executed: `n` is a positive integer, `m` is a positive integer, `edges` is a list of pairs of integers representing directed edges, `graph` is a defaultdict of lists where each key `u` has a list of all vertices `v` such that `(u, v)` is in `edges`, and if `edges` is empty, `graph` is a defaultdict of lists with each key `u` having an empty list as its value. The graph has a cycle.
    for (u, v) in edges:
        graph[u].remove(v)
        
        if not has_cycle(graph):
            return 'YES'
        
        graph[u].append(v)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `m` is a positive integer, `edges` is a list of pairs of integers, and `graph` is a defaultdict of lists representing the graph, with `graph` being either in its original state if no edge removal resulted in a cycle-free graph or modified if an edge removal resulted in a return of 'YES'.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function checks if a directed graph, represented by the number of vertices `n`, the number of edges `m`, and a list of edges `edges`, can be made acyclic by removing at most one edge. It returns 'YES' if such an edge exists and 'NO' otherwise. The function iterates through all edges, checking if the removal of each edge results in an acyclic graph. If it finds an edge whose removal makes the graph acyclic, it immediately returns 'YES'. If no such edge is found after checking all edges, it returns 'NO'. The function handles graphs with any number of vertices and edges, including empty graphs, and correctly identifies whether the removal of a single edge can make the graph acyclic.

#State of the program right berfore the function call: graph is a dictionary representing a directed graph where each key is a vertex (an integer between 1 and n) and each value is a list of vertices that the key vertex has a directed edge to, n is an integer representing the number of vertices in the graph.
def has_cycle(graph):
    in_degree = {i: (0) for i in range(1, n + 1)}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
        
    #State of the program after the  for loop has been executed: `graph` is a dictionary representing a directed graph with `n` vertices, `n` is a non-negative integer representing the original number of vertices in the graph, and `in_degree` is a dictionary where each key is a vertex in the graph and each value is the actual in-degree of that vertex, which is the total number of edges coming into that vertex from all other vertices in the graph.
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    count = 0
    while queue:
        node = queue.popleft()
        
        count += 1
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
        
    #State of the program after the loop has been executed: `graph` remains unchanged, `n` is unchanged, `in_degree` reflects the updated in-degrees after processing, `queue` is empty, and `count` equals the number of nodes reachable from the initial set of nodes with an in-degree of 0 in the graph. If the graph is connected and all nodes are reachable from nodes with an initial in-degree of 0, then `count` equals `n`.
    return count != n
    #The program returns True if the graph contains nodes that are not reachable from the initial set of nodes with an in-degree of 0; otherwise, it returns False.
#Overall this is what the function does:The function `has_cycle` checks if a directed graph contains nodes that are not reachable from the initial set of nodes with an in-degree of 0. It accepts a dictionary `graph` representing a directed graph and an implicit integer `n` representing the number of vertices in the graph, where each key in the dictionary is a vertex and its corresponding value is a list of vertices that the key vertex has a directed edge to. The function returns `True` if the graph contains nodes that are not reachable from the initial set of nodes with an in-degree of 0, indicating the presence of a cycle or disconnected nodes; otherwise, it returns `False`. The function handles all potential cases, including empty graphs, graphs with multiple connected components, and graphs with no nodes having an in-degree of 0. However, it assumes that the input graph is a valid dictionary representation of a directed graph and does not contain any self-loops or multiple edges between the same pair of vertices. The function's return value indicates whether the graph contains a cycle or has disconnected nodes, but does not provide any information about the specific cycle or disconnected nodes.

