#State of the program right berfore the function call: No variables in the function signature.
def func_1():
    return int(sys.stdin.readline().strip())
    #The program returns an integer value that is read from the standard input, stripped of any leading or trailing whitespace.
#Overall this is what the function does:The function `func_1` reads an integer from the standard input, removes any leading or trailing whitespace, and returns this integer.

#State of the program right berfore the function call: No specific variables are present in the function signature. The function `func_2` does not take any parameters and is expected to read a line from standard input, strip any leading/trailing whitespace, and return it as a string.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns a string that is the line read from standard input, with any leading or trailing whitespace removed.
#Overall this is what the function does:The function `func_2` reads a line from standard input, removes any leading or trailing whitespace from the line, and returns the resulting string.

#State of the program right berfore the function call: No variables in the function signature. The function `func_3` reads a line from standard input, strips any leading/trailing whitespace, splits the line into a list of strings based on whitespace, and maps each string to an integer.
def func_3():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object that contains integers, which are the result of mapping each string from the list of strings (obtained by splitting a line read from standard input, stripped of leading/trailing whitespace) to an integer.
#Overall this is what the function does:The function `func_3` reads a line from standard input, removes any leading or trailing whitespace, splits the line into a list of strings based on whitespace, converts each string in the list to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: No variables are present in the function signature of `func_4()`. This function reads a line from standard input, strips any leading/trailing whitespace, splits the line into a list of strings based on whitespace, and maps each string to an integer, returning the resulting list of integers.
def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers derived from a line of input where each integer corresponds to a whitespace-separated string from the input line after stripping any leading or trailing whitespace.
#Overall this is what the function does:The function `func_4` reads a line from standard input, removes any leading or trailing whitespace, splits the line into a list of strings based on whitespace, converts each string to an integer, and returns the resulting list of integers.

#State of the program right berfore the function call: No variables are present in the function signature of `func_5`. This function reads a line from standard input, strips any leading/trailing whitespace, splits the line into a list of substrings separated by whitespace, and returns this list.
def func_5():
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of substrings obtained by splitting a line read from standard input, after stripping any leading or trailing whitespace.
#Overall this is what the function does:The function reads a line from standard input, removes any leading or trailing whitespace, splits the line into a list of substrings based on whitespace, and returns this list.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the graph, m is an integer representing the number of edges in the graph such that 3 <= n <= m <= min((n*(n - 1))/2, 2 * 10^5).
def func_6():
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: `n` and `m` remain the values returned by `func_3()`, `graph` is a defaultdict with list as the default factory containing `m` edges represented as adjacency lists, and `edges` is a list of `m` tuples, each containing a weight `w` and the vertices `u` and `v` of an edge.
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
        
    #State: `n` and `m` remain the values returned by `func_3()`, `graph` is a defaultdict with list as the default factory containing `m` edges represented as adjacency lists, `edges` is a list of `m` tuples, each containing a weight `w` and the vertices `u` and `v` of an edge, sorted in descending order by weight `w`, then by vertex `u`, and finally by vertex `v`, `dsu` is an instance of the DSU class with `n + 1` elements reflecting the connected components after processing all edges, `_min_edge` is the minimum weight of an edge found among the edges that connect vertices already in the same set, `node_u` is the first vertex of the edge with the minimum weight found among the edges that connect vertices already in the same set, `node_v` is the second vertex of the edge with the minimum weight found among the edges that connect vertices already in the same set.
    colors = [0] * (n + 1)
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    #This is printed: _min_edge, len(res) (where _min_edge is the minimum weight of an edge connecting vertices already in the same set, and res is the result of the dfs function starting from node_u)
    print(*res)
    #This is printed: res (where res is the result of the dfs function starting from node_u)
#Overall this is what the function does:The function `func_6` constructs a graph from a given number of vertices `n` and edges `m`, processes the edges to find a minimum-weight edge that connects vertices already in the same connected component, and then performs a depth-first search (DFS) starting from one of the vertices of this edge. It prints the weight of this edge and the number of vertices visited during the DFS, followed by the list of visited vertices.

#State of the program right berfore the function call: curr is an integer representing the current vertex, parent is an integer representing the parent vertex, and path is a list of integers representing the current path in the depth-first search.
def dfs(curr, parent, path):
    if (colors[curr] == 1) :
        return path
        #The program returns the list 'path' representing the current path in the depth-first search.
    #State: `curr` is an integer representing the current vertex, `parent` is an integer representing the parent vertex, and `path` is a list of integers representing the current path in the depth-first search. The color of the vertex `curr` is not equal to 1.
    colors[curr] = 1
    path.append(curr)
    for nei in graph[curr]:
        if colors[nei] != 2 and nei != parent:
            res = dfs(nei, curr, path)
            set_res = set(res)
            if res and node_v in set_res:
                return res
        
    #State: `curr` is an integer representing the current vertex, `parent` is an integer representing the parent vertex, and `path` is a list of integers representing the current path in the depth-first search, with `curr` appended to it. The color of the vertex `curr` is 1. If a path containing `node_v` is found during the DFS, it is returned and the loop terminates early. Otherwise, the loop completes without returning a path.
    colors[curr] = 2
    return []
    #The program returns an empty list.
#Overall this is what the function does:The function performs a depth-first search starting from a given vertex `curr`, keeping track of the path. It returns the path if it contains a specific node `node_v`; otherwise, it returns an empty list.

#State of the program right berfore the function call: No variables are present in the function signature of `func_7()`. It does not take any parameters and does not return any values. It relies on other functions (`func_1()` and `func_6()`) to perform its operations.
def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` holds the value returned by `func_1()`.
#Overall this is what the function does:The function `func_7` does not accept any parameters and does not return any values. It performs a series of operations by calling `func_1()` to determine the number of test cases and then calls `func_6()` for each test case.

