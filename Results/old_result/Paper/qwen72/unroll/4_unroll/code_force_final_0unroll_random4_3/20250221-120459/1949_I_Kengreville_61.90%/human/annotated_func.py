#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000. x, y, and r are lists of integers where len(x) = len(y) = len(r) = n, and for each i, -10^9 <= x[i], y[i] <= 10^9 and 1 <= r[i] <= 10^9. visited, coef0, and coef1 are lists of length n initialized to False and None respectively. nodes is an empty list.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef0 = [None] * n
    coef1 = [None] * n
    nodes = []
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `x` is a list of integers of length `n`, `y` is a list of integers of length `n`, `r` is a list of integers of length `n`, `visited` is a list of length `n` initialized to `False`, `coef0` is a list of `None` values of length `n`, `coef1` is a list of `None` values of length `n`, `nodes` is an empty list.
    ok = False
    for i in range(n):
        if not visited[i]:
            coef0[i] = 0
            coef1[i] = 1
            nodes = []
            dfs(i)
            c0 = 0
            c1 = 0
            for j in nodes:
                c0 += coef0[j]
                c1 += coef1[j]
            ok = ok or c1 != 0
        
    #State: `x` is a list of integers of length `n`, `y` is a list of integers of length `n`, `r` is a list of integers of length `n`, `visited` is a list of length `n` where all elements are `True`, `coef0` is a list of integers of length `n` where all elements are `0`, `coef1` is a list of integers of length `n` where all elements are `1`, `nodes` is an empty list, `ok` is `True` if any of the `c1` values calculated in the loop are non-zero, otherwise `False`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: *`x` is a list of integers of length `n`, `y` is a list of integers of length `n`, `r` is a list of integers of length `n`, `visited` is a list of length `n` where all elements are `True`, `coef0` is a list of integers of length `n` where all elements are `0`, `coef1` is a list of integers of length `n` where all elements are `1`, `nodes` is an empty list, and `ok` is `True` if at least one of the `c1` values calculated in the loop is non-zero; otherwise, `ok` is `False`.
#Overall this is what the function does:The function reads an integer `n` and `n` sets of coordinates and radii from the user input, storing them in lists `x`, `y`, and `r` respectively. It then processes these sets using a depth-first search (DFS) to determine if there is at least one non-zero value in the `coef1` list after the DFS completes. If such a value exists, the function prints 'YES'; otherwise, it prints 'NO'. After the function concludes, the lists `x`, `y`, and `r` contain the input values, `visited` is a list of length `n` with all elements set to `True`, `coef0` is a list of length `n` with all elements set to `0`, `coef1` is a list of length `n` with all elements set to `1`, and `nodes` is an empty list.

#State of the program right berfore the function call: i is an integer representing the index of a disk, n is a positive integer representing the total number of disks, x and y are lists of integers representing the x and y coordinates of the centers of the disks, r is a list of positive integers representing the radii of the disks, visited is a list of booleans indicating whether a disk has been visited, nodes is a list of integers representing the indices of the disks being processed, coef0 and coef1 are lists of numbers representing coefficients used in the DFS algorithm.
def dfs(i):
    if (not visited[i]) :
        visited[i] = True
        nodes.append(i)
        for j in range(n):
            dx = x[i] - x[j]
            
            dy = y[i] - y[j]
            
            if not visited[j] and (r[i] + r[j]) ** 2 == dx ** 2 + dy ** 2:
                coef0[j] = r[i] + r[j] - coef0[i]
                coef1[j] = -coef1[i]
                dfs(j)
            
        #State: The loop modifies the `visited`, `coef0`, `coef1`, and `nodes` lists. For each disk `j` that has not been visited and whose center is exactly `r[i] + r[j]` units away from the center of disk `i`, the following changes occur: `visited[j]` becomes `True`, `coef0[j]` is updated to `r[i] + r[j] - coef0[i]`, `coef1[j]` is updated to `-coef1[i]`, and `j` is appended to `nodes`. The index `i` remains unchanged, and the lists `x`, `y`, and `r` are not modified.
    #State: *`i` is an integer representing the index of a disk, `n` is a positive integer representing the total number of disks, `x` and `y` are lists of integers representing the x and y coordinates of the centers of the disks, `r` is a list of positive integers representing the radii of the disks, `visited` is a list of booleans indicating whether a disk has been visited, `nodes` is a list of integers representing the indices of the disks being processed, and `coef0` and `coef1` are lists of numbers representing coefficients used in the DFS algorithm. If `visited[i]` is `False`, the `visited`, `coef0`, `coef1`, and `nodes` lists are modified as follows: For each disk `j` that has not been visited and whose center is exactly `r[i] + r[j]` units away from the center of disk `i`, `visited[j]` becomes `True`, `coef0[j]` is updated to `r[i] + r[j] - coef0[i]`, `coef1[j]` is updated to `-coef1[i]`, and `j` is appended to `nodes`. If `visited[i]` is `True`, no changes are made to any of the lists.
#Overall this is what the function does:The function `dfs` accepts an integer `i` representing the index of a disk. It marks the disk at index `i` as visited if it has not been visited before and appends `i` to the `nodes` list. It then recursively visits all disks `j` that have not been visited and whose centers are exactly `r[i] + r[j]` units away from the center of disk `i`. For each such disk `j`, it updates `visited[j]` to `True`, `coef0[j]` to `r[i] + r[j] - coef0[i]`, and `coef1[j]` to `-coef1[i]`, and appends `j` to the `nodes` list. If the disk at index `i` has already been visited, the function returns without making any changes. The lists `x`, `y`, and `r` remain unchanged throughout the function's execution.

