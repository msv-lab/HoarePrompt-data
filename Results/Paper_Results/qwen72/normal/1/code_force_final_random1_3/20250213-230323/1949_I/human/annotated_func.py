#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000. x, y, and r are lists of integers where for each i (0 ≤ i < n), x[i] and y[i] are the coordinates of the center of the i-th disk with -10^9 ≤ x[i], y[i] ≤ 10^9, and r[i] is the radius of the i-th disk with 1 ≤ r[i] ≤ 10^9. visited is a list of booleans initialized to False for each element, and coef is a list of None values, both of length n.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: After the loop executes all the iterations, `n` is an input integer between 1 and 1000, `i` is `n-1`, `x` is a list where each element `x[j]` (for `j` in `0` to `n-1`) is the first integer from the corresponding input line, `y` is a list where each element `y[j]` (for `j` in `0` to `n-1`) is the second integer from the corresponding input line, `r` is a list where each element `r[j]` (for `j` in `0` to `n-1`) is the third integer from the corresponding input line, `visited` is a list of False values of length `n`, `coef` is a list of None values of length `n`.
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
        
    #State: `n` is an input integer between 1 and 1000, `i` is `n-1`, `x` is a list where each element `x[j]` (for `j` in `0` to `n-1`) is the first integer from the corresponding input line, `y` is a list where each element `y[j]` (for `j` in `0` to `n-1`) is the second integer from the corresponding input line, `r` is a list where each element `r[j]` (for `j` in `0` to `n-1`) is the third integer from the corresponding input line, `visited` is a list where each element is True if it was initially False, otherwise it remains unchanged, `coef` is a list where each element is 1 if the corresponding `visited` element was initially False, otherwise it remains None, `tot` is the total number of nodes processed in the last iteration where `bipartite` was True and `tot` was not 0, `bipartite` is True if the graph is bipartite, otherwise it is False, `ok` is True if the graph is bipartite and there was at least one node processed, otherwise it is False.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: *`n` is an input integer between 1 and 1000, `i` is `n-1`, `x` is a list where each element `x[j]` (for `j` in `0` to `n-1`) is the first integer from the corresponding input line, `y` is a list where each element `y[j]` (for `j` in `0` to `n-1`) is the second integer from the corresponding input line, `r` is a list where each element `r[j]` (for `j` in `0` to `n-1`) is the third integer from the corresponding input line, `visited` is a list where each element is True if it was initially False, otherwise it remains unchanged, `coef` is a list where each element is 1 if the corresponding `visited` element was initially False, otherwise it remains None, `tot` is the total number of nodes processed in the last iteration where `bipartite` was True and `tot` was not 0, `bipartite` is True if the graph is bipartite, otherwise it is False, and `ok` indicates whether the graph is bipartite and there was at least one node processed. If `ok` is True, the graph is bipartite and there was at least one node processed. If `ok` is False, either the graph is not bipartite or there were no nodes processed.
#Overall this is what the function does:The function reads an integer `n` and then reads `n` lines of input, each containing three integers representing the x-coordinate, y-coordinate, and radius of a disk. It initializes a list `visited` to track which disks have been processed and a list `coef` for additional calculations. The function then processes the disks to determine if the graph formed by the disks is bipartite and if there is at least one disk processed. If the graph is bipartite and at least one disk is processed, it prints 'YES'; otherwise, it prints 'NO'. The final state of the program includes the modified `visited` and `coef` lists, and the variables `tot`, `bipartite`, and `ok` reflecting the results of the processing.

