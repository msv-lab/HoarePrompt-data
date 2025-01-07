#State of the program right berfore the function call: node is an integer representing a vertex in the graph, graph is an adjacency list or matrix representing a directed graph with n vertices, visited and rec_stack are lists or sets of integers representing the visited vertices and the current recursion stack, respectively.
def func_1(node, graph, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if func_1(neighbor, graph, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
        
    #State of the program after the  for loop has been executed: `node` is a valid vertex in the graph, `graph` remains unchanged, `visited` reflects the visitation state of all neighbors of `node` after traversal, and `rec_stack` represents the recursion stack state after visiting all neighbors of `node`. If the graph contains a cycle reachable from `node`, the program returns True; otherwise, the return value depends on the implementation of `func_1`. If `graph[node]` is empty, the loop does not execute, and the initial state of `visited` and `rec_stack` is preserved.
    rec_stack[node] = False
    return False
    #The program returns False
#Overall this is what the function does:The function `func_1` checks for the presence of a cycle in a directed graph starting from a given vertex `node`. It accepts four parameters: `node` (the current vertex), `graph` (the adjacency list or matrix representation of the graph), `visited` (a list or set of visited vertices), and `rec_stack` (a list or set representing the current recursion stack). The function returns `True` if a cycle is detected and `False` otherwise. After execution, the `visited` list reflects the visitation state of all vertices reachable from `node`, and the `rec_stack` represents the recursion stack state after visiting all these vertices. The function handles various cases, including when the graph contains a cycle reachable from `node`, when `node` has unvisited neighbors, and when `node` has no neighbors. The function's return value indicates whether a cycle is detected, and its side effects update the `visited` and `rec_stack` data structures to reflect the traversal state. Edge cases, such as an empty graph or a node with no neighbors, are implicitly handled by the function's recursive structure and the base case `return False` statement.

