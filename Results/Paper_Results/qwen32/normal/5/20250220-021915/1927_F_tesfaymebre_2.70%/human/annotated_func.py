#State of the program right berfore the function call: No variables in the function signature.
def func_1():
    return int(sys.stdin.readline().strip())
    #The program returns an integer value that is read from the standard input and stripped of any leading or trailing whitespace.
#Overall this is what the function does:The function `func_1` reads an integer from the standard input, removes any leading or trailing whitespace, and returns this integer.

#State of the program right berfore the function call: No variables in the function signature. The function `func_2` does not take any parameters and returns a string read from standard input, stripped of leading and trailing whitespace.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns a string that is read from standard input and stripped of any leading or trailing whitespace.
#Overall this is what the function does:The function `func_2` reads a string from standard input, removes any leading or trailing whitespace from the string, and returns the resulting string.

#State of the program right berfore the function call: No variables are present in the function signature of `func_3()`. The function reads a line from standard input, splits it into strings, converts each string to an integer, and returns a map object containing these integers.
def func_3():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object containing integers that were read from standard input, split by whitespace, and converted to integers.
#Overall this is what the function does:The function `func_3` reads a line from standard input, splits the line into strings based on whitespace, converts each string to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: No variables are present in the function signature.
def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers that were read from the standard input, split by whitespace, and converted from strings to integers.
#Overall this is what the function does:The function `func_4` reads a line of input from the standard input, splits it into parts based on whitespace, converts each part from a string to an integer, and returns a list of these integers.

#State of the program right berfore the function call: No variables are present in the function signature of `func_5`.
def func_5():
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings, where each string is a substring from the input line provided to the standard input, split by whitespace.
#Overall this is what the function does:The function `func_5` reads a line of input from the standard input, splits it into substrings by whitespace, and returns a list of these substrings.

#State of the program right berfore the function call: n and m are integers representing the number of vertices and edges in the graph respectively, where 3 <= n <= m <= min((n*(n - 1))/2, 2 * 10^5).
def func_6():
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: `n` and `m` are the values returned by `func_3()`, where 3 <= n <= m <= min((n*(n - 1))/2, 2 * 10^5); `graph` is a defaultdict of lists with each node having a list of adjacent nodes; `edges` is a list containing `m` tuples, each representing an edge with its weight and the two nodes it connects; `m` iterations have completed; `i` is `m-1`; `u`, `v`, and `w` are the values returned by `func_3()` in the last iteration; all edges specified by the `func_3()` calls have been added to `graph` and `edges`.
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
        
    #State: All edges have been processed, and the graph is fully connected if possible. The DSU structure reflects the connected components of the graph. The variables `_min_edge`, `node_u`, and `node_v` hold the information about the edge with the minimum weight in the last merged component.
    colors = [0] * (n + 1)
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    #This is printed: _min_edge (where _min_edge is the edge with the minimum weight in the last merged component), len(res) (where len(res) is the number of nodes in the graph)
    print(*res)
    #This is printed: node1 node2 node3 ... nodeN (where node1, node2, ..., nodeN are the nodes in the graph visited during the DFS traversal)
#Overall this is what the function does:The function `func_6` constructs a graph using the number of vertices `n` and edges `m` provided by `func_3()`. It processes the edges to find a specific edge with the minimum weight in the last merged component using a Disjoint Set Union (DSU) structure. It then performs a Depth-First Search (DFS) starting from one of the nodes of this edge and prints the minimum weight of the edge and the number of nodes visited during the DFS traversal. Additionally, it prints the nodes visited during the DFS.

#State of the program right berfore the function call: curr is an integer representing the current vertex, parent is an integer representing the parent vertex of the current vertex in the DFS traversal, and path is a list of integers representing the current path taken in the DFS traversal.
def dfs(curr, parent, path):
    if (colors[curr] == 1) :
        return path
        #The program returns the current path taken in the DFS traversal.
    #State: curr is an integer representing the current vertex, parent is an integer representing the parent vertex of the current vertex in the DFS traversal, and path is a list of integers representing the current path taken in the DFS traversal. Additionally, the color of the current vertex (colors[curr]) is not 1.
    colors[curr] = 1
    path.append(curr)
    for nei in graph[curr]:
        if colors[nei] != 2 and nei != parent:
            res = dfs(nei, curr, path)
            set_res = set(res)
            if res and node_v in set_res:
                return res
        
    #State: `curr` is an integer representing the current vertex, `parent` is an integer representing the parent vertex of the current vertex in the DFS traversal, `path` is a list of integers representing the current path taken in the DFS traversal and now includes `curr` as its last element, and the color of the current vertex (`colors[curr]`) is 1. The function returns a path containing `node_v` if found, or `None` if no such path is found after exploring all neighbors.
    colors[curr] = 2
    return []
    #The program returns an empty list.
#Overall this is what the function does:The function `dfs` performs a depth-first search starting from a given vertex `curr` and returns a path that includes a specific node `node_v` if such a path exists. If no such path is found, it returns an empty list. The function uses a list `path` to keep track of the current path and an array `colors` to mark the state of each vertex during the traversal.

#State of the program right berfore the function call: test_cases is an integer representing the number of test cases, where 1 <= test_cases <= 10^4.
def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` iterations of `func_6()` have been completed, and `test_cases` remains unchanged.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It performs a number of iterations equal to the value returned by `func_1()`, where each iteration calls `func_6()`. The function returns the number of test cases, which is an integer between 1 and 10,000.

