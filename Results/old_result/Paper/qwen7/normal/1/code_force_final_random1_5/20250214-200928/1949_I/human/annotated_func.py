#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000. x, y, and r are lists of length n, where for each 0 ≤ i < n, x[i], y[i] are integers such that -10^9 ≤ x[i], y[i] ≤ 10^9, and r[i] is an integer such that 1 ≤ r[i] ≤ 10^9. visited is a list of boolean values of length n initialized to False. coef is a list of length n initialized to None.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: After the loop executes all the iterations, `n` must be greater than or equal to the final value of `i`, which will be `n-1`. For each `i` from 0 to `n-1`, `x[i]`, `y[i]`, and `r[i]` will be integers from the input. The values of `visited`, `coef`, and the initial conditions for `x`, `y`, and `r` lists remain as they were initialized.
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
        
    #State: All nodes from 0 to n-1 have been processed, meaning `visited[i]` is True for every `i` in the range of `n`. The value of `coef[i]` is 1 for every `i` where `visited[i]` is True. The value of `tot` is the sum of all non-zero contributions made during the DFS calls for each component. `bipartite` is True for each component where the graph is bipartite and `tot` is not zero. `ok` is True if any component is bipartite and `tot` is not zero.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: All nodes from 0 to n-1 have been processed, meaning `visited[i]` is True for every `i` in the range of `n`. The value of `coef[i]` is 1 for every `i` where `visited[i]` is True. The value of `tot` is the sum of all non-zero contributions made during the DFS calls for each component. `bipartite` is True for each component where the graph is bipartite and `tot` is not zero. `ok` is True if any component is bipartite and `tot` is not zero. If the condition `ok` is True, then `ok` remains True. If `ok` is False, then `ok` remains False.
#Overall this is what the function does:The function processes a set of nodes (represented by lists `x`, `y`, and `r`) to determine if any component of the graph formed by these nodes is bipartite and has a non-zero sum (`tot`). If such a component exists, it prints 'YES'; otherwise, it prints 'NO'. After processing all nodes, the function ensures that all nodes are visited, and the `visited` list is updated accordingly. The `coef` list is set to 1 for visited nodes.

