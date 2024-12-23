#State of the program right berfore the function call: node is an integer representing the current vertex, graph is a list of tuples representing the directed edges, visited is a set of integers containing the visited vertices, and rec_stack is a set of integers used to track the recursion stack of vertices.
def func_1(node, graph, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if func_1(neighbor, graph, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
        
    #State of the program after the  for loop has been executed: `node` is an integer representing a valid index for `graph`, `visited` is a set of integers including all neighbors of `node` that were visited during the loop, `rec_stack` records whether any neighbors of `node` are currently in the recursion stack, and the loop concludes with no unvisited neighbors left in the graph for `node` or a cycle has been detected.
    rec_stack[node] = False
    return False
    #The program returns False, indicating that node has not been identified as part of a cycle in the graph since rec_stack[node] is False.
#Overall this is what the function does:The function `func_1` is designed to perform a depth-first search on a directed graph to detect cycles. It takes four parameters: `node` (an integer representing the current vertex being visited), `graph` (a list of tuples representing directed edges between nodes), `visited` (a set of integers that tracks which nodes have been visited), and `rec_stack` (a set of integers that tracks the nodes currently in the recursion stack). The function returns a boolean value: it returns `True` if a cycle is detected during the traversal or if an unvisited neighbor exists that can be explored; otherwise, it returns `False` if all neighbors have been visited without finding a cycle.

The postconditions indicate that if `True` is returned, it may signify the presence of unvisited neighbors or a cycle in the graph; if `False` is returned, it indicates that the node is not part of any cycle. However, the annotations may not fully capture that the function should return `True` upon detecting cycles and not solely for traversal states. The code does not explicitly check for valid indices in the `graph` input, which could lead to errors if an invalid node is passed or if the graph contains unexpected structures. This could potentially lead to an unhandled index error if the node index exceeds the bounds of the graph representation. Overall, this function efficiently explores the directed graph for cycles, affecting the `visited` and `rec_stack` sets to ensure proper tracking of the search state.

