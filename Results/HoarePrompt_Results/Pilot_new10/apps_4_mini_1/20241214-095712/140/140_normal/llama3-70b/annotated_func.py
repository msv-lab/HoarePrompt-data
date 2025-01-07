#State of the program right berfore the function call: node is an integer representing the current node in the graph, graph is a list of tuples where each tuple (u, v) represents a directed edge from vertex u to vertex v, visited is a set of integers representing the visited nodes, and rec_stack is a set of integers representing the nodes currently in the recursion stack.
def func_1(node, graph, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if func_1(neighbor, graph, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
        
    #State of the program after the  for loop has been executed: `node` is an integer representing the current node, `visited` is a set of integers representing all nodes that have been visited during the traversal, `rec_stack` is a set of integers representing the nodes that are currently in the recursion stack. The `graph` structure indicates if any cycles were detected. If no cycles were detected, the function returns False; if a cycle was detected at any point, it returns True.
    rec_stack[node] = False
    return False
    #The program returns False
#Overall this is what the function does:The function accepts an integer `node`, a list of tuples `graph` representing directed edges, a set `visited` to track visited nodes, and a set `rec_stack` to monitor nodes currently in the recursion stack. It returns True if a cycle is detected in the directed graph; otherwise, it returns False. The function performs a depth-first search to explore the graph and checks for cycles by determining if a node is revisited while still in the recursion stack.

