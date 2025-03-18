#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of the following: n and m are integers such that 3 ≤ n ≤ m ≤ min(⌊n⋅(n−1)/2⌋, 2⋅10^5); u, v, and w are integers such that 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6.
def func_1():
    return int(sys.stdin.readline().strip())
    #The program reads an integer from standard input, strips any trailing whitespace, and returns it as an integer.
#Overall this is what the function does:The function reads an integer from standard input, removes any trailing whitespace, and returns it as an integer.

#State of the program right berfore the function call: None of the variables in the provided function `func_2()` are mentioned in the problem description or used within the function itself. The function simply reads a line from standard input and returns it stripped of leading and trailing whitespace. Therefore, no specific precondition can be derived from the function's signature or body alone.
def func_2():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips leading and trailing whitespace, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes any leading and trailing whitespace, and returns the modified line.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 3 ≤ n ≤ m ≤ min(⌊n(n - 1)/2⌋, 2 ⋅ 10^5), and for each edge, u, v, and w are integers such that 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6.
def func_3():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a tuple of integers read from the standard input.
#Overall this is what the function does:The function reads a line of input from the standard input, splits it into individual integers, and returns them as a tuple. This tuple contains the integers provided as input.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of n and m, where 3 ≤ n ≤ m ≤ min(⌊n(n - 1)/2⌋, 2⋅10^5), and m lines describing the edges with u, v, and w representing the vertices and the weight of the edge respectively, where 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6.
def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers read from the standard input, split by spaces and converted to integers.
#Overall this is what the function does:The function reads a line of input from the standard input, splits it into integers based on spaces, and returns them as a list. This list contains integers that represent some form of input data, such as test case parameters or edge weights in a graph.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 3 ≤ n ≤ m ≤ min(⌊n⋅(n−1)/2⌋, 2⋅10^5), and u, v, and w are integers such that 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6.
def func_5():
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings read from standard input, stripped of any trailing whitespace, and split on whitespace boundaries.
#Overall this is what the function does:The function reads a line of input from the standard input, strips any trailing whitespace, splits the line into a list of strings based on whitespace boundaries, and returns this list.

#State of the program right berfore the function call: (n, m) is a tuple of integers where 3 ≤ n ≤ m ≤ min(⌊n(n - 1)/2⌋, 2 ⋅ 10^5), edges is a list of tuples where each tuple contains three integers (u, v, w) representing an edge between vertices u and v with weight w, and DSU is a Disjoint Set Union data structure initialized with n + 1 elements.
def func_6():
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: After the loop executes all its iterations, `graph[u]` will include all vertices `v` connected to `u` through the edges added by the loop, `graph[v]` will include all vertices `u` connected to `v` through the edges added by the loop, `w` will be the weight of the last edge added, `edges` will contain tuples `(w, u, v)` for each edge added during the loop's iterations, `i` will be equal to `m - 1`, and `u`, `v`, and `w` will be the values returned by `func_3()` in the last iteration.
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
        
    #State: Output State: All nodes in the DSU structure are merged into connected components based on the edges processed. The variable `parent_u` and `parent_v` represent the root of each node `u` and `v` respectively, after all union operations have been performed. The variable `_min_edge` retains its value from the last iteration since no further updates occurred during the remaining iterations. The variable `w`, `u`, and `v` hold the values from the last tuple processed in `edges`. The `dsu` object reflects the final disjoint set structure where all connected components are formed, and the `parent` array within `dsu` shows the ultimate parent of each node.
    #
    #In simpler terms, after all iterations of the loop, all nodes that are connected through the edges in `edges` will be part of the same connected component in the DSU structure. The `_min_edge` value will stay the same as it was after the third iteration, indicating that no further updates to the minimum edge weight in any component were necessary. The `w`, `u`, and `v` variables will reflect the last edge processed, and the `dsu` object will show the fully connected graph with all nodes merged into their respective components.
    colors = [0] * (n + 1)
    res = dfs(node_u, -1, [])
    print(_min_edge, len(res))
    #This is printed: _min_edge, n+1
    print(*res)
    #This is printed: the sequence of nodes visited during the DFS traversal starting from node u and excluding the parent node -1
