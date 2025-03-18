#State of the program right berfore the function call: No variables in the function signature.
def func_1():
    return int(sys.stdin.readline().strip())
    #The program returns an integer that is read from the standard input.
#Overall this is what the function does:The function `func_1` reads a line from the standard input, strips any leading or trailing whitespace, converts it to an integer, and returns this integer.

#State of the program right berfore the function call: No variables in the function signature. The function `func_2` reads a line from the standard input and returns it as a stripped string.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns a stripped string read from the standard input.
#Overall this is what the function does:The function `func_2` reads a line from the standard input, removes any leading and trailing whitespace from the line, and returns the resulting string.

#State of the program right berfore the function call: No variables are present in the function signature of `func_3`. This function is expected to read a line from standard input, strip any leading or trailing whitespace, split the line into components based on whitespace, convert each component to an integer, and return the resulting integers as a map object.
def func_3():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object containing integers that were read from a line of standard input, stripped of leading and trailing whitespace, and split by whitespace.
#Overall this is what the function does:The function `func_3` reads a line from standard input, removes any leading or trailing whitespace, splits the line into components based on whitespace, converts each component to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: No variables are present in the function signature of `func_4`. Therefore, no precondition can be derived from the function signature alone.
def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers obtained by reading a line from standard input, stripping any leading or trailing whitespace, splitting the line into substrings based on whitespace, and converting each substring to an integer.
#Overall this is what the function does:The function `func_4` reads a line from standard input, removes any leading or trailing whitespace, splits the line into substrings based on whitespace, converts each substring to an integer, and returns a list of these integers.

#State of the program right berfore the function call: No variables are used in the function signature of `func_5`.
def func_5():
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings, where each string is a word from the line read from standard input, with leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_5` reads a line from standard input, removes any leading and trailing whitespace, splits the line into words, and returns a list of these words.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the graph, and m is an integer representing the number of edges in the graph such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5).
def func_6():
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: `graph` is a defaultdict with a default factory of `list` where each `u` and `v` pair (returned by `func_3()`) have their respective connections recorded `m` times, and `edges` is a list of `m` tuples, each representing an edge with its weight and the nodes it connects.
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
        
    #State: `graph` is a defaultdict with a default factory of `list` where each `u` and `v` pair (returned by `func_3()`) have their respective connections recorded `m` times; `edges` is an empty list, as all edges have been processed; `dsu` is a DSU object with an internal state reflecting the union of all sets containing the nodes, indicating a single connected component; `_min_edge` is the minimum edge weight found in the graph; `node_u` and `node_v` are the nodes corresponding to `_min_edge`.
    colors = [0] * (n + 1)
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    #This is printed: _min_edge, len(res) (where _min_edge is the minimum edge weight in the graph and len(res) is the number of nodes in the list `res`)
    print(*res)
    #This is printed: node_u, node_v, ... (where node_u is the starting node and the sequence includes all nodes in the graph)
#Overall this is what the function does:The function constructs a graph with `n` vertices and `m` edges, then identifies the minimum edge weight in a spanning tree and performs a depth-first search starting from the node associated with this minimum edge. It prints the minimum edge weight and the number of nodes in the resulting path, followed by the sequence of nodes in the path.

#State of the program right berfore the function call: curr is an integer representing the current vertex, parent is an integer representing the parent vertex to avoid revisiting, and path is a list of integers representing the current path in the DFS traversal.
def dfs(curr, parent, path):
    if (colors[curr] == 1) :
        return path
        #The program returns the list 'path' which represents the current path in the DFS traversal.
    #State: `curr` is an integer representing the current vertex, `parent` is an integer representing the parent vertex to avoid revisiting, and `path` is a list of integers representing the current path in the DFS traversal. Additionally, `colors[curr]` is not equal to 1.
    colors[curr] = 1
    path.append(curr)
    for nei in graph[curr]:
        if colors[nei] != 2 and nei != parent:
            res = dfs(nei, curr, path)
            set_res = set(res)
            if res and node_v in set_res:
                return res
        
    #State: The loop completes all iterations without returning a path, implying that `node_v` is not reachable from `curr`.
    colors[curr] = 2
    return []
    #The program returns an empty list
#Overall this is what the function does:The function `dfs` performs a depth-first search starting from the current vertex `curr`. It avoids revisiting the `parent` vertex and tracks the current path in `path`. The function returns the path if it reaches a vertex with a specific color, or if it finds a path containing `node_v` through recursive calls. If no such path is found, it returns an empty list.

#State of the program right berfore the function call: No variables in the function signature. This function does not take any input parameters and does not return any values directly. It likely orchestrates the reading of test cases and the execution of the main logic through other functions.
def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` retains its initial value, and `func_6()` has been called `test_cases` number of times.
#Overall this is what the function does:The function `func_7` does not accept any input parameters and does not return any values directly. It reads the number of test cases and executes the logic defined in `func_6` for each test case.

