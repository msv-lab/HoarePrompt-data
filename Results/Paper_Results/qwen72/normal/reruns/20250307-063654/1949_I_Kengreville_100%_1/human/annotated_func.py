#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000. x, y, and r are lists of integers where each list has length n, and for each i (0 <= i < n), x[i] and y[i] are integers in the range -10^9 to 10^9, and r[i] is an integer in the range 1 to 10^9. visited and coef are lists of length n, initially all elements in visited are False, and coef is initialized with None values.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `n` is an input integer such that 1 <= n <= 1000, `i` is `n-1`, `x`, `y`, and `r` are lists where each element from index 0 to `n-1` is assigned the values of three integers input by the user, split by spaces. The `visited` list remains a list of length `n` where all elements are `False`, and `coef` remains a list of `None` values with length `n`.
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
        
    #State: `n` is an input integer such that 1 <= n <= 1000, `i` is `n-1`, `x`, `y`, and `r` are lists where each element from index 0 to `n-1` is assigned the values of three integers input by the user, split by spaces. The `visited` list is a list of length `n` where all elements are `True`. The `coef` list is a list of length `n` where each element is 1 if the corresponding index was not visited before the loop started, and remains `None` if the corresponding index was visited before the loop started. `tot` is 0, `bipartite` is `True`, `ok` is `True` if any of the `bipartite` checks were `True` and `tot` was not 0 for any iteration.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: *`n` is an input integer such that 1 <= n <= 1000, `i` is `n-1`, `x`, `y`, and `r` are lists where each element from index 0 to `n-1` is assigned the values of three integers input by the user, split by spaces. The `visited` list is a list of length `n` where all elements are `True`. The `coef` list is a list of length `n` where each element is 1 if the corresponding index was not visited before the loop started, and remains `None` if the corresponding index was visited before the loop started. `tot` is 0, `bipartite` is `True`. If `ok` is `True`, the program has entered the if condition. If `ok` is `False`, the program has entered the else condition, and `ok` remains `False`.
#Overall this is what the function does:The function reads an integer `n` and three lists of integers `x`, `y`, and `r` from user input, each of length `n`. It then processes these lists to determine if a certain condition (related to bipartiteness and a non-zero total) is met. After processing, it prints 'YES' if the condition is met, and 'NO' otherwise. The function does not return any value. The lists `visited` and `coef` are modified during the processing, with `visited` being set to `True` for all indices and `coef` being set to `1` for some indices. The final state of the program includes the modified `visited` and `coef` lists, and the printed output of either 'YES' or 'NO'.

