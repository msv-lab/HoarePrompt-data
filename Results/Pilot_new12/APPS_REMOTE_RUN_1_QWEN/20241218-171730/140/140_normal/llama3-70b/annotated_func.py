#State of the program right berfore the function call: node is an integer representing a vertex in the graph, graph is a dictionary where each key is a vertex and its value is a list of vertices that have a directed edge coming out from the key vertex, visited and rec_stack are lists used to keep track of visited nodes and the recursion stack respectively, both initialized as empty lists.
def func_1(node, graph, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if func_1(neighbor, graph, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
        
    #State of the program after the  for loop has been executed: `node` is an integer representing a vertex in the graph, `visited[node]` is `True`, `rec_stack[node]` is `True`. If the loop executes at least once, for at least one neighbor `neighbor` of `node`, either `visited[neighbor]` was updated to `True` and `func_1(neighbor, graph, visited, rec_stack)` returned `True`, or `rec_stack[neighbor]` was `True`. If the loop does not execute, `visited[neighbor]` remains unchanged for all neighbors of `node`.
    rec_stack[node] = False
    return False
    #The program returns False
#Overall this is what the function does:The function `func_1` takes a `node`, a `graph` represented as a dictionary, and two lists `visited` and `rec_stack` as inputs. It performs a depth-first search (DFS) to detect cycles in the graph. If a cycle is detected during the DFS traversal starting from the given `node`, the function returns `True`; otherwise, it returns `False`. The function uses the `visited` list to keep track of visited nodes and the `rec_stack` list to detect cycles. If a node is encountered that is already in the recursion stack (`rec_stack`), a cycle is detected, and the function returns `True`. If no cycle is detected and the DFS completes, the function returns `False`. This function can handle graphs with cycles and acyclic graphs.

