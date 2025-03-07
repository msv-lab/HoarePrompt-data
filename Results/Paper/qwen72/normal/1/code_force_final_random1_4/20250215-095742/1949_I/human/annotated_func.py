#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000. x, y, and r are lists of integers where for each i (0 ≤ i < n), x[i] and y[i] are integers such that -10^9 ≤ x[i], y[i] ≤ 10^9, and r[i] is an integer such that 1 ≤ r[i] ≤ 10^9. visited is a list of booleans initialized to False for each element. coef is a list of None values with length n.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `n` is the input integer, `i` is `n-1`, `x` is a list of `n` integers, `y` is a list of `n` integers, `r` is a list of `n` integers, `visited` is a list of `False` values with length `n`, `coef` is a list of `None` values with length `n`.
    tot = 0
    bipartite = True
    ok = False
    for i in range(n):
        if not visited[i]:
            coef[i] = 1
            tot = 0
            bipartite = True
            dfs(i)
            ok = ok or bipartite and tot != 0
        
    #State: After all iterations of the loop, `n` remains the same as the input integer, `i` is `n-1`, `x` is a list of `n` integers, `y` is a list of `n` integers, `r` is a list of `n` integers (potentially updated), `visited` is a list where each element is `True` if the corresponding index has been processed by the `dfs` function, `coef` is a list where elements are set to 1 if the corresponding index has been processed by the `dfs` function, `tot` is the total count of nodes processed by the `dfs` function, `bipartite` is `True` if the graph remains bipartite after processing all nodes, and `ok` is `True` if the graph is bipartite and `tot` is not 0, or if `ok` was already `True` before the final update.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: *After all iterations of the loop, `n` remains the same as the input integer, `i` is `n-1`, `x` is a list of `n` integers, `y` is a list of `n` integers, `r` is a list of `n` integers (potentially updated), `visited` is a list where each element is `True` if the corresponding index has been processed by the `dfs` function, `coef` is a list where elements are set to 1 if the corresponding index has been processed by the `dfs` function, `tot` is the total count of nodes processed by the `dfs` function, and `bipartite` is `True` if the graph remains bipartite after processing all nodes. If `ok` was `True` before the final update, it remains `True`; otherwise, `ok` is `False`.
#Overall this is what the function does:The function reads an integer `n` and three lists of integers `x`, `y`, and `r` from user input, where each list has `n` elements. It then processes these lists using a depth-first search (DFS) algorithm to determine if a certain condition related to the bipartiteness of a graph is met. The function updates the `visited` and `coef` lists during this process. Finally, it prints 'YES' if the graph is bipartite and at least one node has been processed, otherwise it prints 'NO'. The function does not return any value.

