#State of the program right berfore the function call: node is an integer representing a vertex in the graph, graph is a dictionary where each key is a vertex and its value is a list of vertices that the key vertex has directed edges to, visited and rec_stack are lists used to keep track of visited nodes and the recursion stack during depth-first search, respectively.
def func_1(node, graph, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if func_1(neighbor, graph, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
        
    #State of the program after the  for loop has been executed: `node` is an integer representing a vertex in the graph, `graph` is a dictionary where each key is a vertex and its value is a list of vertices that the key vertex has directed edges to, `visited` and `rec_stack` are lists used to keep track of visited nodes and the recursion stack during depth-first search, respectively, `visited[node]` is True, `rec_stack[node]` is True, `graph[node]` is empty or all neighbors have been processed. If `func_1(neighbor, graph, visited, rec_stack)` returns True for any neighbor, the function returns True. If `rec_stack[neighbor]` is True for any neighbor, the function returns True. Otherwise, the function returns None.
    rec_stack[node] = False
    return False
    #The program returns False
#Overall this is what the function does:The function `func_1` accepts an integer `node`, a dictionary `graph`, and two lists `visited` and `rec_stack`. It performs a depth-first search to detect cycles in the graph. If a cycle is detected, the function returns True; otherwise, it returns False.

