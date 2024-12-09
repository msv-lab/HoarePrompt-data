#State of the program right berfore the function call: node is an integer representing a vertex in the directed graph, graph is a list of lists where each list contains the vertices connected by directed edges, visited is a list of boolean values indicating whether each vertex has been visited, and rec_stack is a list of boolean values indicating whether each vertex is in the current recursion stack.
def func_1(node, graph, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if func_1(neighbor, graph, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
        
    #State of the program after the  for loop has been executed: `node` is an integer, `graph` has been fully traversed, `visited` indicates all nodes reachable from the original `node`, `rec_stack` reflects whether a cycle was detected along any path from the original `node`. If all reachable nodes were visited without detecting a cycle, then `rec_stack` for those nodes will be False. If at least one cycle was detected during the traversal, then `rec_stack` for at least one of those nodes will be True.
    rec_stack[node] = False
    return False
    #The program returns False
#Overall this is what the function does:The function accepts an integer `node`, a list of lists `graph`, a list of boolean values `visited`, and a list of boolean values `rec_stack`. It performs a depth-first search to detect cycles in a directed graph. The function returns `True` if a cycle is detected (i.e., if a node is revisited while still in the recursion stack) or if there are unvisited neighbors. It returns `False` if all reachable nodes from `node` have been visited without detecting a cycle. Additionally, the function does not handle the case where the input `node` is out of bounds for the `graph`, which could lead to indexing errors.

