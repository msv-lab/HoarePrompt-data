#State of the program right berfore the function call: |V| and |E| are positive integers. The graph G(V, E) is a directed graph with nodes numbered from 0 to |V|-1. Each query pair u and v are nodes in the graph.**
def func_1(frm, to):
    g[frm].append(to)
    rg[to].append(frm)
#Overall this is what the function does:The function `func_1` accepts two parameters `frm` and `to`, both of which are positive integers representing nodes in a directed graph G(V, E) with nodes numbered from 0 to |V|-1. The function then updates the graph by adding an edge from node `frm` to node `to` and an edge from node `to` to node `frm` in the reverse graph, without returning any specific output. It is important to note that the annotations mention the state of the program before the function call, but don't provide any information about the state after the function execution.

#State of the program right berfore the function call: **
def func_2(now, used, back_track):
    used[now] = True
    for nx in g[now]:
        if not used[nx]:
            func_2(nx, used, back_track)
        
    #State of the program after the  for loop has been executed: All elements in `g[now]` have been visited and set to `True` in `used` after the loop finishes executing.
    back_track.append(now)
#Overall this is what the function does:The function `func_2` recursively visits nodes in a graph represented by the adjacency list `g`. It marks each visited node as `True` in the `used` array and appends the visited nodes to the `back_track` list. The function accepts three parameters: `now`, `used`, and `back_track`, but the specific return value or output is not provided in the constraints.

#State of the program right berfore the function call: **
def func_3(now, num_cmp, used, cmp):
    used[now] = True
    cmp[now] = num_cmp
    for nx in rg[now]:
        if not used[nx]:
            func_3(nx, num_cmp, used, cmp)
        
    #State of the program after the  for loop has been executed: `used[now]` remains True, `cmp[now]` retains the value of `num_cmp`, `rg[now]` remains unchanged. The loop will only call `func_3` for `nx` in `rg[now]` where `used[nx]` is initially False.
#Overall this is what the function does:The function func_3 accepts parameters now, num_cmp, used, and cmp. It marks the current index as used, assigns num_cmp to cmp for the current index, and recursively calls itself on neighboring indices in rg that have not been used yet. The function continues this process until all connected indices have been visited and marked as used.

#State of the program right berfore the function call: **The input consists of a directed graph G(V, E) where |V| is the number of nodes and |E| is the number of edges in the graph. The graph nodes are named with numbers 0, 1,..., |V|-1. Each query contains a pair of nodes u and v, where 0 ≤ u, v < |V|.
def func_4(n):
    used = [False] * n
    back_track = []
    cmp = [-1] * n
    for v in xrange(n):
        if not used[v]:
            func_2(v, used, back_track)
        
    #State of the program after the  for loop has been executed: All elements in the list `used` are `True` for each node in the graph, `back_track` contains the path taken, `cmp` is a list of length `n` filled with updated values.
    used = [False] * n
    num_cmp = 0
    for v in back_track[::-1]:
        if not used[v]:
            func_3(v, num_cmp, used, cmp)
            num_cmp += 1
        
    #State of the program after the  for loop has been executed: All elements in the list `used` are updated to `True` for all nodes in the graph, `back_track` contains the path taken, `cmp` is a list of length `n` filled with updated values, `num_cmp` is equal to the number of unique nodes in `back_track`
    return num_cmp, cmp
    #The program returns the number of unique nodes in the path taken stored in 'num_cmp' and the list 'cmp' containing updated values for all nodes
#Overall this is what the function does:The function func_4 accepts a positive integer n representing the number of nodes in a directed graph G(V, E). It initializes lists used, back_track, and cmp. It then iterates through the nodes of the graph, updating the lists used, back_track, and cmp accordingly. After the iteration, it resets the used list, calculates the number of unique nodes in the back_track path, and updates the cmp list. Finally, it returns the number of unique nodes in the path stored in 'num_cmp' and the updated values for all nodes in the list 'cmp'.

