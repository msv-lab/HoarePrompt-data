#State of the program right berfore the function call: n is an integer representing the number of vertices in the graph (2 ≤ n ≤ 500), m is an integer representing the number of directed edges (1 ≤ m ≤ min(n(n - 1), 100000)), and edges is a list of tuples where each tuple (u, v) contains integers representing directed edges such that 1 ≤ u, v ≤ n and u ≠ v.
def func_1(n, m, edges):
    graph = defaultdict(list)
    for (u, v) in edges:
        graph[u].append(v)
        
    #State of the program after the  for loop has been executed: `n` is an integer (2 ≤ n ≤ 500), `m` is an integer (1 ≤ m ≤ min(n(n - 1), 100000)), `edges` is a list of tuples containing `m` valid edges, and `graph` is a defaultdict where each key is a vertex `u` and each value is a list containing all vertices `v` that `u` points to from the edges list.
    if (not has_cycle(graph)) :
        return 'YES'
        #The program returns 'YES' indicating that the current state of the graph does not have any cycles.
    #State of the program after the if block has been executed: *`n` is an integer (2 ≤ n ≤ 500), `m` is an integer (1 ≤ m ≤ min(n(n - 1), 100000)), `edges` is a list of tuples containing `m` valid edges, and `graph` is a defaultdict where each key is a vertex `u` and each value is a list containing all vertices `v` that `u` points to from the edges list. The graph represented by `edges` contains at least one cycle.
    for (u, v) in edges:
        graph[u].remove(v)
        
        if not has_cycle(graph):
            return 'YES'
        
        graph[u].append(v)
        
    #State of the program after the  for loop has been executed: `n` is an integer (2 ≤ n ≤ 500), `m` is an integer (1 ≤ m ≤ min(n(n - 1), 100000)), `edges` is a list containing all valid edges, `graph` is a defaultdict containing all vertices and their corresponding adjacency lists after all edges have been checked, and all edges in `edges` have been processed with respect to cycles.
    return 'NO'
    #The program returns 'NO', indicating that there is likely a condition in the graph or edges that does not permit a certain operation or that a cycle has been detected.
#Overall this is what the function does:The function accepts an integer `n` (the number of vertices), an integer `m` (the number of directed edges), and a list of `edges` representing directed edges in a graph. It checks if the directed graph contains cycles. If the graph is acyclic, it returns 'YES'. If a cycle is detected upon removing any edge from the graph, it also returns 'YES', indicating that the graph remains acyclic without that edge. If no such condition is met, it returns 'NO', indicating the presence of a cycle or a failure to meet the conditions set by the edges. The function does not handle cases where the input values for `n` and `m` are outside the specified constraints.

#State of the program right berfore the function call: graph is a dictionary where keys are integers representing vertices (from 1 to n) and values are lists of integers representing directed edges to other vertices; n is an integer representing the number of vertices (2 ≤ n ≤ 500).
def has_cycle(graph):
    in_degree = {i: (0) for i in range(1, n + 1)}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
        
    #State of the program after the  for loop has been executed: `in_degree[v]` is equal to the number of incoming edges to each vertex `v` in `graph`, `graph` is a dictionary with keys from 1 to `n`, and all values are integers representing the number of directed edges for each vertex; `u` is each vertex from 1 to `n`.
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    count = 0
    while queue:
        node = queue.popleft()
        
        count += 1
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
        
    #State of the program after the loop has been executed: `queue` is empty, `count` is equal to the total number of vertices in the graph that have been processed (i.e., those with their `in_degree` reduced to 0), `in_degree[v]` for all vertices `v` that were reachable from the initial vertices with `in_degree[v] == 0` is now 0, while those that were not reachable retain their original `in_degree` values. If `count` is equal to the number of vertices in the graph, then the graph has no cycles; otherwise, there are nodes in the graph that are part of a cycle.
    return count != n
    #The program returns True if count is not equal to n, indicating there are nodes in the graph that are part of a cycle; otherwise, it returns False, indicating the graph has no cycles.
#Overall this is what the function does:The function accepts a dictionary `graph` representing a directed graph with integer keys (vertices) and lists of integers (edges). It calculates whether there are cycles in the graph by checking if all vertices can be processed based on their incoming edges. The function returns True if there are cycles in the graph (i.e., some vertices cannot be processed), and False if there are no cycles present. This implementation assumes that the graph contains vertices numbered from 1 to n, where n is an integer between 2 and 500.

