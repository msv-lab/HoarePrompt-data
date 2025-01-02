#State of the program right berfore the function call: graph is a list of lists representing an undirected graph where graph[i] contains all the indices of nodes connected to node i. start is an integer representing the starting node, which is 0 (Room 1 in the problem context).
def func_1(graph, start):
    used = [False] * len(graph)
    used[start] = True
    q = [start]
    depth = [-1] * len(graph)
    post = [-1] * len(graph)
    depth[0] = 0
    for v in q:
        for w in graph[v]:
            if depth[w] != -1 and (depth[w] < depth[v] or depth[v] == -1):
                depth[v] = depth[w] + 1
                post[v] = w
            if not used[w]:
                used[w] = True
                q.append(w)
        
    #State of the program after the  for loop has been executed: `graph[v]` contains at least one element, `v` is a valid vertex in the graph, `depth[v]` is the shortest path distance from `v` to the farthest vertex in the graph, `post[v]` is the last vertex processed in the DFS traversal rooted at `v`, `q` is a queue containing all vertices reachable from `v` through unvisited edges, `used` indicates which vertices have been visited, and `depth[w]` and `post[w]` are updated accordingly for all `w` in `graph[v]`. If the loop does not execute, `depth[v]` remains -1, `post[v]` remains its original value, and `q` remains its initial state.
    return post
    #`The program returns the last vertex processed in the DFS traversal rooted at v (post[v])`
#Overall this is what the function does:The function `func_1` accepts a graph represented as a list of lists and a starting node, and performs a depth-first search (DFS) traversal starting from the given node. It updates the `depth` and `post` arrays to keep track of the shortest path distances and the last vertex processed in the DFS traversal, respectively. After the traversal, it returns the last vertex processed in the DFS traversal rooted at the starting node (`post[v]`). Potential edge cases include the graph being empty or the starting node not being connected to any other nodes. In such cases, `depth[v]` would remain -1 and `post[v]` would retain its initial value of -1. The function also ensures that all reachable vertices from the starting node are visited and their corresponding `depth` and `post` values are updated.

#State of the program right berfore the function call: n and m are integers such that 2 <= n <= 10^5 and 1 <= m <= 2 * 10^5. graph is a list of lists where graph[i] is a list of integers representing the indices of rooms directly connected to Room i+1 by a passage.
def func_2():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        
        graph[a - 1].append(b - 1)
        
        graph[b - 1].append(a - 1)
        
    #State of the program after the  for loop has been executed: `n` is `n_input`, `m` is `m_input`, `graph` is a list of `n` lists where each list contains the indices of nodes connected to the node represented by the index. The number of edges (`m`) is `m_input`, and each edge is bidirectional, connecting node `a-1` to node `b-1` and vice versa.
    post = func_1(graph)[1:]
    if (-1 in post) :
        func_3('No')
        return
        #None
    #State of the program after the if block has been executed: `n` is `n_input`, `m` is `m_input`, `graph` is a list of `n` lists where each list contains the indices of nodes connected to the node represented by the index, `post` is the result of `func_1(graph)` sliced from index 1 onwards, and -1 is not in `post`
    func_3('Yes')
    for i in post:
        func_3(i + 1)
        
    #State of the program after the  for loop has been executed: `n` is `n_input`, `m` is `m_input`, `graph` is a list of `n` lists where each list contains the indices of nodes connected to the node represented by the index, `post` is the result of `func_1(graph)` sliced from index 1 onwards and must contain at least one element, and -1 is not in `post`; `func_3(i + 1)` has been called for each valid `i` in `post`.
#Overall this is what the function does:The function `func_2` reads the number of rooms (`n`) and passages (`m`) from standard input, constructs a bidirectional graph representation of the rooms and passages, and then processes the results of `func_1(graph)` to determine whether the graph is fully connected. If `func_1(graph)` returns a list containing `-1`, indicating that the graph is not fully connected, the function calls `func_3('No')` and terminates without further action. Otherwise, it calls `func_3('Yes')` followed by a series of calls to `func_3` for each element in the result of `func_1(graph)`, excluding the first element. The function does not return any value. Potential edge cases include scenarios where the graph is not fully connected, causing the function to terminate early with `func_3('No')`. The function also assumes that `func_1(graph)` returns a list containing either `-1` or valid node indices, and it does not handle any missing functionality related to the behavior of `func_1` or `func_3`.

#State of the program right berfore the function call: args is a variable-length argument list containing the values to be printed, and kwargs is a dictionary that can contain the following keys: 'sep' (string, default is a space), 'file' (file object, default is sys.stdout), 'end' (string, default is a newline), and 'flush' (boolean, default is False).
def func_3():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `args` must be a non-empty list, the file contains the concatenation of all elements in `args` separated by `sep`, `at_start` is `False`.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`args` is a non-empty list, the file contains the concatenation of all elements in `args` separated by `sep`, `at_start` is `False`, and `kwargs` does not contain the key `'end'`. If `kwargs.pop('flush', False)` is `True`, the file buffer is flushed. Otherwise, the file buffer remains unchanged.
#Overall this is what the function does:The function `func_3` accepts a variable-length argument list `args` and a dictionary `kwargs` containing optional keys 'sep', 'file', 'end', and 'flush'. It prints the values in `args` to the specified output stream (`sys.stdout` by default) using the specified separator (`' '` by default). After printing, it appends the end string (`'\n'` by default) and flushes the output buffer if requested. The function does not return any value.

The final state of the program after the function concludes is as follows:
- The output stream contains the concatenated values from `args`, separated by the specified separator `sep`.
- The `args` parameter is a non-empty list.
- The `at_start` variable is `False`, indicating that no additional separator is needed for subsequent elements.
- The `kwargs` dictionary no longer contains the keys 'sep', 'file', 'end', and 'flush'.
- If `kwargs.pop('flush', False)` was `True`, the output buffer is flushed; otherwise, it remains unchanged.

