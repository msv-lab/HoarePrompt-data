#State of the program right berfore the function call: None
def func_1():
    return int(sys.stdin.readline().strip())
    #The program returns an integer value read from the standard input (stdin), which is the user's input after any leading or trailing whitespace has been removed.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads a line of input from the standard input (stdin), strips any leading or trailing whitespace, converts the resulting string to an integer, and returns this integer value.

#State of the program right berfore the function call: None. This function does not take any parameters.
def func_2():
    return sys.stdin.readline().strip()
    #The program returns the first line of input from the user, with leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads the first line of input from the user, removes any leading and trailing whitespace, and returns this modified line. The function leaves no lasting impact on the program state beyond the returned value.

#State of the program right berfore the function call: None. This function does not take any parameters and reads input from stdin, assuming the input format is correctly provided according to the problem description.
def func_3():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object that converts each element from the input line (read from stdin) into an integer, where the input line consists of space-separated values.
#Overall this is what the function does:Reads a line of space-separated values from standard input, converts each value to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: None. This function does not take any parameters and reads input from stdin, expecting a line of space-separated integers.
def func_4():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers read from the standard input (stdin), where each integer was originally provided as a space-separated value on a single line.
#Overall this is what the function does:The function `func_4` reads a line of space-separated integers from the standard input (stdin) and returns them as a list of integers. It does not accept any parameters. After the function concludes, the program state includes a list of integers derived from the input line.

#State of the program right berfore the function call: None of the variables are passed as arguments to the function `func_5`. This function reads a line from standard input and returns it as a list of strings.
def func_5():
    return list(sys.stdin.readline().strip().split())
    #The program returns a list of strings obtained by reading a line from standard input, stripping any leading or trailing whitespace, and splitting the line into words.
#Overall this is what the function does:Reads a line from standard input, removes any leading or trailing whitespace, splits the line into words, and returns a list of these words.

#State of the program right berfore the function call: n and m are positive integers representing the number of vertices and edges in the graph, respectively, such that 3 ≤ n ≤ m ≤ min(n*(n-1)/2, 2*10^5). edges is a list of tuples (w, u, v) where w is a positive integer representing the weight of the edge, and u, v are integers representing the vertices connected by the edge, with 1 ≤ u, v ≤ n and u ≠ v.
def func_6():
    n, m = func_3()
    graph = defaultdict(list)
    edges = []
    for i in range(m):
        u, v, w = func_3()
        
        graph[u].append(v)
        
        graph[v].append(u)
        
        edges.append((w, u, v))
        
    #State: After the loop executes all the iterations, `n` and `m` are positive integers such that 3 ≤ n ≤ m ≤ min(n*(n-1)/2, 2*10^5). The `edges` list contains `m` tuples, each of the form `(w, u, v)`, where `u`, `v`, and `w` are the values returned by `func_3()` during each iteration. The `graph` is a defaultdict of lists, where each key `u` has a list of length equal to the number of times `u` was used as a vertex in the edges added to the graph. The index `i` is `m - 1`, indicating that the loop has completed all `m` iterations.
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
        
    #State: After all iterations of the loop, `n` and `m` remain positive integers such that 3 ≤ n ≤ m ≤ min(n*(n-1)/2, 2*10^5). The `edges` list is still a list of `m` tuples sorted in descending order by the first element of each tuple (weight `w`). The `graph` remains a defaultdict of lists, and `i` is 0. The `dsu` instance is updated to reflect the final connected components formed by the union operations. If any two vertices `u` and `v` were found to be in the same component before being unioned, `_min_edge` will be the smallest weight `w` of such an edge, and `start` and `end` will be the corresponding vertices `u` and `v`. Otherwise, `_min_edge` remains infinity, `start` remains -1, and `end` remains -1.
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
        
    #State: After all iterations, `node` will be the last processed node from `que` or `end` if it was reached, and `que` will be empty. The `prev` dictionary will have entries for all nodes that were reachable from `start` and not previously in `prev`, mapping each node to its predecessor in the path. If `end` was reached, the loop will have terminated early when `node` became `end`. All other variables (`n`, `m`, `edges`, `graph`, `i`, `dsu`, `_min_edge`, `start`, `end`) remain unchanged.
    path = []
    curr = end
    while curr != -1:
        path.append(curr)
        
        curr = prev[curr]
        
    #State: After all iterations, `node` will be the last processed node from `que` or `end` if it was reached, and `que` will be empty. The `prev` dictionary will have entries for all nodes that were reachable from `start` and not previously in `prev`, mapping each node to its predecessor in the path. If `end` was reached, the loop will have terminated early when `node` became `end`. All other variables (`n`, `m`, `edges`, `graph`, `i`, `dsu`, `_min_edge`, `start`, `end`) remain unchanged. `path` is now a list containing the full path from `end` back to `start` (or the first node in the path that has no predecessor), with each element being a node in the path. `curr` is set to `-1`, indicating that the loop has completed and no more predecessors can be found.
    print(_min_edge, len(path))
    #This is printed: _min_edge, len(path) (where _min_edge is the value of _min_edge and len(path) is the number of nodes in the path from end back to start)
    print(*path[::-1])
    #This is printed: [start, ..., end] (where [start, ..., end] is the list of nodes from start to end in the path)
#Overall this is what the function does:The function `func_6` constructs a graph from a given number of vertices `n` and edges `m`, where each edge is represented by a tuple `(w, u, v)` indicating the weight `w` and the vertices `u` and `v` it connects. It then sorts these edges in descending order by weight and uses a Disjoint Set Union (DSU) data structure to find the minimum weight cycle in the graph. If a cycle is found, it identifies the minimum weight edge in the cycle and the path forming the cycle. Finally, it prints the minimum weight of the cycle, the length of the cycle path, and the nodes in the cycle path in reverse order. If no cycle is found, it prints the minimum weight as infinity and an empty path.

#State of the program right berfore the function call: No variables are passed to the function `func_7`. This function is designed to handle the overall process of reading test cases and processing each one, likely calling other functions (`func_1` and `func_6`) to manage the input and computation for each test case.
def func_7():
    test_cases = func_1()
    for _ in range(test_cases):
        func_6()
        
    #State: `test_cases` must be greater than or equal to 0 (it was originally greater than 0 and has been decremented by the number of iterations), `func_6()` has been called `test_cases` times.
#Overall this is what the function does:The function `func_7` does not accept any parameters. It reads a number of test cases using `func_1`, and then iterates over this number, calling `func_6` for each test case. After the function completes, the number of times `func_6` has been called is equal to the number of test cases initially read by `func_1`. The function does not return any value.

