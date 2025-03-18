#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, x and y are lists of integers where each element satisfies -10^9 <= x[i], y[i] <= 10^9, r is a list of integers where each element satisfies 1 <= r[i] <= 10^9, visited is a list of boolean values initialized to False, and coef is a list of None values that will be used to store coefficients during the DFS traversal.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `n` is the integer value provided by the user input, `x` is a list of `n` integers, `y` is a list of `n` integers, `r` is a list of `n` integers, `visited` is a list of `n` False values, and `coef` is a list of `n` None values.
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
        
    #State: `n` is the integer value provided by the user input, `x` is a list of `n` integers, `y` is a list of `n` integers, `r` is a list of `n` integers, `visited` is a list of `n` boolean values (some of which may be `True` after the loop), `coef` is a list of `n` integers (some of which may be `1` after the loop), `tot` is an integer (potentially modified by the loop), `bipartite` is a boolean (potentially modified by the loop), and `ok` is a boolean (potentially `True` if a bipartite condition with non-zero `tot` is met during the loop).
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `n` is the integer value provided by the user input, `x` is a list of `n` integers, `y` is a list of `n` integers, `r` is a list of `n` integers, `visited` is a list of `n` boolean values (some of which may be `True` after the loop), `coef` is a list of `n` integers (some of which may be `1` after the loop), `tot` is an integer (potentially modified by the loop), `bipartite` is a boolean (potentially modified by the loop), and `ok` is a boolean. If `ok` is `True`, the current value of `ok` remains `True`. If `ok` is `False`, the value of `ok` remains `False`.
#Overall this is what the function does:The function reads input values, performs a Depth-First Search (DFS) traversal on a graph constructed from the input data, and prints 'YES' if the graph is bipartite with a non-zero total, otherwise it prints 'NO'. The function modifies the `visited` and `coef` lists during the traversal but does not return any value explicitly.

