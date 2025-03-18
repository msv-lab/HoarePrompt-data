#State of the program right berfore the function call: No variables in the function signature.
def func_1():
    return int(sys.stdin.readline().strip())
    #The program returns an integer read from the standard input (stdin).
#Overall this is what the function does:The function reads a line from the standard input, strips any leading or trailing whitespace, converts it to an integer, and returns this integer.

#State of the program right berfore the function call: No variables are present in the function signature, thus no specific precondition can be derived from the variables.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns a string that is the next line of input from standard input, with leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_2` accepts no parameters and returns a string representing the next line of input from standard input, with any leading and trailing whitespace removed.

#State of the program right berfore the function call: This function does not have any parameters. It reads a line from the standard input, strips any leading/trailing whitespace, splits the line into a list of substrings based on whitespace, converts each substring to an integer, and returns the resulting map object containing these integers.
def func_3():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object containing integers that were converted from a line of whitespace-separated substrings read from standard input.
#Overall this is what the function does:The function reads a line from standard input, strips any leading or trailing whitespace, splits the line into substrings based on whitespace, converts each substring to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: No variables are present in the function signature of `func_4`.
def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers that are obtained by reading a line from standard input, stripping any leading or trailing whitespace, splitting the line into substrings based on whitespace, and converting each substring to an integer.
#Overall this is what the function does:The function `func_4` reads a line from standard input, removes any leading or trailing whitespace, splits the line into substrings based on whitespace, converts each substring to an integer, and returns a list of these integers.

#State of the program right berfore the function call: No variables in the function signature. This function reads a line from standard input and returns a list of strings, which are the space-separated values from that line.
def func_5():
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings, which are the space-separated values from the line read from standard input.
#Overall this is what the function does:The function reads a line from standard input, strips any leading or trailing whitespace, splits the line into space-separated components, and returns these components as a list of strings.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the graph, and m is an integer representing the number of edges in the graph such that 3 <= n <= m <= min(n*(n - 1)/2, 2 * 10^5).
def func_6():
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: `graph` is a defaultdict of lists where each key (node) has a list of adjacent nodes connected by edges. `edges` is a list of tuples, where each tuple contains a weight `w` and the two nodes `u` and `v` that the edge connects. After `m` iterations, `graph` will have `m` edges added to it, and `edges` will contain `m` tuples representing these edges. The values of `n` and `m` remain unchanged.
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
        
    #State: `graph` is a defaultdict of lists; `edges` is a list of tuples sorted in descending order based on weight; `dsu` is an instance of the DSU class with updated connected components; `n` and `m` remain unchanged; `_min_edge` is the weight of the smallest edge in the last updated component; `node_u` and `node_v` are the nodes of that smallest edge.
    colors = [0] * (n + 1)
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    #This is printed: _min_edge, len(res) (where _min_edge is the weight of the smallest edge in the last updated connected component and len(res) is the number of elements in the result of the dfs function starting from node_u)
    print(*res)
    #This is printed: node_u [nodes visited in DFS order starting from node_u] (where node_u is the starting node of the DFS and the nodes are the elements of the list `res`)
#Overall this is what the function does:The function `func_6` constructs a graph using a given number of vertices `n` and edges `m`, sorts the edges by weight in descending order, and then uses a Disjoint Set Union (DSU) structure to process these edges. It identifies the smallest edge in the last updated connected component and performs a Depth-First Search (DFS) starting from one of the nodes of this smallest edge. The function prints the weight of this smallest edge and the number of nodes visited in the DFS, followed by the list of nodes visited in DFS order.

#State of the program right berfore the function call: curr is an integer representing the current vertex, parent is an integer representing the parent vertex in the DFS traversal, and path is a list of integers representing the current path in the traversal.
def dfs(curr, parent, path):
    if (colors[curr] == 1) :
        return path
        #The program returns the list 'path' representing the current path in the DFS traversal
    #State: curr is an integer representing the current vertex, parent is an integer representing the parent vertex in the DFS traversal, and path is a list of integers representing the current path in the traversal. The color of the vertex `curr` is not 1.
    colors[curr] = 1
    path.append(curr)
    for nei in graph[curr]:
        if colors[nei] != 2 and nei != parent:
            res = dfs(nei, curr, path)
            set_res = set(res)
            if res and node_v in set_res:
                return res
        
    #State: `curr` is an integer representing the current vertex, `parent` is an integer representing the parent vertex in the DFS traversal, and `path` is a list of integers representing the current path in the traversal with `curr` appended to it. The color of the vertex `curr` is 1.
    colors[curr] = 2
    return []
    #The program returns an empty list.
#Overall this is what the function does:The function `dfs` performs a depth-first search on a graph starting from a given vertex `curr`, with `parent` indicating the parent vertex in the traversal, and `path` keeping track of the current traversal path. It returns the `path` if a specific node (`node_v`) is found in the path during the traversal; otherwise, it returns an empty list.

#State of the program right berfore the function call: No variables are present in the function signature of `func_7()`.
def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` holds the same return value of `func_1()` as in the initial state.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It retrieves the number of test cases from `func_1()` and executes `func_6()` for each test case. The function does not return any value.

