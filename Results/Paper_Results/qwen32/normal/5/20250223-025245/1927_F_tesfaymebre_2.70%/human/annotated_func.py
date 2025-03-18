#State of the program right berfore the function call: No variables are present in the function signature. The function `func_1` does not take any parameters and is expected to read an integer from standard input.
def func_1():
    return int(sys.stdin.readline().strip())
    #The program returns an integer read from standard input.
#Overall this is what the function does:The function `func_1` reads an integer from standard input and returns that integer.

#State of the program right berfore the function call: This function does not use any parameters. It reads a single line from the standard input and returns it as a string, stripped of any leading or trailing whitespace.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns a string that is a single line read from the standard input, stripped of any leading or trailing whitespace.
#Overall this is what the function does:The function reads a single line from the standard input, removes any leading or trailing whitespace from the line, and returns the resulting string.

#State of the program right berfore the function call: No variables are present in the function signature, thus no precondition can be derived from it.
def func_3():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object containing integers that were read from the standard input, split by whitespace.
#Overall this is what the function does:The function `func_3` reads a line of input from the standard input, splits it into substrings based on whitespace, converts each substring into an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: No variables are present in the function signature of `func_4`. The function reads a line from standard input, strips any leading or trailing whitespace, splits the line into a list of substrings based on whitespace, and maps each substring to an integer, returning the resulting list of integers.
def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers that were read from standard input, stripped of any leading or trailing whitespace, and split by whitespace.
#Overall this is what the function does:The function `func_4` reads a line from standard input, removes any leading or trailing whitespace, splits the line into substrings based on whitespace, converts each substring to an integer, and returns the resulting list of integers.

#State of the program right berfore the function call: No variables in the function signature. The function `func_5` does not take any parameters and is expected to read from standard input.
def func_5():
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings, where each string is a substring from the line of input read from standard input, split by whitespace.
#Overall this is what the function does:The function `func_5` reads a line of input from standard input, splits the line into substrings based on whitespace, and returns a list of these substrings.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the graph, m is an integer representing the number of edges in the graph, such that 3 <= n <= m <= min(n*(n-1)/2, 2*10^5).
def func_6():
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: `n` and `m` are the values returned by `func_3()` such that \(3 \leq n \leq m \leq \min\left(\frac{n(n-1)}{2}, 2 \times 10^5\right)\); `graph` is a defaultdict with list as the default factory and contains all the edges added during the loop; `edges` is a list containing all the tuples `(w, u, v)` added during the loop; `i` is equal to `m` after the loop completes, indicating all iterations have finished; `u`, `v`, and `w` are the values returned by `func_3()` in the last iteration of the loop.
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
        
    #State: `n` and `m` are the values returned by `func_3()` such that \(3 \leq n \leq m \leq \min\left(\frac{n(n-1)}{2}, 2 \times 10^5\right)\); `graph` is a defaultdict with list as the default factory and contains all the edges added during the loop; `edges` is a list containing all the tuples `(w, u, v)` added during the loop, sorted in descending order by `w`; `i` is equal to `m` after the loop completes; `u`, `v`, and `w` are the values returned by `func_3()` in the last iteration of the loop; `dsu` is an instance of the DSU class initialized with `n + 1` elements and reflects all the unions performed during the loop; `_min_edge` is the minimum edge weight in the final connected component; `node_u` and `node_v` are the nodes of the edge with `_min_edge` weight in the final connected component.
    colors = [0] * (n + 1)
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    #This is printed: _min_edge, len(res) (where _min_edge is the minimum edge weight in the final connected component, and len(res) is the number of nodes in the connected component that includes node_u)
    print(*res)
    #This is printed: res (where res is the result of the DFS traversal starting from node_u in the graph)
#Overall this is what the function does:The function constructs a graph with `n` vertices and `m` edges, sorts the edges by weight in descending order, and uses a Disjoint Set Union (DSU) data structure to find a connected component. It identifies the minimum edge weight in this component and performs a Depth-First Search (DFS) starting from one of the nodes of this minimum edge. The function prints the minimum edge weight, the number of nodes in the connected component, and the nodes themselves.

#State of the program right berfore the function call: curr is an integer representing the current vertex, parent is an integer representing the parent vertex of the current vertex, and path is a list of integers representing the current path in the Depth-First Search (DFS) traversal.
def dfs(curr, parent, path):
    if (colors[curr] == 1) :
        return path
        #The program returns the list 'path' which represents the current path in the Depth-First Search (DFS) traversal.
    #State: `curr` is an integer representing the current vertex, `parent` is an integer representing the parent vertex of the current vertex, and `path` is a list of integers representing the current path in the Depth-First Search (DFS) traversal. The color of the current vertex `curr` is not equal to 1.
    colors[curr] = 1
    path.append(curr)
    for nei in graph[curr]:
        if colors[nei] != 2 and nei != parent:
            res = dfs(nei, curr, path)
            set_res = set(res)
            if res and node_v in set_res:
                return res
        
    #State: `curr` is an integer representing the current vertex, `parent` is an integer representing the parent vertex of the current vertex, `path` is a list of integers representing the current path in the DFS traversal including `curr`. The color of the current vertex `curr` is 1. No result containing `node_v` was found in any of the recursive calls, so the function does not return anything.
    colors[curr] = 2
    return []
    #The program returns an empty list.
#Overall this is what the function does:The function `dfs` performs a Depth-First Search (DFS) traversal starting from a given vertex `curr`. It keeps track of the traversal path and uses a color array to mark visited vertices. If it detects a cycle containing a specific node `node_v`, it returns the path of that cycle. If no such cycle is found, it returns an empty list.

#State of the program right berfore the function call: test_cases is an integer representing the number of test cases, where 1 <= test_cases <= 10^4.
def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` is the value returned by `func_1()` and remains unchanged after all iterations of the loop.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It retrieves the number of test cases by calling `func_1()`, then iterates that many times, calling `func_6()` in each iteration. The function does not return any specific value and the final state is determined by the side effects of `func_6()`.

