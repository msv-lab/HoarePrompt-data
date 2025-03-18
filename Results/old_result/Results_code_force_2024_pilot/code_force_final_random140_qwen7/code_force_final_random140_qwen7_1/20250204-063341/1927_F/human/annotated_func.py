#State of the program right berfore the function call: None of the variables in the provided function signature are used in the given code snippet. The function `func_1` reads an integer from standard input but does not use any variables related to the problem description.
def func_1():
    return int(sys.stdin.readline().strip())
    #The program returns an integer read from standard input and stripped of leading and trailing whitespace.
#Overall this is what the function does:The function `func_1` reads an integer from standard input, strips any leading or trailing whitespace from the input, and returns this integer.

#State of the program right berfore the function call: None of the variables in the provided function signature are present in the given function `func_2()`. The function reads a line from standard input and returns it after stripping any trailing whitespace.
def func_2():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns the resulting string.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 3 ≤ n ≤ m ≤ min(⌊n(n - 1)/2⌋, 2 ⋅ 10^5), and u, v, and w are integers such that 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6.
def func_3():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns an integer tuple (t, n, m, u, v, w) read from standard input.
#Overall this is what the function does:The function reads an integer tuple (t, n, m, u, v, w) from standard input, where t is between 1 and 10^4 inclusive, n and m satisfy 3 ≤ n ≤ m ≤ min(⌊n(n - 1)/2⌋, 2 ⋅ 10^5), and u, v, and w are within their respective bounds. It then returns this tuple.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 3 ≤ n ≤ m ≤ min(⌊n⋅(n - 1)/2⌋, 2⋅10^5), and the subsequent m lines contain three integers u, v, and w representing an edge between vertices u and v with weight w, where 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6.
def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers read from the standard input. The list contains three integers per line, representing an edge between vertices u and v with weight w.
#Overall this is what the function does:The function reads multiple lines of input from the standard input, each containing three integers representing an edge between vertices u and v with weight w. It then returns these inputs as a list of lists, where each inner list contains three integers.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of two integers n and m such that 3 ≤ n ≤ m ≤ min(⌊n⋅(n−1)/2⌋, 2⋅10^5), and m lines describing the edges of the graph, where each line contains three integers u, v, and w representing an edge between vertices u and v with weight w (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 10^6).
def func_5():
    return list(sys.stdin.readline().strip().split())
    #The program returns a list containing two integers n and m read from standard input, where 3 ≤ n ≤ m ≤ min(⌊n⋅(n−1)/2⌋, 2⋅10^5)
