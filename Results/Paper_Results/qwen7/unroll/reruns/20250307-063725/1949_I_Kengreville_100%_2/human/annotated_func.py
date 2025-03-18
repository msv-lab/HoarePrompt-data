#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000. x, y, and r are lists of length n where for each 0 ≤ i < n, x[i], y[i] are integers such that -10^9 ≤ x[i], y[i] ≤ 10^9, and r[i] is an integer such that 1 ≤ r[i] ≤ 10^9. visited is a list of boolean values of length n initialized to False. coef is a list of None values of length n.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: Output State: `visited` is a list of boolean values of length `n` initialized to `False`, `x` is a list of integers of length `n` where each element is input from the user, `y` is a list of integers of length `n` where each element is input from the user, `r` is a list of integers of length `n` where each element is input from the user, `coef` is a list of `None` values of length `n`.
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
        
    #State: Output State: `bipartite` is True or False based on the `dfs` function's outcome, `visited` is a list of boolean values of length `n` where each element is True if the corresponding node was visited during any of the iterations, `x` is a list of integers of length `n` with original values unchanged, `y` is a list of integers of length `n` with original values unchanged, `r` is a list of integers of length `n` with original values unchanged, `coef` is a list of integer values (either 1 or None) of length `n` where each element is 1 if the corresponding node was visited during any of the iterations and the path was bipartite and non-zero, `tot` is an integer representing the sum of `coef` values for nodes that satisfy the bipartite condition and have a non-zero `tot` value, `ok` is True if any iteration of the loop found a bipartite component with a non-zero `tot` value, otherwise False.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `bipartite` is True or False based on the `dfs` function's outcome, `visited` is a list of boolean values of length `n` where each element is True if the corresponding node was visited during any of the iterations, `x` is a list of integers of length `n` with original values unchanged, `y` is a list of integers of length `n` with original values unchanged, `r` is a list of integers of length `n` with original values unchanged, `coef` is a list of integer values (either 1 or None) of length `n` where each element is 1 if the corresponding node was visited during any of the iterations and the path was bipartite and non-zero, `tot` is an integer representing the sum of `coef` values for nodes that satisfy the bipartite condition and have a non-zero `tot` value, `ok` is True if any iteration of the loop found a bipartite component with a non-zero `tot` value, otherwise `ok` is False.
#Overall this is what the function does:The function accepts an integer `n` and three lists `x`, `y`, and `r` of length `n`. It also uses two lists `visited` and `coef`, both of length `n`. The function processes these inputs to determine if there exists a bipartite component with a non-zero sum of certain coefficients. If such a component is found, it prints 'YES'; otherwise, it prints 'NO'. The function updates the `visited` and `coef` lists during its execution but does not return any value.

