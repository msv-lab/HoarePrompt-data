#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of integers n and m such that 3 ≤ n ≤ m ≤ min(\frac{n\cdot(n - 1)}{2}, 2 \cdot 10^5), and m lines describing the edges of the graph with vertices u, v, and their weight w (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 10^6).
def func_1():
    return int(sys.stdin.readline().strip())
    #The program reads an integer from standard input, strips any trailing whitespace, and returns it as an integer.
#Overall this is what the function does:The function reads an integer from standard input, removes any trailing whitespace, and returns it as an integer.

#State of the program right berfore the function call: None of the variables in the provided function signature are present in the given code snippet. The function `func_2` reads a single line from standard input and returns it after stripping any trailing whitespace, but it does not take any arguments.
def func_2():
    return sys.stdin.readline().strip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns the modified line.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three lines: the first line contains two integers n and m such that 3 ≤ n ≤ m ≤ min(⌊n⋅(n - 1)/2⌋, 2⋅10^5); the second line contains m lines, each with three integers u, v, and w such that 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6 representing an edge between vertices u and v with weight w; and the input format guarantees that there is at most one edge between each pair of vertices and the graph is not necessarily connected.
def func_3():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a tuple of two integers (n, m) read from the standard input.
#Overall this is what the function does:The function reads two integers (n, m) from the standard input and returns them as a tuple. This function does not accept any parameters and ensures that the values of n and m meet specific constraints before returning them.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 3 ≤ n ≤ m ≤ min(⌊n⋅(n - 1)/2⌋, 2⋅10^5), and u, v, and w are integers such that 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6.
def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers read from standard input. The list contains three integers: u, v, and w, separated by spaces.
#Overall this is what the function does:The function reads three integers (u, v, and w) from standard input, where u and v are between 1 and n, u ≠ v, and w is between 1 and 10^6. It then returns a list containing these three integers.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 3 ≤ n ≤ m ≤ min(⌊n(n - 1)/2⌋, 2 ⋅ 10^5), and u, v, and w are integers such that 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6.
def func_5():
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings containing the input from the standard input, stripped of any trailing whitespace and split by whitespace.
#Overall this is what the function does:The function reads a line of input from the standard input, strips any trailing whitespace, splits the line into a list of strings based on whitespace, and returns this list.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 3 ≤ n ≤ m ≤ min(⌊n⋅(n - 1)/2⌋, 2⋅10^5), and u, v, and w are integers such that 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6. The graph is represented by a dictionary `graph` where `graph[u]` is a list of tuples `(v, w)` representing edges from vertex u to vertex v with weight w. The variable `dsu` is an instance of a Disjoint Set Union (DSU) data structure initialized with n+1 sets. The variable `edges` is a list of tuples sorted in reverse order by weight, where each tuple contains (w, u, v).
def func_6():
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: After the loop executes all its iterations, `m` will be equal to the total number of iterations performed; `graph[v]` will include all `u` values returned by `func_3()` for each iteration; `edges` will contain tuples `(w, u, v)` for each iteration, where `w` is the weight, `u` is the source vertex, and `v` is the destination vertex; `u` and `v` will be the last two values returned by `func_3()` during the loop's final iteration; `w` will be the weight of the edge corresponding to the last call to `func_3()` during the loop's final iteration.
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
        
    #State: All nodes have been processed through the union-find operations, and the variables `_min_edge`, `start`, and `end` reflect the minimum edge that causes a cycle in the graph, along with the nodes involved in that cycle.
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
        
    #State: Output State: The deque `que` will contain all nodes that can be reached from the starting node `start` to the ending node `end`, forming the shortest path from `start` to `end` if such a path exists. If multiple paths exist, `que` will contain one such path. The dictionary `prev` will store the predecessor of each node in this path, except for the starting node `start`, which will have a value of `-1` in `prev`.
    #
    #In simpler terms, `que` will hold a list of nodes representing the shortest path from the starting node to the ending node, and `prev` will map each node in this path (except the start node) to its immediate predecessor in the path.
    path = []
    curr = end
    while curr != -1:
        path.append(curr)
        
        curr = prev[curr]
        
    #State: Output State: `que` is a deque containing the shortest path from `start` to `end`, `prev` is a dictionary mapping each node in this path (except `start`) to its immediate predecessor, `path` is a list containing the full shortest path from `start` to `end`, and `curr` is `-1`.
    #
    #Explanation: After the loop completes all its iterations, `curr` will eventually become `-1` because the loop continues as long as `curr` is not equal to `-1`. During each iteration of the loop, `curr` is set to the immediate predecessor of its current value in the path, and `curr` is appended to the `path` list. This process continues until `curr` reaches `start`, at which point the loop terminates. At this point, `path` contains the full shortest path from `start` to `end`, and `curr` is set to `-1`. The `que` and `prev` variables remain unchanged as they are not affected by the loop.
    print(_min_edge, len(path))
    #This is printed: _min_edge, len(path)
    print(*path[::-1])
    #This is printed: the full shortest path from end to start, with nodes separated by spaces
#Overall this is what the function does:The function processes a weighted graph defined by a series of edges and determines if there is a path between two specified vertices for each test case. It first sorts the edges by weight in descending order and uses a Disjoint Set Union (DSU) data structure to find the minimum weight edge that forms a cycle when added to the graph. If such an edge is found, it identifies the nodes involved in the cycle. Then, it performs a breadth-first search (BFS) to find the shortest path between the two specified vertices. Finally, it prints the weight of the minimum edge causing a cycle and the length of the shortest path, followed by the shortest path itself in reverse order.

#State of the program right berfore the function call: test_cases is a positive integer representing the number of test cases. For each test case, n and m are integers such that 3 ≤ n ≤ m ≤ min(⌊n(n - 1)/2⌋, 2 * 10^5), and m represents the number of edges in the graph. Each of the next m lines contains three integers u, v, and w representing an edge between vertices u and v with weight w, where 1 ≤ u, v ≤ n, u ≠ v, and 1 ≤ w ≤ 10^6. It is guaranteed that there is at most one edge between each pair of vertices and the graph is not necessarily connected.
def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: Output State: `test_cases` must be a positive integer, `_` is equal to `test_cases - 1`, and the function `func_6()` has been called `test_cases` times.
    #
    #In natural language: After the loop has executed all its iterations, `test_cases` must still be a positive integer (since it started as one and hasn't been modified inside the loop), the loop variable `_` will be equal to `test_cases - 1` (as it increments with each iteration), and the function `func_6()` will have been called exactly `test_cases` times.
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it accepts integers n and m representing the number of vertices and edges in a graph, respectively. It then accepts m lines of input, each containing three integers u, v, and w representing an edge between vertices u and v with weight w. The function calls another function `func_6()` for each test case, but does not return any value itself. After processing all test cases, the function ensures that `test_cases` remains a positive integer and that `func_6()` has been called exactly `test_cases` times.

