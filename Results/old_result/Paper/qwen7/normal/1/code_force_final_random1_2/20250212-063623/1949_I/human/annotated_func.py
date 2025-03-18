#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000, x and y are lists of n integers representing the x and y coordinates of the centers of the disks respectively, r is a list of n integers representing the radii of the disks respectively, and visited and coef are lists of n boolean and integer values respectively used for tracking visited status and coefficients during the DFS process.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: Output State: `i` is equal to `n`, `n` must be greater than 0, each element in the lists `x`, `y`, and `r` up to index `n-1` is an integer entered by the user, and the lists `x`, `y`, and `r` have length `n`, while all other variables (`visited` and `coef`) remain unchanged and are still filled with `False` and `None`, respectively.
    #
    #This means that after the loop has executed all its iterations, the variable `i` will have the value `n`, indicating that the loop has completed all `n` iterations. Each list `x`, `y`, and `r` will have been populated with `n` integers, as provided by the user through the `input()` function within the loop. The `visited` list and `coef` list will remain unaltered from their initial state.
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
        
    #State: Output State: `i` is `n`, `bipartite` is True, `n` must be greater than 0, each element in the lists `x`, `y`, and `r` up to index `n-1` is an integer entered by the user, and the lists `x`, `y`, and `r` have length `n`, `visited` remains unchanged and is still filled with `False`, `coef[i-1]` (which is `coef[n-1]`) is 1, `tot` is 0, `ok` is True if `bipartite` is True and `tot` is not 0, otherwise `ok` is False.
    #
    #In this final state, after the loop has executed all its iterations, `i` will be equal to `n` because the loop increments `i` from 0 to `n-1`. The variable `bipartite` remains True as it was set to True during the last iteration's call to `dfs(i)`. The `coef` list has been updated such that `coef[i-1]` (or `coef[n-1]`) is set to 1. The `tot` variable remains 0 as there is no increment or modification within the loop body. The `ok` variable is True if `bipartite` is True and `tot` is not 0, otherwise it remains False. All other variables retain their initial or unchanged states as per the problem description.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `i` is `n`, `bipartite` is True, `n` must be greater than 0, each element in the lists `x`, `y`, and `r` up to index `n-1` is an integer entered by the user, and the lists `x`, `y`, and `r` have length `n`, `visited` remains unchanged and is still filled with `False`, `coef[i-1]` (which is `coef[n-1]`) is 1, `tot` is 0, and `ok` is True if `bipartite` is True and `tot` is not 0, otherwise `ok` is False.
#Overall this is what the function does:The function processes a set of disks defined by their x and y coordinates and radii. It uses Depth-First Search (DFS) to determine if the disks can be partitioned into two groups such that no two disks in the same group intersect. If such a partition exists and at least one disk is in each group, the function prints 'YES'. Otherwise, it prints 'NO'. The function does not return any value but modifies the `visited` and `coef` lists during its execution.