#Overall this is what the function does:The function reads two integers \( n \) and \( m \) from standard input, where \( 3 \leq n \leq m \leq \min(\lfloor n \cdot (n-1)/2 \rfloor, 2 \cdot 10^5) \), and returns a list containing these two integers.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the graph, m is an integer representing the number of edges in the graph, and graph is a dictionary where keys are vertices and values are lists of adjacent vertices. Additionally, edges is a list of tuples where each tuple contains the weight of the edge and the two vertices it connects.
def func_6():
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: Output State: The loop has executed all its iterations, meaning `i` is equal to `m-1`. At this point, `i` must still be less than `m`. The variable `u` will hold the value returned by `func_3()` on the last iteration, `v` will hold the value returned by `func_3()` on the last iteration, and `w` will hold the value returned by `func_3()` on the last iteration. The `graph` dictionary will have updated its adjacency lists such that for every edge added, both vertices `u` and `v` will have each other in their respective adjacency lists. The `edges` list will contain tuples `(w, u, v)` for each of the `m` edges added during the loop's iterations.
    #
    #In summary, the graph will be fully constructed with all `m` edges, and the `edges` list will contain all the weights and corresponding vertex pairs that were added during the loop's execution.
    edges.sort(reverse=True)
    dsu = DSU(n + 1)
    _min_edge = float('inf')
    start = -1
    end = -1
    for (w, u, v) in edges:
        parent_u = dsu.find(u)
        
        parent_v = dsu.find(v)
        
        if parent_u == parent_v:
            _min_edge = w
            start = u
            end = v
        else:
            dsu.union(u, v)
        
    #State: Output State: The loop has executed all iterations, meaning all `m` edges have been processed. At the end of the loop, `w` is the weight of the last edge processed, `u` is one endpoint of that edge, and `v` is the other endpoint. `parent_u` is the root of the component containing `u`, and `parent_v` is the root of the component containing `v`. If `parent_u` equals `parent_v`, then `_min_edge` is the weight of the last edge processed, `start` is `u`, and `end` is `v`. Otherwise, the union operation between `u` and `v` has been performed by `dsu.union(u, v)`, and the DSU structure reflects the union-find relationships among all nodes. The `edges` list is sorted in descending order based on the weights of the edges, and the `graph` dictionary reflects the final adjacency list structure of the graph after all edges have been added and union operations have been performed.
    que = deque([start])
    prev = {start: -1}
    while que:
        node = que.popleft()
        
        if node == end:
            break
        
        for nei in graph[node]:
            if node == start and nei == end:
                continue
            if nei not in prev:
                prev[nei] = node
                que.append(nei)
        
    #State: Output State: `que` is an empty deque, `node` is the last node processed before `que` became empty, and the dictionary `prev` contains the predecessors of all nodes that were processed in the graph, forming the shortest path tree rooted at `start`. If the final `node` equals `end`, the loop would have broken out of the most internal loop or if statement. All nodes reachable from `start` are now in `prev`, with each node pointing to the node that was traversed to reach it. The `graph` dictionary reflects the final adjacency list structure of the graph after all edges have been added and union operations have been performed.
    path = []
    curr = end
    while curr != -1:
        path.append(curr)
        
        curr = prev[curr]
        
    #State: Output State: `que` is an empty deque, `node` is the last node processed before `que` became empty, the dictionary `prev` contains the predecessors of all nodes that were processed in the graph, forming the shortest path tree rooted at `start`, `curr` is equal to `prev[curr]` until `curr` becomes `-1`, and `path` is a list containing the shortest path from `end` to `start` in reverse order.
    #
    #This means that after all iterations of the loop, `path` will contain the entire shortest path from the `end` node back to the `start` node, listed from the `end` node to the `start` node. The `curr` variable will eventually become `-1` when there are no more predecessors to trace back, indicating that the shortest path has been fully constructed in the `path` list.
    print(_min_edge, len(path))
    #This is printed: _min_edge, len(path)
    print(*path[::-1])
    #This is printed: the shortest path from end to start
#Overall this is what the function does:The function constructs a graph using the given number of vertices, edges, and adjacency information. It then sorts the edges in descending order of weight and uses a Disjoint Set Union (DSU) data structure to find a minimum spanning tree (MST). After constructing the MST, it performs a breadth-first search (BFS) to find the shortest path from a specified start node to an end node. Finally, it prints the weight of the last edge processed during MST construction and the length of the shortest path, followed by printing the shortest path itself in reverse order.

#State of the program right berfore the function call: test_cases is an integer such that 1 ≤ test_cases ≤ 10^4. Each test case consists of two integers n and m such that 3 ≤ n ≤ m ≤ min(⌊n⋅(n−1)/2⌋, 2⋅10^5), followed by m lines, each containing three integers u, v, and w such that 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6, representing an edge between vertices u and v with weight w.
def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: Output State: `test_cases` must be greater than or equal to 3.
    #
    #In natural language: After the loop has executed all its iterations, the value of `test_cases` must be at least 3. This is because the loop continues as long as `test_cases` is greater than 0, and we know it has run through at least 3 iterations, meaning `test_cases` was initially greater than or equal to 3 and has not been reduced below 3 during the loop's execution.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( m \), followed by \( m \) lines of input. Each line contains three integers \( u \), \( v \), and \( w \), representing an edge between vertices \( u \) and \( v \) with weight \( w \). The function iterates through all test cases, and after processing, ensures that the number of test cases is at least 3. The function does not return any value.

