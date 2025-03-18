#State of the program right berfore the function call: None. This function does not take any parameters and is used to read an integer from standard input, typically representing the number of test cases.
def func_1():
    return int(sys.stdin.readline().strip())
    #The program returns an integer read from standard input, typically representing the number of test cases.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads an integer from standard input, typically representing the number of test cases, and returns this integer.

#State of the program right berfore the function call: None of the variables are used in the function signature.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns the first line of input from the user, with any leading or trailing whitespace removed.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns the first line of input from the user, with any leading or trailing whitespace removed.

#State of the program right berfore the function call: None of the variables in the function signature are used. The function reads input from stdin and returns a map object of integers.
def func_3():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object containing integers, which are the result of converting the input string from stdin into a list of integers by splitting the string on whitespace and stripping any leading or trailing whitespace.
#Overall this is what the function does:The function `func_3` reads a line of input from standard input (stdin), splits the line into substrings based on whitespace, converts each substring to an integer, and returns a map object containing these integers. The function does not modify any external variables and does not have any side effects. After the function concludes, the caller will have a map object that can be iterated over to access the integers.

#State of the program right berfore the function call: None
def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers read from the standard input, where each integer is separated by spaces.
#Overall this is what the function does:The function reads a line from the standard input, splits the line into substrings based on spaces, converts each substring to an integer, and returns a list of these integers.

#State of the program right berfore the function call: None
def func_5():
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings, where each string is a word from the input line read from standard input (stdin), excluding any leading or trailing whitespace.
#Overall this is what the function does:The function `func_5` does not accept any parameters. It reads a line from standard input (stdin), removes any leading or trailing whitespace, splits the line into words, and returns a list of these words as strings.

#State of the program right berfore the function call: n and m are integers such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5), and graph is a defaultdict of lists representing an undirected graph, and edges is a list of tuples (w, u, v) where 1 <= u, v <= n, u != v, and 1 <= w <= 10^6.
def func_6():
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: `n` and `m` remain unchanged, `graph` is a defaultdict of lists where each key has a list of nodes it is connected to, and `edges` is a list of tuples representing the edges in the graph, each tuple containing the weight and the two nodes it connects.
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
        
    #State: `n` and `m` remain unchanged, `graph` is a defaultdict of lists where each key has a list of nodes it is connected to, `edges` is now a sorted list of tuples in descending order based on the edge weights, `dsu` is an instance of the DSU class with updated parent and min_edge values, `_min_edge` is the minimum edge weight that was successfully added to the DSU, `node_u` is the node u of the edge with the minimum weight that was successfully added to the DSU, `node_v` is the node v of the edge with the minimum weight that was successfully added to the DSU.
    colors = [0] * (n + 1)
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    #This is printed: - The print statement will output the minimum edge weight `_min_edge` and the length of the list `res`.
    #
    #Output:
    print(*res)
    #This is printed: [elements of res] (where res is the result of the dfs function called with node_u, -1, and an empty list)
#Overall this is what the function does:The function `func_6` does not accept any parameters but initializes and uses `n`, `m`, `graph`, and `edges` internally. It constructs an undirected graph from a list of weighted edges and uses a Disjoint Set Union (DSU) data structure to find and union components of the graph. After processing, it prints the minimum edge weight that was successfully added to the DSU and the length of a list `res` obtained from a depth-first search (DFS) starting from a specific node. It also prints the elements of `res`. The final state of the program includes the original `n` and `m` values, a `graph` representing the constructed undirected graph, a sorted `edges` list, an updated `dsu` instance, and the printed values.

#State of the program right berfore the function call: curr is an integer representing the current vertex, parent is an integer representing the parent vertex in the DFS traversal, and path is a list of integers representing the current path in the DFS traversal.
def dfs(curr, parent, path):
    if (colors[curr] == 1) :
        return path
        #The program returns the current path in the DFS traversal, represented by the list `path`.
    #State: curr is an integer representing the current vertex, parent is an integer representing the parent vertex in the DFS traversal, and path is a list of integers representing the current path in the DFS traversal. Additionally, the color of the current vertex `curr` is not 1.
    colors[curr] = 1
    path.append(curr)
    for nei in graph[curr]:
        if colors[nei] != 2 and nei != parent:
            res = dfs(nei, curr, path)
            set_res = set(res)
            if res and node_v in set_res:
                return res
        
    #State: The loop will iterate through all neighbors `nei` of the current vertex `curr` in the graph. If a neighbor `nei` is not already fully processed (i.e., `colors[nei] != 2`) and is not the parent vertex, the loop will call `dfs(nei, curr, path)`. If the result of the `dfs` call is not `None` and contains `node_v`, the loop will return this result. If no such result is found, the loop will complete all iterations, and the state of `curr`, `parent`, and `path` will remain unchanged.
    colors[curr] = 2
    return []
    #The program returns an empty list.
#Overall this is what the function does:The function `dfs` performs a depth-first search (DFS) traversal in a graph. It accepts three parameters: `curr` (the current vertex), `parent` (the parent vertex), and `path` (the current path in the DFS traversal). The function marks the current vertex as being visited and appends it to the path. If the current vertex has already been visited (i.e., its color is 1), the function returns the current path. Otherwise, it recursively explores all unvisited neighbors of the current vertex, excluding the parent vertex. If a neighbor's path contains a specific node `node_v`, the function returns that path. If no such path is found, the function marks the current vertex as fully processed and returns an empty list.

#State of the program right berfore the function call: No variables are passed to the function `func_7`.
def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` remains the same as the result of `func_1()`.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It retrieves a number of test cases by calling `func_1()`, and then iterates that many times, calling `func_6()` in each iteration. After the function concludes, the value of `test_cases` remains unchanged, and the function does not return any value.

