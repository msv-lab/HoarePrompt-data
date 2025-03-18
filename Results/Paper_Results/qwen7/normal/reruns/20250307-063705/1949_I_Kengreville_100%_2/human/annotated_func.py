#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000. x, y, and r are lists of length n, where for each i (0 ≤ i < n), x[i], y[i] are integers such that -10^9 ≤ x[i], y[i] ≤ 10^9, and r[i] is an integer such that 1 ≤ r[i] ≤ 10^9. visited is a list of boolean values of length n initialized to False. coef is a list of length n initialized to None.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: Output State: `i` is equal to `n-1`, `n` must be greater than 0, `x[i]`, `y[i]`, `r[i]` are integers entered by the user for each valid index `i` from `0` to `n-1`.
    #
    #This means that after the loop has executed all its iterations, the variable `i` will be equal to `n-1`, indicating that the loop has completed all `n` iterations. The lists `x`, `y`, and `r` will each contain `n` integers, which are the values entered by the user during each iteration of the loop.
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
        
    #State: All `coef[i]` where `i` ranges from 0 to `n-1` are set to 1, `tot` is 0, `bipartite` remains unchanged, and `ok` is True if `bipartite` is True and `tot` is not 0 for any iteration, otherwise `ok` remains False.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: All `coef[i]` where `i` ranges from 0 to `n-1` are set to 1, `tot` is 0, `bipartite` remains unchanged, and `ok` remains False.
#Overall this is what the function does:The function processes predefined lists `x`, `y`, `r`, `visited`, and `coef` to determine if a certain condition (`bipartite` and `tot`) holds true for any element in the list. If the condition is met for any element, it prints 'YES', otherwise it prints 'NO'. The function sets all elements in the `coef` list to 1 and initializes `tot` and `bipartite` to 0 and `ok` to False. After processing, it checks the value of `ok` and prints either 'YES' or 'NO' accordingly.

