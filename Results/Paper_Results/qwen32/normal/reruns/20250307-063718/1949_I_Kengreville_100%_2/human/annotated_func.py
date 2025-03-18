#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, x, y, and r are lists of integers where x[i], y[i] are the integer coordinates of the center of the i-th disk and r[i] is the radius of the i-th disk, with -10^9 <= x[i], y[i] <= 10^9 and 1 <= r[i] <= 10^9 for all i in the range [0, n-1], visited is a list of boolean values initialized to False, coef is a list of None values that will be used to store coefficients during the DFS traversal, and tot is an integer initialized to 0 which will be used to accumulate the total difference in radii during the DFS traversal.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `n` is an input integer such that 1 <= `n` <= 1000, `x` is a list of integers of length `n` where each element is an input integer, `y` is a list of integers of length `n` where each element is an input integer, `r` is a list of integers of length `n` where each element is an input integer, `visited` is a list of boolean values initialized to False (all elements are False), `coef` is a list of `None` values of length `n`, `tot` is 0.
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
        
    #State: `n` is an input integer such that 1 <= `n` <= 1000, `x` is a list of integers of length `n`, `y` is a list of integers of length `n`, `r` is a list of integers of length `n`, `visited` is a list of boolean values where each element is True if it was visited during the loop, `coef` is a list of `None` values of length `n` except for indices that were visited, where `coef[i]` is set to 1 or potentially updated based on DFS logic, `tot` is the final value updated by the last DFS call, `bipartite` is the final value updated by the last DFS call, `ok` is True if any DFS call resulted in `bipartite` being True and `tot` not equal to 0, `i` is `n-1`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `n` is an input integer such that 1 <= `n` <= 1000, `x` is a list of integers of length `n`, `y` is a list of integers of length `n`, `r` is a list of integers of length `n`, `visited` is a list of boolean values where each element is True if it was visited during the loop, `coef` is a list of `None` values of length `n` except for indices that were visited, where `coef[i]` is set to 1 or potentially updated based on DFS logic, `tot` is the final value updated by the last DFS call, `bipartite` is the final value updated by the last DFS call, `i` is `n-1`. If `ok` is True, it indicates that at least one DFS call resulted in `bipartite` being True and `tot` not equal to 0. If `ok` is False, no DFS call resulted in `bipartite` being True and `tot` not equal to 0.
#Overall this is what the function does:The function reads input values describing disks, performs a DFS traversal to check for a specific condition related to the disks' radii and positions, and prints "YES" if the condition is met, otherwise prints "NO".

