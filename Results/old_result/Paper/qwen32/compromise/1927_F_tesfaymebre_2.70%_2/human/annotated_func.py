#State of the program right berfore the function call: No variables in the function signature.
def func_1():
    return int(sys.stdin.readline().strip())
    #The program returns an integer value that is read from the standard input and stripped of any leading or trailing whitespace.
#Overall this is what the function does:The function `func_1` reads an integer from the standard input, removes any leading or trailing whitespace, and returns this integer.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2()`. This function reads a line from the standard input and returns it as a string without any leading or trailing whitespace.
def func_2():
    return sys.stdin.readline().strip()
    #The program reads a line from the standard input and returns it as a string without any leading or trailing whitespace.
#Overall this is what the function does:The function `func_2` reads a line from the standard input, removes any leading or trailing whitespace from the line, and returns the resulting string.

#State of the program right berfore the function call: No variables are present in the function signature of `func_3`. The function reads a line from the standard input, strips any leading/trailing whitespace, splits the line into substrings based on whitespace, converts each substring to an integer, and returns a map object containing these integers.
def func_3():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object containing integers that were converted from substrings of a line read from standard input, where each substring was separated by whitespace.
#Overall this is what the function does:The function reads a line from the standard input, trims any leading or trailing whitespace, splits the line into substrings based on whitespace, converts each substring to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: No variables are present in the function signature of `func_4`. The function reads a line from standard input, strips any leading/trailing whitespace, splits the line into substrings based on whitespace, converts each substring to an integer, and returns the resulting list of integers.
def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers, where each integer is a substring converted from a line read from standard input, stripped of leading/trailing whitespace, and split based on whitespace.
#Overall this is what the function does:The function `func_4` reads a line from standard input, removes any leading or trailing whitespace, splits the line into substrings based on whitespace, converts each substring to an integer, and returns the resulting list of integers.

#State of the program right berfore the function call: No variables are present in the function signature, thus no specific precondition can be derived from the variables alone.
def func_5():
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings, where each string is a substring from the input line provided to the program, split by whitespace.
#Overall this is what the function does:The function `func_5` reads a line of input from the standard input, removes any leading or trailing whitespace, splits the line into substrings separated by whitespace, and returns these substrings as a list of strings.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the graph, m is an integer representing the number of edges in the graph such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5).
def func_6():
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: `n` and `m` remain the values returned by `func_3()`, `graph` is a defaultdict of lists where each key (node) has a list of connected nodes (forming an undirected graph), and `edges` is a list of tuples, each containing a weight `w` and two nodes `u` and `v` representing an edge in the graph.
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
        
    #State: `n` and `m` remain the values returned by `func_3()`, `graph` is unchanged, `edges` is unchanged, `dsu` reflects the connected components, `_min_edge` is the smallest edge weight in any connected component, `node_u` and `node_v` are the nodes of the edge with the smallest weight in the connected component.
    colors = [0] * (n + 1)
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    #This is printed: _min_edge (where _min_edge is the smallest edge weight in any connected component), len(res) (where res is the result of the dfs(node_u, -1, []) function call)
    print(*res)
    #This is printed: res (where res is the list of nodes visited during the DFS traversal starting from node_u)
#Overall this is what the function does:The function `func_6` constructs an undirected graph with `n` vertices and `m` edges, identifies the smallest edge weight in any connected component of the graph, and performs a depth-first search (DFS) starting from one of the nodes of the smallest edge. It then prints the smallest edge weight and the number of nodes visited during the DFS, followed by the list of nodes visited.

#State of the program right berfore the function call: curr is an integer representing the current vertex, parent is an integer representing the parent vertex of the current vertex, and path is a list of integers representing the current path in the depth-first search.
def dfs(curr, parent, path):
    if (colors[curr] == 1) :
        return path
        #The program returns the list `path` representing the current path in the depth-first search.
    #State: `curr` is an integer representing the current vertex, `parent` is an integer representing the parent vertex of the current vertex, and `path` is a list of integers representing the current path in the depth-first search. Additionally, the color of the current vertex (`colors[curr]`) is not equal to 1.
    colors[curr] = 1
    path.append(curr)
    for nei in graph[curr]:
        if colors[nei] != 2 and nei != parent:
            res = dfs(nei, curr, path)
            set_res = set(res)
            if res and node_v in set_res:
                return res
        
    #State: `curr` is an integer representing the current vertex, `parent` is an integer representing the parent vertex of the current vertex, `path` is a list of integers representing the current path in the depth-first search with `curr` appended to it, and the color of the current vertex (`colors[curr]`) is equal to 1.
    colors[curr] = 2
    return []
    #The program returns an empty list.
#Overall this is what the function does:The function performs a depth-first search starting from a given vertex (`curr`) and returns the current path (`path`) if a specific node (`node_v`) is found in the path. If the search completes without finding `node_v`, it returns an empty list.

#State of the program right berfore the function call: No variables are present in the function signature of `func_7`.
def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` still holds the return value of `func_1()`, which is `N`.
    #
    #Output State:
#Overall this is what the function does:The function `func_7` does not accept any parameters. It executes a number of iterations determined by the return value of `func_1()`, calling `func_6()` in each iteration. The function itself does not return any value, but it performs actions based on the logic within `func_6()`.

