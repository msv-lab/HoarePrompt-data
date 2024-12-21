#State of the program right berfore the function call: node is an integer representing the current vertex, graph is a list of lists where each sublist represents the directed edges from the corresponding vertex (1 ≤ node ≤ n), visited is a list of boolean values indicating whether each vertex has been visited, and rec_stack is a list of boolean values indicating the recursion stack state for each vertex.
def func_1(node, graph, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if func_1(neighbor, graph, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
        
    #State of the program after the  for loop has been executed: `visited[node]` is True, `rec_stack[node]` is True, all neighbors of `node` have been evaluated. If a neighbor has not been visited, `func_1(neighbor, graph, visited, rec_stack)` has been called for that neighbor. If a neighbor has been visited, for each visited neighbor, `rec_stack[neighbor]` whether True or False reflects their inclusion in the recursion stack at some point during the exploration. Additionally, if any neighbor has led to a cycle, the function would have returned True.
    rec_stack[node] = False
    return False
    #The program returns False, indicating that there are no cycles detected in the graph for the current node since all neighbors have been evaluated and did not lead to a cycle.
#Overall this is what the function does:The function `func_1` is designed to detect cycles in a directed graph represented as a list of adjacency lists. It accepts four parameters: `node`, an integer representing the current vertex to explore; `graph`, a list of lists where each sublist contains directed edges from the corresponding vertex; `visited`, a list of boolean values indicating which vertices have been traversed; and `rec_stack`, a list of boolean values representing the vertices currently in the recursion stack. Upon execution, the function marks the current node as visited and adds it to the recursion stack. It then recursively examines each unvisited neighbor of the current node. If a visited neighbor is found which is also in the recursion stack, a cycle is detected, and the function returns `True`. If all neighbors are explored without finding a cycle, the function marks the current node as not in the recursion stack and returns `False`. The overall functionality thus checks for cycles in the directed graph, providing a boolean output indicating the presence or absence of cycles. Additionally, the function does not handle edge cases where the input `node` may be out of bounds, which could lead to index errors. Therefore, handling for such edge cases is a missing element in the current implementation.