#Overall this is what the function does:The function processes a graph represented by vertices and weighted edges using a Disjoint Set Union (DSU) data structure to find the minimum edge weight among all connected components. It then performs a depth-first search (DFS) starting from a specified node to determine the size of the connected component containing that node. Finally, it prints the minimum edge weight found and the sequence of nodes visited during the DFS traversal.

#State of the program right berfore the function call: curr is an integer representing the current vertex being visited, parent is an integer representing the previously visited vertex, and path is a list representing the current path of vertices being explored.
def dfs(curr, parent, path):
    if (colors[curr] == 1) :
        return path
        #The program returns the list 'path' which represents the current path of vertices being explored.
    #State: curr is an integer representing the current vertex being visited, parent is an integer representing the previously visited vertex, and path is a list representing the current path of vertices being explored. The color of the current vertex `curr` is not 1.
    colors[curr] = 1
    path.append(curr)
    for nei in graph[curr]:
        if colors[nei] != 2 and nei != parent:
            res = dfs(nei, curr, path)
            set_res = set(res)
            if res and node_v in set_res:
                return res
        
    #State: Output State: `colors[curr]` is set to 1, `curr` is an integer representing the current vertex being visited, `parent` is an integer representing the previously visited vertex, `path` is a list representing the final path of vertices being explored, which includes all vertices that were part of the path during the entire execution of the loop, `res` is a set containing the elements of the original `res` list, and `set_res` is the set created from `res`. If any neighbor `nei` of the current vertex `curr` was not colored 2, not equal to `parent`, and `node_v` was in `set_res` when `res` was not empty, the function would have returned a set containing the elements of the original `res` list. Since the loop has executed all its iterations without returning, the function will return None.
    colors[curr] = 2
    return []
    #The program returns an empty list
#Overall this is what the function does:The function `dfs` performs a depth-first search (DFS) on a graph starting from a given vertex `curr`. It accepts three parameters: `curr` (the current vertex being visited), `parent` (the previously visited vertex), and `path` (the current path of vertices being explored). The function returns one of the following:
- A list `path` representing the current path of vertices being explored.
- A non-empty list `res` containing elements found during the DFS traversal, if `node_v` is present in this list.
- The result of the DFS function call for a neighbor `nei` of the current vertex `curr`, if `nei` is not colored 2, not equal to `parent`, and either `res` is empty or `nei` is not in `set_res`.
- A set containing the elements of the original `res` list.
- An empty list, if no valid path or result is found.

#State of the program right berfore the function call: test_cases is an integer such that 1 ≤ test_cases ≤ 10^4. Each test case consists of n and m (3 ≤ n ≤ m ≤ min(⌊n⋅(n - 1)/2⌋, 2⋅10^5)), followed by m lines of three integers u, v, and w (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 10^6), representing the vertices and the weight of the edge between them.
def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: Output State: `test_cases` must be greater than 0.
    #
    #Natural Language Explanation: After the loop has executed all its iterations, the value of `test_cases` must still be greater than 0. This is because the loop continues as long as `test_cases` is greater than 0, and there is no operation within the loop that changes the value of `test_cases`. Therefore, if the loop runs for all its iterations without `test_cases` becoming less than or equal to 0, it means `test_cases` remains greater than 0 at the end.
#Overall this is what the function does:The function processes multiple test cases, where each test case involves two integers \( n \) and \( m \) (with \( 3 \leq n \leq m \leq \min(\lfloor n \cdot (n - 1)/2 \rfloor, 2 \cdot 10^5) \)), followed by \( m \) lines of three integers \( u \), \( v \), and \( w \) (with \( 1 \leq u, v \leq n \), \( u \neq v \), and \( 1 \leq w \leq 10^6 \)). The function reads these inputs and processes them for each test case. The function does not return any specific value but ensures that the number of test cases remains greater than 0 after processing all test cases.

