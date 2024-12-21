#State of the program right berfore the function call: n is a non-negative integer representing the number of vertices, m is a non-negative integer representing the number of edges, and edges is a list of pairs of integers (u, v) such that 1 <= u, v <= n, u!= v, representing the directed edges in the graph.
def func_1(n, m, edges):
    graph = defaultdict(list)
    for (u, v) in edges:
        graph[u].append(v)
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `m` is a non-negative integer, `edges` is a list of pairs of integers, and `graph` is a dictionary where each key is a vertex `u` and its corresponding value is a list of neighboring vertices `v` such that `(u, v)` is an edge in `edges`, or `graph` is an empty dictionary if `edges` is empty.
    if (not has_cycle(graph)) :
        return 'YES'
        #The program returns 'YES'
    #State of the program after the if block has been executed: `n` is a non-negative integer, `m` is a non-negative integer, `edges` is a list of pairs of integers, and `graph` is a dictionary where each key is a vertex `u` and its corresponding value is a list of neighboring vertices `v` such that `(u, v)` is an edge in `edges`, or `graph` is an empty dictionary if `edges` is empty. The graph contains at least one cycle.
    for (u, v) in edges:
        graph[u].remove(v)
        
        if not has_cycle(graph):
            return 'YES'
        
        graph[u].append(v)
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `m` is a non-negative integer, `edges` is a list of pairs of integers, and `graph` is a dictionary representing a graph with its original structure unless the function returned `'YES'` early, indicating a modification was found that would remove the cycle, but this return does not change the values of `n`, `m`, or `edges`, only the program's flow.
    return 'NO'
    #The program returns string 'NO'
#Overall this is what the function does:The function determines whether a directed graph, represented by the number of vertices `n`, the number of edges `m`, and a list of edges, contains a cycle that can be removed by deleting a single edge. It accepts three parameters: `n` (the number of vertices), `m` (the number of edges), and `edges` (a list of pairs of integers representing the directed edges in the graph). The function returns either `'YES'` if such an edge exists whose removal would result in a cycle-free graph or `'NO'` if no such edge exists. The function's state after execution includes the original graph structure unless the function returned `'YES'` early, indicating a modification was found that would remove the cycle. The function covers potential edge cases such as an empty graph (when `edges` is empty), graphs with multiple cycles, and graphs where removing any edge would not affect the presence of cycles.

#State of the program right berfore the function call: graph is a dictionary representing a directed graph where each key is a node (an integer from 1 to n) and each value is a list of its neighboring nodes, and n is a non-negative integer such that it is the number of vertices in the graph.
def has_cycle(graph):
    in_degree = {i: (0) for i in range(1, n + 1)}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
        
    #State of the program after the  for loop has been executed: `graph` is a dictionary representing a directed graph, `n` is a non-negative integer, and `in_degree` is a dictionary where each key `v` has a value equal to the number of edges in `graph` that point to `v`.
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    count = 0
    while queue:
        node = queue.popleft()
        
        count += 1
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
        
    #State of the program after the loop has been executed: `queue` is empty, `count` equals the total number of nodes processed from the initial `queue`, and `in_degree` values are updated to reflect the graph processing, with `node` being the last processed node from `queue` if the loop executed at least once, otherwise `node` and `count` retain their initial values and `in_degree` remains unchanged if the loop did not execute.
    return count != n
    #The program returns a boolean value indicating whether the total number of nodes processed (0) is not equal to the total number of nodes in the graph (n)
#Overall this is what the function does:The function `has_cycle` accepts a dictionary `graph` representing a directed graph and an implicit integer `n` representing the number of vertices in the graph, and returns a boolean value indicating whether the graph has a cycle. The function calculates the in-degree of each node, initializes a queue with nodes having an in-degree of 0, and then performs a breadth-first traversal of the graph. If all nodes are processed during the traversal (i.e., the count of processed nodes equals the total number of nodes `n`), the function returns `False`, indicating that the graph does not have a cycle. Otherwise, it returns `True`, indicating the presence of a cycle. The function handles graphs with any number of nodes and edges, including the edge case where the graph is empty (i.e., `n` equals 0). However, the function assumes that the input graph is well-formed, i.e., it does not contain any nodes with values outside the range from 1 to `n`, and it does not account for potential errors that may occur if the graph is not well-formed or if the input `n` does not match the actual number of nodes in the graph.

