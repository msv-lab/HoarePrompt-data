#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of integers n and m representing the number of vertices and edges in the graph respectively, where 3 ≤ n ≤ m ≤ min(\frac{n\cdot(n - 1)}{2}, 2 \cdot 10^5). For each edge, there are three integers u, v, and w representing the vertices connected by the edge and its weight, where 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6.
def func_1():
    return int(sys.stdin.readline().strip())
    #The program reads an integer from standard input, strips any trailing whitespace, and returns it as an integer.
#Overall this is what the function does:The function reads an integer from standard input, removes any trailing whitespace, and returns it as an integer.

#State of the program right berfore the function call: None of the variables in the provided function signature are present in the given code snippet. The function `func_2` reads a single line from standard input and returns it after stripping any trailing whitespace, but no variables are defined or passed to this function within the snippet itself.
def func_2():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns the modified line.

#State of the program right berfore the function call: None of the variables in the function `func_3()` are provided or described in the function signature. The function reads input from standard input, specifically splitting a line into space-separated integers.
def func_3():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object containing integers converted from space-separated integers read from standard input.
#Overall this is what the function does:The function reads space-separated integers from standard input, converts them to integers, and returns a map object containing these integers.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 3 ≤ n ≤ m ≤ min(⌊n(n - 1)/2⌋, 2 ⋅ 10^5), and u, v, and w are integers such that 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6.
def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers read from standard input.
#Overall this is what the function does:The function reads a line of space-separated integers from standard input, converts them to a list of integers, and returns this list.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three lines: the first line contains two integers n and m such that 3 ≤ n ≤ m ≤ min(\frac{n\cdot(n - 1)}{2}, 2 \cdot 10^5), the second line contains m lines with three integers u, v, and w representing an edge between vertices u and v with weight w, and it is guaranteed that there is at most one edge between each pair of vertices and the graph does not contain loops.
def func_5():
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings, each string representing a line from the standard input, split by whitespace. The first line of the input contains two integers n and m, and subsequent lines contain edges represented by three integers u, v, and w.
#Overall this is what the function does:The function reads input from the standard input, splits each line by whitespace, and returns a list of these strings. The list contains the first line with two integers n and m, followed by lines each containing three integers u, v, and w representing edges in a graph.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the graph, m is an integer representing the number of edges in the graph, and graph is a dictionary representing the adjacency list of the graph where each key is a vertex and its value is a list of tuples containing adjacent vertices and their corresponding edge weights. Additionally, edges is a list of tuples where each tuple contains the weight of an edge and the two vertices it connects.
def func_6():
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: Output State: `n` vertices in the graph, `m` edges in the graph, `edges` is a list containing `m` tuples, each tuple consisting of a weight `w` and two vertices `u` and `v` which represent an undirected edge between `u` and `v` in the graph. The graph dictionary `graph` has `n` keys, each corresponding to a vertex, and the value for each key is a list of vertices that are connected to it by an edge.
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
        
    #State: _min_edge is the minimum weight of the edges that form a cycle, node_u and node_v are the nodes involved in the cycle with the minimum weight edge.
    colors = [0] * (n + 1)
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    #This is printed: _min_edge, len(res) (where _min_edge is the minimum weight of the edges that form a cycle and len(res) is the number of nodes in the cycle formed by the dfs traversal)
    print(*res)
    #This is printed: node_u node_v (or any sequence of nodes forming the cycle, including node_u and node_v)
#Overall this is what the function does:The function processes an undirected graph represented by its number of vertices (`n`), number of edges (`m`), and adjacency list (`graph`). It then finds the minimum-weight cycle in the graph using a union-find data structure and depth-first search (DFS). Finally, it prints the weight of the minimum-weight cycle and the nodes involved in this cycle.

#State of the program right berfore the function call: curr is an integer representing the current vertex, parent is an integer representing the parent vertex in the DFS traversal, and path is a list representing the current path being explored.
def dfs(curr, parent, path):
    if (colors[curr] == 1) :
        return path
        #The program returns the list 'path' which represents the current path being explored during the DFS traversal and includes the current vertex 'curr' whose color is 1 and its parent vertex 'parent'.
    #State: curr is an integer representing the current vertex, parent is an integer representing the parent vertex in the DFS traversal, and path is a list representing the current path being explored. The color of the current vertex is not 1.
    colors[curr] = 1
    path.append(curr)
    for nei in graph[curr]:
        if colors[nei] != 2 and nei != parent:
            res = dfs(nei, curr, path)
            set_res = set(res)
            if res and node_v in set_res:
                return res
        
    #State: Output State: `colors` remains unchanged with `colors[curr]` set to 1, `curr` and `parent` remain unchanged with their respective values, `path` contains the current path being explored including `curr`.
    #
    #This means that the `colors` dictionary and `curr`, `parent` variables retain their initial values, and the `path` list includes the current vertex `curr` after the loop has executed all its iterations. The loop does not modify these variables outside of its own scope.
    colors[curr] = 2
    return []
    #The program returns an empty list
#Overall this is what the function does:The function `dfs` performs a depth-first search traversal on a graph. It accepts three parameters: `curr` (the current vertex), `parent` (the parent vertex in the DFS traversal), and `path` (a list representing the current path being explored). The function returns the list `path` if the current vertex `curr` has been visited (color 1) and is part of the path, otherwise it returns an empty list.

#State of the program right berfore the function call: test_cases is an integer such that 1 ≤ test_cases ≤ 10^4. Each test case consists of two integers n and m such that 3 ≤ n ≤ m ≤ min(⌊n⋅(n - 1)/2⌋, 2⋅10^5), followed by m lines, each containing three integers u, v, and w representing an edge between vertices u and v with weight w, where 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6.
def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: Output State: `test_cases` is an integer such that 0 ≤ `test_cases` ≤ 10^4, and for each iteration from 0 to `test_cases` - 1, `func_6()` has been executed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( m \), where \( 3 \leq n \leq m \leq \left\lfloor \frac{n \cdot (n - 1)}{2} \right\rfloor \) and \( m \leq 2 \times 10^5 \). For each test case, it reads \( m \) lines, each containing three integers \( u \), \( v \), and \( w \), representing an edge between vertices \( u \) and \( v \) with weight \( w \), where \( 1 \leq u, v \leq n \), \( u \neq v \), and \( 1 \leq w \leq 10^6 \). The function does not return any specific value but processes the input data according to the specified structure.

