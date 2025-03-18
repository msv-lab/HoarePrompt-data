#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000. x, y, and r are lists of length n where for each 0 ≤ i < n, x[i], y[i] are integers such that -10^9 ≤ x[i], y[i] ≤ 10^9, and r[i] is an integer such that 1 ≤ r[i] ≤ 10^9. visited is a list of boolean values of length n initialized to False. coef is a list of length n initialized to None.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: Output State: `n` is an input integer, `x` is a list of length `n` where each element is an integer entered by the user, `y` is a list of length `n` where each element is an integer entered by the user, `r` is a list of length `n` where each element is an integer entered by the user, `visited` is a list of length `n` with all elements set to False, `coef` is a list of length `n` initialized to None.
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
        
    #State: Output State: `bipartite` is True or False based on the result of all `dfs` calls, `n` is the same input integer, `x` is a list of length `n` where each element is an integer entered by the user, `y` is a list of length `n` where each element is an integer entered by the user, `r` is a list of length `n` where each element is an integer entered by the user, `visited` is a list of length `n` with all elements set to True, `coef` is a list of length `n` where some elements may be set to 1 and others remain None, `tot` is the sum of all `tot` values from successful `dfs` calls, `ok` is True if any `dfs` call resulted in `bipartite` being True and `tot` not equal to 0, otherwise `ok` is False.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `bipartite` is True if any `dfs` call resulted in `bipartite` being True and `tot` not equal to 0, otherwise `bipartite` is False.
#Overall this is what the function does:The function accepts an integer `n`, and three lists `x`, `y`, and `r` of length `n`. It also takes two lists `visited` and `coef`, both of length `n`. The function performs a depth-first search (DFS) on the input data to determine if the graph represented by `x`, `y`, and `r` is bipartite. If any DFS call results in the graph being bipartite and the total sum `tot` is not zero, `ok` is set to True. Finally, the function prints 'YES' if `ok` is True, otherwise it prints 'NO'. The function does not return any value.

