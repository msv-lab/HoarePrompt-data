#State of the program right berfore the function call: `graph` is a list of lists where `graph[v]` contains all the rooms directly connected to Room `v` through passages, `start` is an integer representing the starting room, which is Room 1 (though it is not used in the function as the room is fixed to 0 in the function call).
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
        
    #State of the program after the  for loop has been executed: `graph` is a list of lists, `used` is a list indicating whether each vertex has been visited, `q` is a list of vertices, `depth` is a list indicating the depth of each vertex in the traversal, and `post` is a list indicating the last vertex visited from each vertex. All elements in `used` are boolean values, all elements in `q` are integers, all elements in `depth` and `post` are integers. After the loop executes, every vertex that can be reached from `start` will have its `depth` and `post` values set correctly, and `used` will be `True` for all visited vertices. `q` will contain all the vertices that were added during the traversal, and the loop ensures that all reachable vertices are processed. If no vertex is reachable from `start`, the values of `used`, `q`, `depth`, and `post` remain as initially set.
    return post
    #`The program returns the list 'post', which indicates the last vertex visited from each vertex during the traversal starting from 'start'`
#Overall this is what the function does:The function `func_1` accepts two parameters: `graph`, a list of lists representing the adjacency list of a graph where `graph[v]` contains all the rooms directly connected to Room `v`, and `start`, an integer representing the starting room (which is fixed to 0). It performs a breadth-first search (BFS) traversal starting from the `start` room to determine the last room visited from each room during the traversal. The function returns a list `post` where `post[v]` indicates the last room visited from Room `v`. 

If no vertex is reachable from the `start` room, the function will still return a list of `-1` for all rooms, indicating that no room was visited from those rooms. The function sets the `depth` of the `start` room to 0 and marks it as visited. For each room `v` in the queue, it updates the `depth` and `post` values for its neighbors `w` if they haven't been visited yet. This process continues until all reachable rooms are processed.

#State of the program right berfore the function call: n and m are integers such that 2 <= n <= 10^5 and 1 <= m <= 2 * 10^5, graph is a list of lists where graph[i] contains integers representing the indices of rooms directly connected to Room i+1 via a passage, and all values in graph are valid according to the constraints provided.
def func_2():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        
        graph[a - 1].append(b - 1)
        
        graph[b - 1].append(a - 1)
        
    #State of the program after the  for loop has been executed: `n` is the integer value of the first number inputted, `m` is the integer value of the second number inputted and must be greater than or equal to 0, `a` is an integer from the input, `b` is an integer from the input, and `graph` is a list of `n` empty lists; for each pair `(a, b)`, `graph[a - 1]` includes `b - 1` and `graph[b - 1]` includes `a - 1`.
    post = func_1(graph)[1:]
    if (-1 in post) :
        func_3('No')
        return
        #None
    #State of the program after the if block has been executed: `n` is the integer value of the first number inputted, `m` is the integer value of the second number inputted and must be greater than or equal to 0, `a` is an integer from the input, `b` is an integer from the input, `graph` is a list of `n` empty lists; `post` is the list obtained by slicing the list returned by `func_1(graph)` starting from index 1, and -1 is not in the `post` list
    func_3('Yes')
    for i in post:
        func_3(i + 1)
        
    #State of the program after the  for loop has been executed: `i` is within the range of `post` (i.e., `0 <= i < len(post)`), `func_3(i + 1)` has been called for every valid `i` in `post`, and -1 is not in `post`.
#Overall this is what the function does:The function `func_2` accepts three parameters: `n`, `m`, and `graph`. It reads these parameters from the input, constructs a graph represented as a list of lists, and then calls another function `func_1` with this graph. If the result of `func_1` contains `-1`, it prints "No" and returns immediately. Otherwise, it prints "Yes" followed by the indices of the nodes in the graph as determined by `func_1`, excluding `-1`. The function does not return any value itself.

#State of the program right berfore the function call: args is a variable-length argument list containing the values to be printed, and kwargs is a dictionary containing keyword arguments such as 'sep' for separator, 'file' for the output stream, 'end' for the trailing character to write after the last value, and 'flush' to flush the stream.
def func_3():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `args` is a non-empty variable-length argument list, `kwargs` is a dictionary without 'sep' and 'file' keys, `sep` is either the original value of `sep` if it was present in `kwargs` or ' ', `file` is `sys.stdout`, `at_start` is `False`, and `sys.stdout` now contains the concatenated string of all elements in `args` separated by `sep`.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`args` is a non-empty variable-length argument list, `kwargs` is a dictionary without 'end', 'sep', and 'file' keys, `sep` is either the original value of `sep` if it was present in `kwargs` or ' ', `file` is `sys.stdout`, `at_start` is `False`, and if the key 'flush' is `True` in `kwargs`, the output is flushed to `sys.stdout`. Otherwise, the output remains as is.
#Overall this is what the function does:The function `func_3` accepts a variable-length argument list `args` and a dictionary of keyword arguments `kwargs`. It prints the values from `args` to a specified output stream (defaulting to `sys.stdout`), using the specified keyword arguments such as `sep` (separator), `file` (output stream), `end` (trailing character to write after the last value), and `flush` (to flush the output stream). After the function executes, the following conditions hold:
- The output stream (`file`) contains the concatenated string of all elements in `args` separated by `sep` and ending with `end`.
- If the `flush` keyword argument is `True`, the output stream is flushed; otherwise, it remains as is.
- All keyword arguments (`sep`, `file`, `end`, `flush`) are removed from `kwargs` upon completion.
- The function handles the case where `kwargs` might not contain certain keys by providing default values (e.g., `sep` defaults to a space, `file` defaults to `sys.stdout`, and `end` defaults to a newline).
- Potential edge cases include when `args` is empty or `kwargs` is empty, in which case no output is generated.

