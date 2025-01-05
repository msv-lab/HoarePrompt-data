#State of the program right berfore the function call: frm is a list of pairs representing directed edges in a directed graph, where each pair consists of non-negative integers representing node indices, and to is a list of pairs representing queries, where each pair consists of non-negative integers representing node indices, with constraints 1 ≤ |V| ≤ 10,000, 0 ≤ |E| ≤ 30,000, and 1 ≤ Q ≤ 100,000.
def func_1(frm, to):
    g[frm].append(to)
    rg[to].append(frm)
#Overall this is what the function does:The function accepts two parameters: a list of directed edges `frm` and a list of queries `to`. It appends directed edges to a graph and its reverse graph. However, the function does not return any results or fulfill the queries in `to`, making the annotation misleading. Instead, it only constructs part of a graph structure but lacks the complete implementation to handle queries or provide any output.

#State of the program right berfore the function call: now is an integer representing the current node in the graph, used is a set of integers representing the nodes that have been visited, and back_track is a list of integers representing the path taken during the traversal.
def func_2(now, used, back_track):
    used[now] = True
    for nx in g[now]:
        if not used[nx]:
            func_2(nx, used, back_track)
        
    #State of the program after the  for loop has been executed: `now` is the current node, `used` marks all reachable nodes from the starting node as visited, `back_track` remains unchanged.
    back_track.append(now)
#Overall this is what the function does:The function accepts an integer `now`, a set `used` to track visited nodes, and a list `back_track` to record the traversal path. It marks the current node as visited and recursively visits all adjacent unvisited nodes. After all reachable nodes are processed, it appends the current node to the `back_track` list, which effectively performs a depth-first traversal of a graph.

#State of the program right berfore the function call: now is an integer representing the current node, num_cmp is an integer representing the number of strongly connected components, used is a list of boolean values indicating whether each node has been visited, and cmp is a list of integers representing the component index of each node.
def func_3(now, num_cmp, used, cmp):
    used[now] = True
    cmp[now] = num_cmp
    for nx in rg[now]:
        if not used[nx]:
            func_3(nx, num_cmp, used, cmp)
        
    #State of the program after the  for loop has been executed: `now` is an integer representing the current node, `num_cmp` is an integer representing the number of strongly connected components, `used` is a list of boolean values with all nodes reachable from `now` set to True, `cmp` has updated `cmp` for all nodes reachable from `now` to `num_cmp`, and `rg[now]` contains all neighboring nodes of `now`.
#Overall this is what the function does:The function accepts an integer `now` representing the current node, an integer `num_cmp` indicating the index of the strongly connected component, a list `used` marking whether each node has been visited, and a list `cmp` which assigns component indices to nodes. It updates `used` to mark the current node and all reachable nodes as visited, and updates `cmp` to assign the current component index to those nodes. The function does not return a value but modifies the `used` and `cmp` lists in place to reflect the traversal of the graph.

#State of the program right berfore the function call: n is a non-negative integer representing the number of nodes in a directed graph, and the function processes a list of directed edges and a sequence of queries on pairs of nodes (u, v) where 0 <= u, v < n. The number of edges must satisfy 0 <= |E| <= 30,000, and the number of queries Q must satisfy 1 ≤ Q ≤ 100,000.
def func_4(n):
    used = [False] * n
    back_track = []
    cmp = [-1] * n
    for v in xrange(n):
        if not used[v]:
            func_2(v, used, back_track)
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer; `used` is a list of length `n` where elements may be either `True` or `False` depending on whether `func_2` was called for the corresponding index; `back_track` is a list that may contain elements modified by `func_2`; `cmp` is a list of length `n` with all elements set to `-1` unless modified by `func_2`.
    used = [False] * n
    num_cmp = 0
    for v in back_track[::-1]:
        if not used[v]:
            func_3(v, num_cmp, used, cmp)
            num_cmp += 1
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `used` reflects which elements from `back_track` were processed, `cmp` is unchanged unless modified by `func_3`, `num_cmp` is the number of unprocessed elements from `back_track` that were not used.
    return num_cmp, cmp
    #The program returns the number of unprocessed elements from 'back_track' that were not used as 'num_cmp' and the value of 'cmp' which is unchanged unless modified by 'func_3'.
#Overall this is what the function does:The function accepts a non-negative integer `n`, representing the number of nodes in a directed graph. It processes nodes using two helper functions, `func_2` and `func_3`, to determine strongly connected components. The function returns the count of strongly connected components as `num_cmp` and a list `cmp` that may contain modified values indicating the component each node belongs to. If the graph has no edges, `num_cmp` will be 0 and `cmp` will remain unchanged from its initial state.

