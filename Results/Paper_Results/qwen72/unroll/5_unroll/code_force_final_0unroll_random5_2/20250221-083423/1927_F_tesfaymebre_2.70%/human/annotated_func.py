#State of the program right berfore the function call: None
def func_1():
    return int(sys.stdin.readline().strip())
    #The program returns an integer value read from the standard input (stdin).
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an integer value read from the standard input (stdin). The state of the program after the function concludes is that an integer value has been read from the standard input and is returned.

#State of the program right berfore the function call: None
def func_2():
    return sys.stdin.readline().strip()
    #The program returns the first line of input from the user, with any trailing whitespace removed.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns the first line of input from the user, with any trailing whitespace removed.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_3():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns an iterator that converts each element of the input line (after stripping any leading or trailing whitespace and splitting by spaces) into an integer.
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns an iterator that converts each element of a single line of input from `sys.stdin`, after stripping leading and trailing whitespace and splitting by spaces, into an integer.

#State of the program right berfore the function call: No variables are passed to the function func_4. The function reads input from stdin, expecting a line of space-separated integers.
def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers read from a line of space-separated integers provided as input.
#Overall this is what the function does:The function `func_4` reads a line of space-separated integers from the standard input and returns them as a list of integers. No variables are passed to the function. After the function concludes, the program has a list of integers that were provided as input.

#State of the program right berfore the function call: None. This function does not take any parameters and is used to read input from stdin.
def func_5():
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings, where each string is a word or number from the line of input read from stdin, with leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_5` does not accept any parameters. It reads a line of input from stdin, removes leading and trailing whitespace, and splits the line into a list of strings based on whitespace. The function returns this list of strings.

#State of the program right berfore the function call: n and m are non-negative integers such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5), and edges is a list of tuples (w, u, v) where 1 <= u, v <= n, u != v, and 1 <= w <= 10^6.
def func_6():
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: `n` and `m` remain unchanged, `edges` is a list of `m` tuples where each tuple is of the form `(w, u, v)` as returned by `func_3()`, and `graph` is a defaultdict of type list where each key `u` has a list of values `v` that were appended during the loop iterations.
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
        
    #State: `n` and `m` remain unchanged, `edges` is a sorted list of `m` tuples in descending order where each tuple is of the form `(w, u, v)` as returned by `func_3()`, `graph` is a defaultdict of type list where each key `u` has a list of values `v` that were appended during the loop iterations, `dsu` is an instance of the `DSU` class initialized with `n + 1` and modified by the union operations, `_min_edge` is the minimum weight of the edges that were successfully unioned, `node_u` is the node involved in the union operation that resulted in the minimum edge weight, `node_v` is the other node involved in the same union operation.
    colors = [0] * (n + 1)
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    #This is printed: _min_edge, len(res) (where _min_edge is the minimum weight of the edges that were successfully unioned, and len(res) is the length of the path found by the DFS starting from node_u)
    print(*res)
    #This is printed: [nodes visited during the DFS starting from node_u] (where node_u is the node involved in the union operation that resulted in the minimum edge weight)
#Overall this is what the function does:The function `func_6` constructs a graph from a list of weighted edges, sorts these edges in descending order by weight, and then uses a Disjoint Set Union (DSU) data structure to process these edges. It finds the minimum weight of the edges that were successfully unioned and identifies the nodes involved in this union. The function then performs a depth-first search (DFS) starting from one of these nodes and prints the minimum edge weight, the length of the path found by the DFS, and the nodes visited during the DFS. The function does not return any value but modifies the `graph`, `edges`, and `dsu` structures during its execution. The final state of the program includes the sorted `edges` list, the modified `graph` and `dsu` structures, and the printed results.

#State of the program right berfore the function call: curr is a vertex in the graph, parent is the parent vertex of curr in the DFS traversal (or None if curr is the root), and path is a list of vertices representing the current path in the DFS traversal.
def dfs(curr, parent, path):
    if (colors[curr] == 1) :
        return path
        #The program returns the list of vertices representing the current path in the DFS traversal.
    #State: curr is a vertex in the graph, parent is the parent vertex of curr in the DFS traversal (or None if curr is the root), and path is a list of vertices representing the current path in the DFS traversal. Additionally, the color of curr is not 1.
    colors[curr] = 1
    path.append(curr)
    for nei in graph[curr]:
        if colors[nei] != 2 and nei != parent:
            res = dfs(nei, curr, path)
            set_res = set(res)
            if res and node_v in set_res:
                return res
        
    #State: The loop does not directly modify the variables `curr`, `parent`, or `path`. However, it may return a path if a condition is met. If the loop completes all iterations without returning, the state remains: `curr` is a vertex in the graph, `parent` is the parent vertex of `curr` in the DFS traversal (or None if `curr` is the root), `path` is a list of vertices representing the current path in the DFS traversal with `curr` appended to it, and the color of `curr` is 1.
    colors[curr] = 2
    return []
    #The program returns an empty list.
#Overall this is what the function does:The function `dfs` performs a depth-first search in a graph. It accepts a current vertex `curr`, a parent vertex `parent` (or `None` if `curr` is the root), and a list `path` representing the current path in the DFS traversal. The function marks the current vertex as visited (color 1) and appends it to the path. If a cycle is detected (i.e., the current vertex is revisited while its color is 1), the function returns the current path. If the function completes the traversal without finding a cycle, it marks the current vertex as fully processed (color 2) and returns an empty list.

#State of the program right berfore the function call: No variables are passed to the function `func_7`.
def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` is the result of `func_1()`, and `func_6()` has been called `test_cases` times.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It retrieves a value from `func_1` and uses this value to determine the number of times `func_6` should be called. After the function concludes, `func_6` has been called `test_cases` times, where `test_cases` is the result of `func_1()`. The function does not return any value.

