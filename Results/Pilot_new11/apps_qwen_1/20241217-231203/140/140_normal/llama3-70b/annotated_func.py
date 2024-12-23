#State of the program right berfore the function call: node is an integer representing a vertex in the graph, graph is a dictionary where each key is a vertex and its value is a list of vertices that the key vertex points to, visited is a set of integers representing vertices that have been visited during the recursion, and rec_stack is a set of integers representing vertices in the current recursion stack.
def func_1(node, graph, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if func_1(neighbor, graph, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
        
    #State of the program after the  for loop has been executed: `node` is an integer existing as a key in the `graph` dictionary, `graph[node]` is a list (possibly empty), `visited` is a set containing all vertices that can be reached from `node` through a series of edges, `rec_stack` is a set where `rec_stack[node]` is `True`. If any `neighbor` in `graph[node]` has already been visited and is also in `rec_stack`, the function returns `True`. Otherwise, the function returns `False` if no such `neighbor` exists and the loop completes without returning.
    rec_stack[node] = False
    return False
    #`The program returns False`
#Overall this is what the function does:The function `func_1` accepts four parameters: `node`, `graph`, `visited`, and `rec_stack`. 

- `node` is an integer representing a vertex in the graph.
- `graph` is a dictionary where each key is a vertex and its value is a list of vertices that the key vertex points to.
- `visited` is a set of integers representing vertices that have been visited during the recursion.
- `rec_stack` is a set of integers representing vertices in the current recursion stack.

The function checks for cycles in the graph starting from the given `node`. It marks the `node` as visited and adds it to the recursion stack. For each neighbor of the `node`, it recursively checks if the neighbor is part of a cycle. If any neighbor is already visited and in the recursion stack, it means a cycle is detected, and the function returns `True`. If no such neighbor exists, it removes the `node` from the recursion stack and returns `False`.

The function returns `True` in multiple cases where a cycle is detected and `False` when no cycle is found after exploring all neighbors.

