#State of the program right berfore the function call: node is an integer representing the current vertex, graph is a list of tuples representing directed edges, visited is a list of boolean values indicating whether each vertex has been visited, and rec_stack is a list of boolean values indicating the vertices currently in the recursion stack.
def func_1(node, graph, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if func_1(neighbor, graph, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
        
    #State of the program after the  for loop has been executed: `node` is an integer, `graph` is a list of tuples representing directed edges, `visited[node]` is True, `rec_stack[node]` is True, `visited[neighbor]` is True for all neighbors processed, `rec_stack[neighbor]` is True for any neighbor that is part of a cycle, if no cycles are found `rec_stack[neighbor]` is False for those neighbors.
    rec_stack[node] = False
    return False
    #The program returns False, indicating that there is no cycle detected in the graph for the given node
#Overall this is what the function does:The function accepts an integer `node`, a list of tuples `graph` representing directed edges, a list of boolean values `visited` to track visited vertices, and a list of boolean values `rec_stack` to track vertices in the recursion stack. It performs a depth-first search to detect cycles in the directed graph. The function returns True if a cycle is found or if the node is currently being explored, and returns False if the node has been fully processed without detecting cycles.

