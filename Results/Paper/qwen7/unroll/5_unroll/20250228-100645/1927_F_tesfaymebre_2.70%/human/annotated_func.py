#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 3 ≤ n ≤ m ≤ min(⌊n(n - 1)/2⌋, 2 ⋅ 10^5), and u, v, and w are integers such that 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6.
def func_1():
    return int(sys.stdin.readline().strip())
    #The program reads an integer from standard input, strips any trailing whitespace, and returns it as an integer.
#Overall this is what the function does:The function reads an integer from standard input, removes any trailing whitespace, and returns it as an integer.

#State of the program right berfore the function call: None of the variables in the provided function are relevant to the problem description. The function `func_2()` simply reads a line from standard input and returns it stripped of leading and trailing whitespace. This function does not take any parameters and thus no precondition can be derived from its signature alone.
def func_2():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips leading and trailing whitespace, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes any leading and trailing whitespace, and returns the processed line.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 3 ≤ n ≤ m ≤ min(\frac{n\cdot(n - 1)}{2}, 2 \cdot 10^5), and m represents the number of edges in the graph. Each of the next m lines contains three integers u, v, and w such that 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6, representing an edge between vertices u and v with weight w.
def func_3():
    return map(int, sys.stdin.readline().strip().split())
    #The program reads a line from standard input, strips any trailing whitespace, splits the line into individual strings, and maps each string to an integer, returning the resulting tuple of integers.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, splits the line into individual strings, converts each string to an integer, and returns a tuple of these integers.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 3 ≤ n ≤ m ≤ min(⌊n⋅(n−1)/2⌋, 2⋅10^5), and the following m lines contain three integers u, v, and w such that 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6.
def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers read from the standard input, where each integer corresponds to the values split from a line of input.
#Overall this is what the function does:The function reads a line of input from the standard input, splits it into individual integers, and returns them as a list. This process is repeated until all specified inputs are read and converted.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three lines: the first line contains two integers n and m such that 3 ≤ n ≤ m ≤ min(\frac{n\cdot(n - 1)}{2}, 2 \cdot 10^5), representing the number of vertices and edges in the graph, respectively. The next m lines each contain three integers u, v, and w such that 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6, representing an edge between vertices u and v with weight w.
def func_5():
    return list(sys.stdin.readline().strip().split())
    #The program returns a list containing the values of n and m from the first line of input, where n and m are separated by a space.
#Overall this is what the function does:The function reads the first line of input from standard input, splits it into two parts based on space separation, and returns these parts as a list. This list contains the values of n and m, which represent the number of vertices and edges in a graph, respectively.

#State of the program right berfore the function call: (n, m) are integers such that 3 ≤ n ≤ m ≤ min(⌊n*(n - 1)/2⌋, 2 * 10^5), edges is a list of tuples where each tuple contains three integers (u, v, w) representing an edge between vertices u and v with weight w, and DSU is a disjoint set union data structure initialized with n+1 elements.
def func_6():
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: Output State: `n` is the return value of `func_3()`, `m` is the return value of `func_3()`, `graph` is a defaultdict where each key has a list of values representing connected nodes, `edges` is a list of tuples where each tuple contains a weight and a pair of connected nodes. After executing the loop, `graph` will contain edges between nodes based on the values returned by `func_3()` for each iteration, and `edges` will contain the weights and corresponding node pairs for all iterations.
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
        
    #State: `node_u` is a node index, `_min_edge` is the minimum edge weight among the connected components formed during the process, `dsu` is a DSU object with updated find and union operations based on the edges processed, `n` is the return value of `func_3()`, `m` is the return value of `func_3()`, `graph` remains unchanged, `edges` is a list of tuples where each tuple contains a weight and a pair of connected nodes (sorted in descending order by weight), `node_v` is a node index.
    colors = [0] * (n + 1)
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    #This is printed: _min_edge, len(res)
    print(*res)
    #This is printed: nodes visited during DFS from node_u excluding its parent (where nodes are the nodes visited in the DFS traversal excluding the parent of node_u)
#Overall this is what the function does:The function processes a graph represented by a list of edges and a disjoint set union (DSU) data structure. It first constructs an adjacency list and a sorted list of edges. Then, it finds the minimum edge weight among the connected components using the DSU. Finally, it performs a depth-first search (DFS) starting from a selected node and prints the minimum edge weight and the nodes visited during the DFS traversal, excluding the parent node.

#State of the program right berfore the function call: curr is an integer representing the current vertex being visited, parent is an integer representing the parent vertex of the current vertex in the DFS traversal, and path is a list representing the current path of vertices being traversed.
def dfs(curr, parent, path):
    if (colors[curr] == 1) :
        return path
        #The program returns the list 'path' which represents the current path of vertices being traversed during the DFS traversal.
    #State: `curr` is an integer representing the current vertex being visited, `parent` is an integer representing the parent vertex of the current vertex in the DFS traversal, and `path` is a list representing the current path of vertices being traversed. The color of the current vertex `curr` is not 1.
    colors[curr] = 1
    path.append(curr)
    for nei in graph[curr]:
        if colors[nei] != 2 and nei != parent:
            res = dfs(nei, curr, path)
            set_res = set(res)
            if res and node_v in set_res:
                return res
        
    #State: Output State: `curr` is an integer representing the current vertex being visited, `parent` is an integer representing the parent vertex of the current vertex in the DFS traversal, `path` is a list representing the current path of vertices being traversed with `curr` appended to it, and the color of the current vertex `curr` is now 1. The variable `res` contains a list of vertices forming a cycle if one is found during the DFS traversal, otherwise it is an empty list.
    colors[curr] = 2
    return []
    #The program returns an empty list
#Overall this is what the function does:The function `dfs` accepts three parameters: an integer `curr` representing the current vertex being visited, an integer `parent` representing the parent vertex of the current vertex in the DFS traversal, and a list `path` representing the current path of vertices being traversed. It returns the current path of vertices being traversed during the DFS traversal or an empty list if no cycle is detected or other specific conditions are met.

#State of the program right berfore the function call: test_cases is a positive integer representing the number of test cases. For each test case, n and m are integers such that 3 ≤ n ≤ m ≤ min(⌊n⋅(n - 1)/2⌋, 2 ⋅ 10^5), and m represents the number of edges. Each edge is represented by three integers u, v, and w, where 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6. The graph is guaranteed to have at least one simple cycle, and the sum of m across all test cases does not exceed 2 ⋅ 10^5.
def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: Output State: `test_cases` is 0.
    #
    #Explanation: The loop runs `test_cases` times, decrementing `test_cases` each time `_` is iterated over. After all iterations are complete, `test_cases` will be 0.
#Overall this is what the function does:The function accepts a parameter `test_cases`, which is a positive integer representing the number of test cases. For each test case, it processes two integers `n` and `m`, where `3 ≤ n ≤ m ≤ \min(\lfloor n \cdot (n - 1)/2 \rfloor, 2 \cdot 10^5)`, and `m` represents the number of edges. Each edge is represented by three integers `u`, `v`, and `w`, where `1 ≤ u, v ≤ n`, `u ≠ v`, and `1 ≤ w ≤ 10^6`. The graph is guaranteed to have at least one simple cycle, and the sum of `m` across all test cases does not exceed `2 \cdot 10^5`. After processing all test cases, the function outputs information about the graph based on the given parameters. The final state of the program is that `test_cases` is set to 0, indicating that all test cases have been processed.

