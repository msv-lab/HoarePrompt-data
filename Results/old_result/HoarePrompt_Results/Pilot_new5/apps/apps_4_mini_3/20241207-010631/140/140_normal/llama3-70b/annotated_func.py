#State of the program right berfore the function call: node is an integer representing the current vertex, graph is a list of lists representing the directed edges of the graph, visited is a list of booleans indicating whether each vertex has been visited, and rec_stack is a list of booleans indicating whether each vertex is in the current recursion stack. The number of vertices n is between 2 and 500, and the number of edges m is between 1 and min(n(n - 1), 100000). Each vertex is represented by integers from 1 to n.
def func_1(node, graph, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if func_1(neighbor, graph, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
        
    #State of the program after the  for loop has been executed: `node` is the current vertex after exploring all its neighbors, `graph[node]` represents a list of all neighbors for `node`, `visited` indicates whether each vertex has been visited, `rec_stack` indicates whether each vertex was part of the recursion stack during the exploration. If the loop executed all possible iterations, all reachable vertices from `node` have been marked as visited. If any neighbor was found in the recursion stack, it indicates a cycle in the graph. If there were no neighbors, `graph[node]` is empty.
    rec_stack[node] = False
    return False
    #The program returns False indicating that the current vertex 'node' is not part of a cycle in the graph.
#Overall this is what the function does:The function accepts an integer `node`, a list of lists `graph` representing directed edges, and two lists of booleans `visited` and `rec_stack` to track the visitation status of vertices and the recursion stack, respectively. It performs a depth-first search to detect cycles in the directed graph. The function returns True if a cycle is detected (if a neighbor is found that is already in the recursion stack), and returns False if no cycle is present from the current vertex `node`. The function does not handle cases where the input parameters are out of expected bounds, such as an invalid `node` index or when lists are not of the correct size.

