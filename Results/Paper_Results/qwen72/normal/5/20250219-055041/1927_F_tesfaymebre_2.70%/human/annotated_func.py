#State of the program right berfore the function call: None
def func_1():
    return int(sys.stdin.readline().strip())
    #The program returns an integer value read from the standard input (stdin), with leading and trailing whitespace removed.
#Overall this is what the function does:Reads an integer value from the standard input, removes any leading and trailing whitespace, and returns the processed integer value.

#State of the program right berfore the function call: None
def func_2():
    return sys.stdin.readline().strip()
    #The program returns the first line of input from the user, with any trailing whitespace removed.
#Overall this is what the function does:The function `func_2` reads the first line of input from the user via `sys.stdin`, removes any trailing whitespace from this line, and returns the modified line. The function does not accept any parameters and does not modify any external state. After the function concludes, the user will have a string that represents the first line of input they provided, with any trailing whitespace removed.

#State of the program right berfore the function call: No variables are passed to the function. The function reads from standard input, expecting a line of space-separated integers.
def func_3():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object that contains the integers read from a line of space-separated input.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It reads a line of space-separated integers from standard input and returns a map object containing these integers. After the function concludes, the map object can be iterated over to access the integers.

#State of the program right berfore the function call: None
def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers, which are the result of reading a line from standard input, stripping any leading or trailing whitespace, and splitting the line into separate strings that are then converted to integers.
#Overall this is what the function does:The function `func_4` does not accept any parameters. It reads a line from standard input, removes any leading or trailing whitespace, splits the line into separate strings, converts these strings to integers, and returns a list of these integers.

#State of the program right berfore the function call: None of the variables in the function signature are used. This function is a utility function to read a line from standard input, strip any leading or trailing whitespace, and split the line into a list of strings.
def func_5():
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings, where each string is a part of the line read from standard input after stripping leading and trailing whitespace and splitting the line by whitespace.
#Overall this is what the function does:The function `func_5` does not accept any parameters. It reads a line from standard input, removes any leading or trailing whitespace, and splits the line into a list of strings using whitespace as the delimiter. The function returns this list of strings.

#State of the program right berfore the function call: n and m are integers such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5), and graph and edges are initially empty.
def func_6():
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: `u`, `v`, and `w` are assigned new integer values by `func_3()` for each iteration, `graph[u]` now contains the list `[v, v, ..., v]` with `m` elements, `graph[v]` now contains the list `[u, u, ..., u]` with `m` elements, `edges` is a list containing `m` tuples of the form `(w, u, v)`, `i` is `m-1`, `m` must be greater than or equal to 3, `n` and `m` are assigned new integer values by `func_3()` for each iteration.
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
        
    #State: After all iterations of the loop, `u`, `v`, and `w` are assigned new integer values by `func_3()` for each iteration, `graph[u]` contains the list `[v, v, ..., v]` with `m` elements, `graph[v]` contains the list `[u, u, ..., u]` with `m` elements, `edges` is a list containing `m` tuples of the form `(w, u, v)` sorted in descending order by the value of `w`, `i` is 0, `m` is greater than or equal to 3, `n` and `m` are assigned new integer values by `func_3()` for each iteration, `dsu` is a DSU object initialized with `n + 1` elements. `node_u` and `node_v` are the last nodes that were unioned, and `_min_edge` is the minimum edge weight among all the edges that were unioned.
    colors = [0] * (n + 1)
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    #This is printed: _min_edge, len(res) (where _min_edge is the minimum edge weight among all the edges that were unioned, and len(res) is the number of nodes collected by the dfs function starting from node_u)
    print(*res)
    #This is printed: [nodes visited in the dfs traversal starting from node_u, including node_u and node_v] (where the exact nodes depend on the graph structure and the implementation of the dfs function)
#Overall this is what the function does:The function `func_6` initializes an empty graph and an empty list of edges, then populates the graph and edges based on `m` iterations of values provided by `func_3()`. It sorts the edges in descending order by weight, processes them using a Disjoint Set Union (DSU) structure to union nodes and track the minimum edge weight, and finally performs a depth-first search (DFS) starting from a specific node to print the minimum edge weight and the number of nodes in the DFS traversal, followed by the nodes themselves. The function does not accept any parameters and does not return any values. The final state of the program includes a populated graph, a sorted list of edges, and the printed results of the minimum edge weight and the DFS traversal nodes.

#State of the program right berfore the function call: curr and parent are integers representing vertices in the graph, and path is a list of integers representing the current path in the DFS traversal.
def dfs(curr, parent, path):
    if (colors[curr] == 1) :
        return path
        #The program returns the list `path` which represents the current path in the DFS traversal.
    #State: `curr` and `parent` are integers representing vertices in the graph, and `path` is a list of integers representing the current path in the DFS traversal. Additionally, `colors[curr]` is not equal to 1.
    colors[curr] = 1
    path.append(curr)
    for nei in graph[curr]:
        if colors[nei] != 2 and nei != parent:
            res = dfs(nei, curr, path)
            set_res = set(res)
            if res and node_v in set_res:
                return res
        
    #State: The loop has completed all iterations. `curr` and `parent` remain integers representing vertices in the graph, `path` is a list of integers representing the current path in the DFS traversal with `curr` appended to it, `colors[curr]` is still 1, and `graph[curr]` has been fully iterated over. If any neighbor `nei` of `curr` (where `nei` is not `parent` and `colors[nei]` is not 2) resulted in a non-empty `res` from the `dfs` function and `node_v` is in `set_res`, the function returns `res`. Otherwise, the function returns an empty list.
    colors[curr] = 2
    return []
    #The program returns an empty list.
#Overall this is what the function does:The function `dfs` performs a depth-first search (DFS) traversal in a graph. It accepts three parameters: `curr` (the current vertex), `parent` (the parent vertex in the DFS traversal), and `path` (the current path in the DFS traversal). The function modifies the `colors` and `path` variables. If the current vertex `curr` is already being visited (i.e., `colors[curr]` is 1), it returns the current path. If a valid path is found from a neighbor of `curr` (excluding `parent` and any already fully visited vertices), and this path includes a specific node `node_v`, it returns this path. If no such path is found, it marks the current vertex as fully visited (i.e., `colors[curr]` is 2) and returns an empty list. The final state of the program is that the `colors` and `path` variables are updated, and the function returns either the current path or an empty list.

#State of the program right berfore the function call: No variables are passed to the function `func_7`.
def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` must be greater than or equal to the number of iterations, `func_6()` has been called `test_cases` times.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It retrieves a number of test cases from `func_1` and then calls `func_6` that many times. After the function concludes, `func_6` has been called a number of times equal to the value returned by `func_1`. The function itself does not return any value.

