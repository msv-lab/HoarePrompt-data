#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000. x, y, and r are lists of length n, where for each 0 ≤ i < n, x[i], y[i] are integers such that -10^9 ≤ x[i], y[i] ≤ 10^9, and r[i] is an integer such that 1 ≤ r[i] ≤ 10^9. visited is a boolean list of length n initialized to False. coef is a list of length n initialized to None.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: Output State: `n` is an input integer, `x` is a list of length `n` where each element is an integer entered by the user, `y` is a list of length `n` where each element is an integer entered by the user, `r` is a list of length `n` where each element is an integer entered by the user, `visited` is a boolean list of length `n` initialized to False, `coef` is a list of length `n` where each element is None.
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
        
    #State: Output State: `bipartite` is True/False based on the result of all `dfs` calls, `n` is the same input integer, `x` is a list of length `n` where each element is an integer entered by the user, `y` is a list of length `n` where each element is an integer entered by the user, `r` is a list of length `n` where each element is an integer entered by the user, `visited` is a boolean list of length `n` with some elements possibly set to True, `coef` is a list of length `n` where each element is either 1 or None, `tot` is an integer that could be 0 or non-zero based on the sum of certain elements during the `dfs` calls, `ok` is True if any `dfs` call results in `bipartite` being True and `tot` not being 0, otherwise False.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `bipartite` is True if any `dfs` call results in `bipartite` being True and `tot` not being 0. Otherwise, `bipartite` is False.
#Overall this is what the function does:The function processes a set of points (x, y) and their respective radii (r) to determine if a certain condition can be satisfied across all points. It initializes several lists and performs depth-first searches (DFS) to mark visited points and calculate coefficients. If any DFS results in a bipartite graph configuration where the total coefficient is non-zero, it prints 'YES'. Otherwise, it prints 'NO'. The function modifies the global lists visited and coef based on the DFS outcomes.

