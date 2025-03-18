#State of the program right berfore the function call: node is an integer representing a vertex in the graph, graph is a dictionary or list representing the adjacency list of the directed graph, visited is a list or dictionary of boolean values representing whether each vertex has been visited, and rec_stack is a list or dictionary of boolean values representing whether each vertex is in the recursion stack.
def func_1(node, graph, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if func_1(neighbor, graph, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
        
    #State of the program after the  for loop has been executed: `node` remains an integer representing a vertex in the graph, `graph` is unchanged as a dictionary or list representing the adjacency list of the directed graph, `visited` and `rec_stack` have been updated based on the neighbors of `node` that were visited and potentially added to the recursion stack during the loop's execution, and `neighbor` would be the last neighbor of `node` in the graph that was processed.
    rec_stack[node] = False
    return False
    #The program returns False
#Overall this is what the function does:The function accepts a node and a directed graph, performs a depth-first search to detect cycles, and returns True if a cycle is found, False otherwise, assuming the input graph is valid and the node exists in the graph.

