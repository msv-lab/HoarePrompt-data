#State of the program right berfore the function call: The input consists of a directed graph G(V, E) where |V| is the number of nodes, |E| is the number of edges, and each query contains a pair of nodes u and v. The nodes are named with numbers 0, 1,..., |V|-1. The nodes u and v in each query are integers representing nodes in the graph.**
def func_1(frm, to):
    g[frm].append(to)
    rg[to].append(frm)
#Overall this is what the function does:The function `func_1` accepts two parameters `frm` and `to`, both integers representing nodes in a directed graph. It modifies the graph structure by appending the `to` node to the adjacency list of `frm` in the directed graph `g` and vice versa in the reverse directed graph `rg`. There is no specific return value mentioned in the provided information.

#State of the program right berfore the function call: |V| is a positive integer representing the number of nodes in the graph, |E| is a non-negative integer representing the number of edges in the graph, and Q is a positive integer representing the number of queries. Each si and ti are integers representing the source and target nodes of the i-th edge, and each ui and vi are pairs of integers representing nodes in the graph.**
def func_2(now, used, back_track):
    used[now] = True
    for nx in g[now]:
        if not used[nx]:
            func_2(nx, used, back_track)
        
    #State of the program after the  for loop has been executed: |V|, |E|, Q, si, ti, ui, vi are integers. Each si and ti are integers, each ui and vi are pairs of integers. used at index now is True. The loop will continue to execute as long as g[now] returns a non-empty list of nodes, and (not used[nx]) is True for each node nx in the list returned by g[now].
    back_track.append(now)
#Overall this is what the function does:The function func_2 recursively traverses a graph starting from a given node `now` and marks the nodes visited by setting them to True in the `used` array. It appends the visited nodes to the `back_track` list. The function does not have a return value.

#State of the program right berfore the function call: V is a non-negative integer representing the number of nodes in the graph, E is a non-negative integer representing the number of edges in the graph, Q is a positive integer representing the number of queries. si and ti are integers representing the source and target nodes of the i-th edge, where 0 <= si, ti < V. ui and vi are integers representing a pair of nodes given as the i-th query, where 0 <= ui, vi < V.**
def func_3(now, num_cmp, used, cmp):
    used[now] = True
    cmp[now] = num_cmp
    for nx in rg[now]:
        if not used[nx]:
            func_3(nx, num_cmp, used, cmp)
        
    #State of the program after the  for loop has been executed: V, E, Q, si, ti, ui, vi, num_cmp, cmp, used are all integers and arrays as described. After the execution of the if-else block, all nodes reachable from the initial node 'now' are marked as visited in the used array, cmp contains the values of num_cmp for each visited node, and there is at least one node connected to each visited node in rg.
#Overall this is what the function does:The function `func_3` accepts parameters `now`, `num_cmp`, `used`, and `cmp`. It marks all nodes reachable from the current node `now` as visited in the `used` array, assigns the value of `num_cmp` to the corresponding nodes in the `cmp` array, and ensures that each visited node has at least one connection in the graph. The function does not explicitly return a value.

#State of the program right berfore the function call: V is a positive integer representing the number of nodes, E is a non-negative integer representing the number of edges, Q is a positive integer representing the number of queries. Each query pair (u, v) consists of two integers u and v such that 0 <= u, v < V.**
def func_4(n):
    used = [False] * n
    back_track = []
    cmp = [-1] * n
    for v in xrange(n):
        if not used[v]:
            func_2(v, used, back_track)
        
    #State of the program after the  for loop has been executed: All elements in the `used` list are `True`, `back_track` contains all values from 0 to n-1 in order, all elements in the `cmp` list remain `-1`, `n` is greater than or equal to 1.
    used = [False] * n
    num_cmp = 0
    for v in back_track[::-1]:
        if not used[v]:
            func_3(v, num_cmp, used, cmp)
            num_cmp += 1
        
    #State of the program after the  for loop has been executed: All elements in the `used` list are `True`, `back_track` contains all values from 0 to n-1 in order, all elements in the `cmp` list will have values ranging from 0 to n-1 in order, `n` is greater than or equal to 1, `num_cmp` is equal to the total number of elements in `back_track`, and the loop has iterated through all elements in `back_track` updating the corresponding values in `used` and `cmp`.
    return num_cmp, cmp
    #The program returns the total number of elements in `back_track`, which is stored in `num_cmp`, and the list `cmp` containing values ranging from 0 to n-1 in order
#Overall this is what the function does:The function `func_4` accepts a positive integer `n` representing the number of nodes. It initializes three lists `used`, `back_track`, and `cmp` with specific values. Then, it iterates through the elements of `back_track` to update `used` and `cmp` accordingly. Finally, it returns the total number of elements in `back_track`, stored in `num_cmp`, and the list `cmp` containing values ranging from 0 to n-1 in order. The function does not include the implementation details of `func_2` and `func_3`, so it relies on those functions to update the necessary lists.

