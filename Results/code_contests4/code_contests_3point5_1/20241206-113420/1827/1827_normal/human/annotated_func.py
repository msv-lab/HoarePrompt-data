#State of the program right berfore the function call: V and E are non-negative integers such that 1 <= |V| <= 10,000 and 0 <= |E| <= 30,000. Q is a positive integer such that 1 <= Q <= 100,000. Each si, ti, ui, and vi are non-negative integers corresponding to nodes in the directed graph.**
def func_1(frm, to):
    g[frm].append(to)
    rg[to].append(frm)
#Overall this is what the function does:The function `func_1` accepts two parameters `frm` and `to`, which are non-negative integers corresponding to nodes in a directed graph. It then adds `to` as a neighbor to the node `frm` in the graph and vice versa. There is no explicit return value specified for this function.

#State of the program right berfore the function call: V is a non-negative integer representing the number of nodes, E is a non-negative integer representing the number of edges, Q is a positive integer representing the number of queries. Each query pair (u, v) consists of two integers where 0 <= u,v < V.**
def func_2(now, used, back_track):
    used[now] = True
    for nx in g[now]:
        if not used[nx]:
            func_2(nx, used, back_track)
        
    #State of the program after the  for loop has been executed: V, E, Q are non-negative integers. `used` at index `now` is True. All nodes reachable from `now` have been visited at least once and `func_2` has been called on each unvisited node.
    back_track.append(now)
#Overall this is what the function does:The function `func_2` recursively visits all nodes reachable from the current node `now` in a graph represented by the adjacency list `g`. It marks nodes as visited in the `used` array and appends the order of visited nodes to the `back_track` list. The function does not explicitly return any value. The provided annotations accurately describe the function's behavior.

#State of the program right berfore the function call: **
def func_3(now, num_cmp, used, cmp):
    used[now] = True
    cmp[now] = num_cmp
    for nx in rg[now]:
        if not used[nx]:
            func_3(nx, num_cmp, used, cmp)
        
    #State of the program after the  for loop has been executed: `used[now]` is True, `cmp[now]` is assigned the value of `num_cmp` for all `now` in rg.
#Overall this is what the function does:The function `func_3` takes parameters `now`, `num_cmp`, `used`, and `cmp`. It marks `now` as used, assigns the value of `num_cmp` to `cmp[now]`, and recursively calls itself for each neighbor of `now` in the graph `rg`. The function does not have a clear return value defined in the annotations.

#State of the program right berfore the function call: V is the number of nodes, E is the number of edges in the graph, and Q is the number of queries. Each query contains a pair of nodes u and v, where u and v are integers representing nodes in the graph.**
def func_4(n):
    used = [False] * n
    back_track = []
    cmp = [-1] * n
    for v in xrange(n):
        if not used[v]:
            func_2(v, used, back_track)
        
    #State of the program after the  for loop has been executed: V is the number of nodes, E is the number of edges in the graph, Q is the number of queries, used is a list of True values with a length of n (indicating all nodes have been visited), back_track contains the values of all nodes visited in order, cmp is a list of -1 values with a length of n, v is n-1
    used = [False] * n
    num_cmp = 0
    for v in back_track[::-1]:
        if not used[v]:
            func_3(v, num_cmp, used, cmp)
            num_cmp += 1
        
    #State of the program after the  for loop has been executed: `V`, `E`, `Q` are integers representing the number of nodes, edges, and queries respectively. `used` is a list of True values with a length of `n`, `back_track` is not empty, `cmp` is a list of non-negative integers with a length of `n`, `v` is the first node in `back_track`, `num_cmp` is equal to the number of unique nodes in `back_track`, and all nodes in `back_track` have been visited at least once.
    return num_cmp, cmp
    #The program returns the number of unique nodes in `back_track` as `num_cmp` and the list of non-negative integers `cmp` representing the components of the graph
#Overall this is what the function does:The function func_4 accepts a parameter n, representing the number of nodes in a graph. It initializes lists used, back_track, and cmp with False values, an empty list, and -1 values respectively. It then iterates over the nodes, marking them as used and appending them to back_track. After that, it resets the used list, counts the number of unique nodes in back_track, and assigns components to each node in cmp. The function returns the number of unique nodes in back_track as num_cmp and the list of components of the graph as cmp. The functionality accurately reflects the code execution.

