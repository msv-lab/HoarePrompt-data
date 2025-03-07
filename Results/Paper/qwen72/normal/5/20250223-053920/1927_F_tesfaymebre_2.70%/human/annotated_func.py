#State of the program right berfore the function call: None of the variables are used in the function signature.
def func_1():
    return int(sys.stdin.readline().strip())
    #The program returns an integer read from the standard input, after stripping any leading or trailing whitespace.
#Overall this is what the function does:The function `func_1` reads a line from the standard input, strips any leading or trailing whitespace, converts the resulting string to an integer, and returns this integer.

#State of the program right berfore the function call: None of the variables are used in the function signature.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns the first line of input from the user, with any leading or trailing whitespace removed.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns the first line of input from the user, with any leading or trailing whitespace removed.

#State of the program right berfore the function call: No variables are passed to the function func_3.
def func_3():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns an iterator that yields integers, which are the result of converting the input string from the standard input (stdin) into a list of integers, after stripping any leading or trailing whitespace and splitting the string by spaces.
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns an iterator that yields integers. These integers are derived from a space-separated string input from the standard input (stdin), after stripping any leading or trailing whitespace and splitting the string by spaces. The function does not modify any external state or variables.

#State of the program right berfore the function call: None of the variables are passed as arguments to the function `func_4`. The function reads input from standard input, expecting a line of space-separated integers.
def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers, which are the space-separated integers read from the standard input.
#Overall this is what the function does:The function `func_4` reads a line of space-separated integers from the standard input and returns a list of these integers. The function does not modify any external variables or state; it only processes the input and returns the resulting list.

#State of the program right berfore the function call: None, as the function does not take any parameters.
def func_5():
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings, where each string is a word or value input by the user from the standard input (stdin) before pressing Enter. The input is stripped of leading and trailing whitespace and then split into separate strings based on spaces.
#Overall this is what the function does:The function `func_5` does not accept any parameters. It reads a line of input from the standard input (stdin), removes any leading and trailing whitespace, splits the input into separate strings based on spaces, and returns a list of these strings. If no input is provided or the input is only whitespace, an empty list is returned.

#State of the program right berfore the function call: The function `func_6` does not take any parameters, but it relies on the `func_3` function to provide the necessary inputs. `func_3` is expected to return a tuple of two integers (n, m) where n is the number of vertices and m is the number of edges in the graph, and for each of the m edges, a tuple (u, v, w) where u and v are the vertices connected by an edge and w is the weight of that edge. The graph is represented using an adjacency list `graph` and a list of edges `edges`. The graph is undirected, and the edges are sorted in non-increasing order of their weights. The `DSU` class is used to manage the union-find data structure, and `colors` is a list used to track the color of nodes during a depth-first search (DFS).
def func_6():
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: The `graph` is now a defaultdict of type `list` containing the adjacency lists for each vertex, where each vertex `u` and `v` in the edges has been added to each other's adjacency list. The `edges` list is now populated with `m` tuples, each representing an edge in the format `(weight, u, v)`. The `DSU` class and the `colors` list remain unchanged.
    edges.sort(reverse=True)
    dsu = DSU(n + 1)
    _min_edge = float('inf')
    node_u = -1
    node_v = -1
    for (w, u, v) in edges:
        parent_u = dsu.find(u)
        
        parent_v = dsu.find(v)
        
        if parent_u == parent_v:
            dsu.union(u, v, w)
            if dsu.min_edge[parent_u] < _min_edge:
                _min_edge = dsu.min_edge[parent_u]
                node_u = u
                node_v = v
        else:
            dsu.union(u, v, w)
        
    #State: The `graph` remains a defaultdict of type `list` containing the adjacency lists for each vertex. The `edges` list is still sorted in descending order based on the weight of the edges. The `DSU` class and the `colors` list remain unchanged. The `dsu` instance has updated its parent and rank information to reflect the union operations performed. The `_min_edge` variable is set to the minimum edge weight that was successfully unioned. The `node_u` and `node_v` variables are set to the vertices that were part of the edge with the minimum weight that was successfully unioned.
    colors = [0] * (n + 1)
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    #This is printed: _min_edge, len(res) (where _min_edge is the minimum edge weight that was successfully unioned, and len(res) is the number of vertices visited during the DFS traversal starting from node_u)
    print(*res)
    #This is printed: [elements of res separated by spaces] (where res is the result of the dfs function called with node_u, -1, and an empty list)
#Overall this is what the function does:The function `func_6` does not accept any parameters. It retrieves the number of vertices and edges in an undirected graph from the `func_3` function. It then constructs an adjacency list representation of the graph and a list of edges, each with a weight, and sorts the edges in non-increasing order of their weights. Using a union-find data structure (`DSU`), it processes the edges to find the minimum weight edge that successfully connects two previously unconnected components. The function performs a depth-first search (DFS) starting from one of the vertices of this minimum weight edge and prints the minimum edge weight and the number of vertices visited during the DFS. It also prints the list of vertices visited during the DFS traversal. The final state of the program includes an updated union-find data structure, a sorted list of edges, and the printed results.

#State of the program right berfore the function call: curr is an integer representing the current vertex in the graph, parent is an integer representing the parent vertex of curr in the DFS traversal, and path is a list of integers representing the current path in the DFS traversal.
def dfs(curr, parent, path):
    if (colors[curr] == 1) :
        return path
        #The program returns the list of integers representing the current path in the DFS traversal.
    #State: `curr` is an integer representing the current vertex in the graph, `parent` is an integer representing the parent vertex of `curr` in the DFS traversal, and `path` is a list of integers representing the current path in the DFS traversal. Additionally, `colors[curr]` is not equal to 1.
    colors[curr] = 1
    path.append(curr)
    for nei in graph[curr]:
        if colors[nei] != 2 and nei != parent:
            res = dfs(nei, curr, path)
            set_res = set(res)
            if res and node_v in set_res:
                return res
        
    #State: The loop has iterated through all neighbors of `curr` in the graph. If a neighbor `nei` of `curr` has not been fully processed (`colors[nei] != 2`) and is not the parent of `curr`, the `dfs` function is called with `nei` as the new current vertex, `curr` as the new parent, and the current path `path`. If the result of the `dfs` call contains `node_v`, the loop returns this result immediately. If no such neighbor is found or none of the `dfs` calls return a path containing `node_v`, the loop completes without returning. The values of `curr`, `parent`, `path`, and `colors[curr]` remain unchanged.
    colors[curr] = 2
    return []
    #The program returns an empty list.
#Overall this is what the function does:The function `dfs` performs a depth-first search in a graph. It accepts three parameters: `curr` (the current vertex in the graph), `parent` (the parent vertex of `curr` in the DFS traversal), and `path` (a list of integers representing the current path in the DFS traversal). The function marks the current vertex as being processed and appends it to the path. It recursively explores all unprocessed neighbors of the current vertex that are not the parent. If a neighbor's DFS traversal returns a path containing a specific node `node_v`, the function returns this path. If no such path is found, the function marks the current vertex as fully processed and returns an empty list.

#State of the program right berfore the function call: No variables are passed to the function `func_7`.
def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` is assigned the value returned by `func_1()`. No other variables are affected.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It retrieves the number of test cases from the function `func_1` and then calls the function `func_6` that many times. After the function concludes, the variable `test_cases` holds the value returned by `func_1`, and no other variables are affected. The function does not return any value, so it may return `None` by default.

