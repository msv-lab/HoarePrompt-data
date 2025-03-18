#State of the program right berfore the function call: n is an integer representing the number of vertices, m is an integer representing the number of edges, and edges is a list of tuples, where each tuple (u, v) represents a directed edge from vertex u to vertex v, and 1 <= u, v <= n, u!= v.
def func_1(n, m, edges):
    graph = defaultdict(list)
    for (u, v) in edges:
        graph[u].append(v)
        
    #State of the program after the  for loop has been executed: `n` is an integer representing the number of vertices, `m` is an integer representing the number of edges, `edges` is a list of tuples, `u` is the source vertex of the last edge, `v` is the destination vertex of the last edge, and `graph` is a defaultdict of lists where each key is a source vertex and its corresponding value is a list of destination vertices that are directly reachable from it.
    if (not has_cycle(graph)) :
        return 'YES'
        #The program returns the string 'YES'
    #State of the program after the if block has been executed: `n` is an integer representing the number of vertices, `m` is an integer representing the number of edges, `edges` is a list of tuples, `u` is the source vertex of the last edge, `v` is the destination vertex of the last edge, and `graph` is a defaultdict of lists where each key is a source vertex and its corresponding value is a list of destination vertices that are directly reachable from it. The graph contains at least one cycle.
    for (u, v) in edges:
        graph[u].remove(v)
        
        if not has_cycle(graph):
            return 'YES'
        
        graph[u].append(v)
        
    #State of the program after the  for loop has been executed: To determine the output state after all iterations of the loop have finished, let's analyze the loop step by step.
    #
    #1. **Loop Iteration**: For each edge `(u, v)` in the `edges` list, the loop removes `v` from the list of destination vertices of `u` in the graph, checks if the graph still has a cycle, and then appends `v` back to the list of destination vertices of `u` in the graph.
    #
    #2. **Effect of Iterations**:
    #   - `n` and `m`: These represent the number of vertices and edges, respectively. They do not change within the loop.
    #   - `edges`: This list of edges is iterated over but not modified in terms of its length or content. Each edge is processed once.
    #   - `u` and `v`: These variables take on the values of the source and destination vertices of each edge as the loop iterates over the `edges` list.
    #   - `graph`: The graph structure is temporarily modified (by removing and then adding back an edge) during each iteration, but at the end of each iteration, it returns to its original state (before the loop started) because `v` is appended back to `graph[u]`.
    #   - `has_cycle(graph)`: This function checks if the graph contains a cycle. The loop's behavior depends on this check, but since it's not the focus of determining the output state's variable values, we acknowledge its role in controlling the loop's flow but focus on variable states.
    #
    #3. **After All Iterations**:
    #   - `n` remains an integer representing the number of vertices.
    #   - `m` remains an integer representing the number of edges.
    #   - `edges` remains a list of tuples representing all edges.
    #   - `u` and `v` will hold the values of the source and destination vertices of the last edge processed.
    #   - `graph` returns to its original state after all iterations because each edge removed is added back.
    #
    #Considering the loop's behavior:
    #- If the graph does not contain a cycle after removing any edge, the function returns 'YES' and the loop does not continue.
    #- However, the question asks for the state after all iterations, implying we consider the scenario where the loop completes normally (without returning early) or when the conditions are such that it does not early return.
    #
    #**Output State**: **`n` is an integer representing the number of vertices, `m` is an integer representing the number of edges, `edges` is a list of tuples, `u` is the source vertex of the last edge, `v` is the destination vertex of the last edge, and `graph` is a defaultdict of lists representing the original graph structure with all edges intact, assuming no early return due to the absence of a cycle. If the graph originally contained at least one cycle, this characteristic is maintained unless an early return occurred.**
    return 'NO'
    #The program returns the string 'NO', indicating the presence of a cycle in the graph after all iterations have completed, with `n` being an integer representing the number of vertices, `m` being an integer representing the number of edges, `edges` being a list of tuples representing all edges, `u` being the source vertex of the last edge, `v` being the destination vertex of the last edge, and `graph` being a defaultdict of lists representing the original graph structure with all edges intact.
#Overall this is what the function does:The function accepts parameters `n` (number of vertices), `m` (number of edges), and `edges` (list of directed edges), and returns 'YES' if the graph is cycle-free or if removing any single edge makes it cycle-free; otherwise, it returns 'NO', indicating the presence of a cycle that cannot be removed by deleting a single edge.

#State of the program right berfore the function call: graph is a dictionary representing a directed graph where each key is a node (integer), the value for each key is a list of its neighboring nodes (integers), and n is a positive integer representing the number of nodes in the graph such that 1 <= n <= 500.
def has_cycle(graph):
    in_degree = {i: (0) for i in range(1, n + 1)}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
        
    #State of the program after the  for loop has been executed: `graph` is a dictionary representing a directed graph, `n` is a positive integer, `in_degree` is a dictionary where each key is a node from 1 to `n` and the value represents the total in-degree of the node in the graph.
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    count = 0
    while queue:
        node = queue.popleft()
        
        count += 1
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
        
    #State of the program after the loop has been executed: `graph` remains the same, `n` is a positive integer, `queue` is empty, `in_degree` values are updated based on the graph structure, and `count` is the number of nodes processed, which is the number of nodes in the graph that are reachable from nodes with an in-degree of 0
    return count != n
    #The program returns True if there are nodes in the graph not reachable from nodes with an in-degree of 0, and False otherwise.
#Overall this is what the function does:The function accepts a dictionary representing a directed graph and the number of nodes, and returns True if there are nodes in the graph not reachable from nodes with an in-degree of 0, indicating a potential cycle, and False otherwise, suggesting the graph is a Directed Acyclic Graph (DAG).

