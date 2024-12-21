#State of the program right berfore the function call: node is a non-negative integer, graph is a list of lists or dictionary representing a directed graph with n vertices and m edges, visited and rec_stack are lists or sets of non-negative integers used to track visited vertices and vertices in the recursion stack.
def func_1(node, graph, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if func_1(neighbor, graph, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
        
    #State of the program after the  for loop has been executed: `node` is a non-negative integer, `graph` is a list of lists or dictionary representing a directed graph, `visited` reflects the nodes visited during the traversal attempt from `node`, and `rec_stack` indicates nodes in the recursion stack, with the program's return value or further actions dependent on the loop's findings regarding cycles or traversal outcomes.
    rec_stack[node] = False
    return False
    #The program returns False
#Overall this is what the function does:The function performs a depth-first search (DFS) traversal on a directed graph, starting from a given node, to detect the presence of a cycle. It accepts four parameters: a non-negative integer node, a directed graph represented as a list of lists or dictionary, and two lists or sets (visited and rec_stack) used to track visited vertices and vertices in the recursion stack, respectively. The function returns a boolean value indicating whether a cycle is detected (True) or not (False). Upon completion, the function will have updated the visited and rec_stack data structures to reflect the nodes visited and the recursion stack state during the traversal attempt from the given node. The function handles cases where a node has unvisited neighbors, visited neighbors that are in the recursion stack (indicating a cycle), and nodes that have been fully traversed without finding a cycle. It will return True as soon as a cycle is detected and False otherwise, covering all potential edge cases such as empty graphs, single-node graphs, and graphs with multiple connected components.

