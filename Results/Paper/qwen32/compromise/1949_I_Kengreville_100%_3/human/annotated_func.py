#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, x, y, and r are lists of integers where x[i], y[i] are the coordinates of the center of the i-th disk and r[i] is the radius of the i-th disk with -10^9 <= x[i], y[i] <= 10^9 and 1 <= r[i] <= 10^9, visited is a list of boolean values initialized to False, coef is a list of None values that will be used to store coefficients, and tot and bipartite are variables used to keep track of the total and bipartiteness during the DFS traversal respectively.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `n` is an input integer, `x` is a list of integers of length `n` where each element is the first integer from each line of input, `y` is a list of integers of length `n` where each element is the second integer from each line of input, `r` is a list of integers of length `n` where each element is the third integer from each line of input, `visited` is a list of boolean values initialized to False, `coef` is a list of `None` values of length `n`, `tot` and `bipartite` are variables used to keep track of the total and bipartiteness during the DFS traversal respectively.
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
        
    #State: `visited` is a list of boolean values indicating which nodes have been visited, `coef` is a list of integers where each element is 1 if it was the starting point of a new component, `tot` is the final value after all DFS traversals, `bipartite` is the final value after all DFS traversals, `ok` is True if at least one bipartite component with a non-zero `tot` was found.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `visited` is a list of boolean values indicating which nodes have been visited, `coef` is a list of integers where each element is 1 if it was the starting point of a new component, `tot` is the final value after all DFS traversals, `bipartite` is the final value after all DFS traversals, and `ok` is a boolean indicating whether at least one bipartite component with a non-zero `tot` was found. If `ok` is True, at least one such component was found; otherwise, no such component was found.
#Overall this is what the function does:The function `func_1` determines if there exists at least one bipartite component of disks (circles) with a non-zero total count after performing a Depth-First Search (DFS) traversal. It reads the number of disks and their properties (center coordinates and radius), then checks each component of disks to see if it is bipartite and has a non-zero total count. If such a component is found, it prints "YES"; otherwise, it prints "NO".

