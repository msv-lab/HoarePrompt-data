#State of the program right berfore the function call: graph is a list of lists representing an adjacency list of the cave's rooms, where graph[i] contains all rooms connected to room i; start is an integer representing the starting room, which is set to 0 by default (corresponding to Room 1).
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
        
    #State of the program after the  for loop has been executed: `graph` is a list of lists representing an adjacency list of the cave's rooms, `start` is 0, `used` is a list of `True` values for all reachable nodes, `q` is an empty list, `depth[v]` is the shortest distance from `start` to node `v`, and `post[v]` is the last node `w` that was visited in the path leading to node `v` for all reachable nodes `v`.
    return post
    #`The program returns a dictionary where the key is a reachable node and the value is the last node `w` that was visited in the path leading to node `v` for all reachable nodes `v`
#Overall this is what the function does:The function `func_1` accepts a parameter `graph`, a list of lists representing an adjacency list of the cave's rooms, and a parameter `start`, an integer representing the starting room. It performs a depth-first search (DFS) to find the shortest path from the start room to all other reachable rooms. For each reachable node, it records the last node `w` that was visited in the path leading to node `v`. If the start room is not reachable from any other room, the corresponding entry in the returned list will be -1. The function returns a list where the key is a reachable node and the value is the last node `w` that was visited in the path leading to node `v` for all reachable nodes `v`.

#State of the program right berfore the function call: n and m are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ m ≤ 2 × 10^5. The value of m represents the number of passages, and the values of n represent the number of rooms. The variable a and b are integers such that 1 ≤ a, b ≤ n and a ≠ b, representing the rooms connected by each passage.
def func_2():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        
        graph[a - 1].append(b - 1)
        
        graph[b - 1].append(a - 1)
        
    #State of the program after the  for loop has been executed: `a` and `b` are integers such that `1 ≤ a ≤ n` and `1 ≤ b ≤ n` and `a ≠ b`; `m` is exactly the number of times the loop has executed; `graph` is a list of `n` lists, where for each `i` from `0` to `n-1`, `graph[i]` contains all integers `j` such that there is an edge between node `i+1` and node `j+1` in the graph.
    post = func_1(graph)[1:]
    if (-1 in post) :
        func_3('No')
        return
        #The program does not return any value
    #State of the program after the if block has been executed: `a` and `b` are integers such that `1 ≤ a ≤ n` and `1 ≤ b ≤ n` and `a ≠ b`; `m` is exactly the number of times the loop has executed; `graph` is a list of `n` lists, where for each `i` from `0` to `n-1`, `graph[i]` contains all integers `j` such that there is an edge between node `i+1` and node `j+1` in the graph; `post` is a list starting from the second element of the list returned by `func_1(graph)` and does not contain -1
    func_3('Yes')
    for i in post:
        func_3(i + 1)
        
    #State of the program after the  for loop has been executed: `a` and `b` are integers such that \(1 \leq a \leq n\) and \(1 \leq b \leq n\) and \(a \neq b\); `m` is the number of times the loop has executed; `graph` is a list of `n` lists, where for each `i` from `0` to `n-1`, `graph[i]` contains all integers `j` such that there is an edge between node `i+1` and node `j+1` in the graph; `post` is a list starting from the second element of the list returned by `func_1(graph)` and does not contain -1, and it is completely processed. `func_3(i + 1)` has been called for each element in `post`.
#Overall this is what the function does:The function reads two integers `n` and `m` from standard input, where `2 ≤ n ≤ 10^5` and `1 ≤ m ≤ 2 × 10^5`. It then constructs a graph representing the connections between `n` rooms using `m` passages. After constructing the graph, it calls `func_1(graph)` to process the graph and obtain certain information. If the first element of the list returned by `func_1(graph)` is `-1`, it prints 'No' and terminates without further processing. Otherwise, it prints 'Yes' followed by the elements of the list returned by `func_1(graph)` starting from the second element. The function does not return any value. Potential edge cases include invalid inputs for `n` and `m`, and the presence of specific structures within the graph that could affect the output of `func_1(graph)`.

#State of the program right berfore the function call: args is a tuple containing the number of rooms (N) and the number of passages (M) as integers, and kwargs is a dictionary that may contain parameters for customizing the output (sep for separator, file for the output stream, end for ending character, and flush for flushing the output stream).
def func_3():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `args` is a tuple containing the number of rooms (N) and the number of passages (M) as integers, `kwargs` no longer contains the keys 'sep' and 'file', `sep` is the value of `kwargs.pop('sep', ' ')`, `file` contains the concatenated string of `str(N)`, `sep`, `str(M)`, and `at_start` is `False`.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`args` is a tuple containing the number of rooms (N) and the number of passages (M) as integers, `kwargs` no longer contains the keys 'sep', 'file', and 'end', `sep` is the value of `kwargs.pop('sep', ' ')`, `file` contains the concatenated string of `str(N)`, `sep`, `str(M)`, and `at_start` is `False`. If `kwargs.pop('flush', False)` is `True`, the internal buffer of `file` has been flushed. Otherwise, the internal buffer remains unchanged.
#Overall this is what the function does:The function `func_3` accepts a tuple `args` containing two integers representing the number of rooms (N) and the number of passages (M), and a dictionary `kwargs` that may contain optional parameters such as `sep` (separator), `file` (output stream), `end` (ending character), and `flush` (flushing the output stream). The function does not return any value. After executing the function, it prints the values of `N` and `M` separated by `sep` (default space) and followed by `end` (default newline), and optionally flushes the output stream if specified.

