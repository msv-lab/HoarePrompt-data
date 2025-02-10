#State of the program right berfore the function call: None
def func_1():
    return int(sys.stdin.readline().strip())
    #The program reads a line from standard input, strips any leading or trailing whitespace, converts the resulting string to an integer, and returns this integer.
#Overall this is what the function does:Reads a line from standard input, removes any leading or trailing whitespace, converts the result to an integer, and returns this integer.

#State of the program right berfore the function call: None of the variables are passed to the function `func_2`. This function reads a line from standard input and returns it stripped of leading and trailing whitespace.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns a string that is read from standard input, stripped of any leading and trailing whitespace.
#Overall this is what the function does:Reads a line from standard input and returns it as a string, stripped of any leading and trailing whitespace.

#State of the program right berfore the function call: None
def func_3():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns an iterator that yields integer values from the input provided through standard input (stdin), where each value is separated by whitespace.
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns an iterator that yields integer values from the input provided through standard input (stdin), where each value is separated by whitespace. The function reads a single line of input, splits it into parts based on whitespace, converts each part to an integer, and returns an iterator over these integers.

#State of the program right berfore the function call: None
def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers read from the standard input, where each integer is separated by whitespace.
#Overall this is what the function does:Reads a line from the standard input, splits the line into substrings based on whitespace, converts each substring into an integer, and returns a list of these integers.

#State of the program right berfore the function call: None of the variables are passed as arguments to the function `func_5`. This function reads a line from standard input, strips leading and trailing whitespace, splits the line into a list of strings, and returns this list.
def func_5():
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings obtained by reading a line from standard input, stripping leading and trailing whitespace, and splitting the line into a list.
#Overall this is what the function does:Reads a line from standard input, removes any leading and trailing whitespace, splits the line into a list of strings based on whitespace, and returns this list.

#State of the program right berfore the function call: n and m are integers such that 3 ≤ n ≤ m ≤ min(n*(n - 1)/2, 2 * 10^5), and edges is a list of tuples (w, u, v) where w is an integer representing the weight of the edge, and u, v are integers representing the vertices connected by the edge, with 1 ≤ u, v ≤ n and u ≠ v.
def func_6():
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: After all iterations of the loop, `n` and `m` are updated to the values returned by `func_3()`, `edges` is a list containing `m` tuples of the form `(w, u, v)`, `graph` is a defaultdict of type list where each key `u` has a list of all `v` values that were appended during the loop, and each key `v` has a list of all `u` values that were appended during the loop. The value of `m` must be greater than or equal to the number of iterations, and `i` is `m-1`. For each iteration, `u`, `v`, and `w` are assigned the values returned by `func_3()`.
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
        
    #State: After all iterations of the loop, `n` and `m` are updated to the values returned by `func_3()`, `edges` is a list containing `m` tuples of the form `(w, u, v)` sorted in descending order based on the first element `w`, `graph` is a defaultdict of type list where each key `u` has a list of all `v` values that were appended during the loop, and each key `v` has a list of all `u` values that were appended during the loop. The value of `m` is greater than or equal to the number of iterations, and `i` is `m-1`. A new instance of the `DSU` class is created with the size `n + 1` and assigned to the variable `dsu`. `_min_edge` is set to the smallest weight `w` of any edge `(w, u, v)` where `u` and `v` had the same parent before the union operation, or it remains set to infinity (`float('inf')`) if no such edge exists. `start` is set to the `u` value of the edge with the smallest `w` where `u` and `v` had the same parent, or it remains set to -1 if no such edge exists. `end` is set to the `v` value of the edge with the smallest `w` where `u` and `v` had the same parent, or it remains set to -1 if no such edge exists. All nodes `u` and `v` that were processed in the loop are now in the same connected component according to the `dsu` structure.
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
        
    #State: The loop has processed all nodes in the `que` until it either finds the `end` node or exhausts the queue. The `prev` dictionary contains all nodes that have been visited along with their respective predecessors, forming a path from the `start` node to the `end` node if such a path exists. The `que` is empty, indicating that all reachable nodes have been processed. The `node` variable holds the value of the last node that was processed from the front of `que`. If the `end` node was found, the loop terminated early when `node` became equal to `end`. If the `end` node was not found, the loop terminated because the `que` became empty.
    path = []
    curr = end
    while curr != -1:
        path.append(curr)
        
        curr = prev[curr]
        
    #State: The loop has processed all nodes in the `que` until it either finds the `end` node or exhausts the queue. The `prev` dictionary contains all nodes that have been visited along with their respective predecessors, forming a path from the `start` node to the `end` node if such a path exists. The `que` is empty, indicating that all reachable nodes have been processed. The `node` variable holds the value of the last node that was processed from the front of `que`. If the `end` node was found, the loop terminated early when `node` became equal to `end`. If the `end` node was not found, the loop terminated because the `que` became empty. `path` is a list containing the full path from the `end` node back to the `start` node, in reverse order. `curr` is now equal to `-1`, indicating that the loop has completed and the entire path has been reconstructed.
    print(_min_edge, len(path))
    #This is printed: _min_edge, len(path) (where _min_edge is the value of the minimum edge weight encountered, and len(path) is the number of nodes in the path from the end node back to the start node)
    print(*path[::-1])
    #This is printed: (nothing printed)
#Overall this is what the function does:The function `func_6` constructs a graph from a given set of edges and finds the minimum weight cycle in the graph. It takes no explicit parameters but internally uses `func_3` to read the number of vertices `n`, the number of edges `m`, and the edges themselves. The function then creates a graph representation using a defaultdict and a list of edges. It sorts the edges in descending order by weight and uses a Disjoint Set Union (DSU) structure to find the minimum weight cycle. If a cycle is found, it determines the start and end nodes of the cycle and reconstructs the path. Finally, it prints the minimum edge weight in the cycle and the length of the path, followed by the nodes in the path in reverse order. If no cycle is found, it prints the minimum edge weight as infinity and an empty path.

#State of the program right berfore the function call: No variables are passed to the function `func_7`.
def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` must be greater than or equal to the number of iterations the loop has completed, and `func_6()` has been executed the same number of times as the loop has iterated.
#Overall this is what the function does:The function `func_7` does not accept any parameters and does not return any value. It calls `func_1` to determine the number of test cases, then iterates this many times, calling `func_6` in each iteration. After the function completes, `func_6` will have been called a number of times equal to the value returned by `func_1`.

