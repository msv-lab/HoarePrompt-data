#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000, x is a list of n integers representing the x-coordinates of the centers of the disks, y is a list of n integers representing the y-coordinates of the centers of the disks, r is a list of n integers representing the radii of the disks, visited is a list of n boolean values indicating whether each disk has been visited during the DFS, coef0 and coef1 are lists of n floating-point numbers used to store coefficients for the linear equations, and nodes is a list used to store nodes during the DFS traversal.
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
        
    #State: Output State: `visited` is a list of length `n` filled with `False`, `x` is a list of length `n` containing `int` values, `y` is a list of length `n` containing `int` values, `r` is a list of length `n` containing `int` values, `coef0` is a list of length `n` filled with `None`, `coef1` is a list of length `n` filled with `None`, and `nodes` is now an empty list.
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
        
    #State: Output State: `visited` is a list of length `n` where each element is `True`, `x` is a list of length `n` containing `int` values, `y` is a list of length `n` containing `int` values, `r` is a list of length `n` containing `int` values, `coef0` is a list of length `n` where each element is `0`, `coef1` is a list of length `n` where each element is `1`, `nodes` is an empty list, and `ok` is `True`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `visited` is a list of length `n` where each element is `True`, `x` is a list of length `n` containing `int` values, `y` is a list of length `n` containing `int` values, `r` is a list of length `n` containing `int` values, `coef0` is a list of length `n` where each element is `0`, `coef1` is a list of length `n` where each element is `1`, `nodes` is an empty list, and `ok` remains unchanged (either `True` or `False`).
#Overall this is what the function does:The function reads the number of disks and their respective coordinates and radii. It then performs a depth-first search (DFS) on each unvisited disk, updating certain coefficients and tracking visited disks. Finally, it checks if any DFS resulted in a non-zero coefficient sum and prints 'YES' if so, otherwise 'NO'. The function ensures all disks are visited and modifies the `visited`, `coef0`, and `coef1` lists accordingly.

#State of the program right berfore the function call: n is an integer representing the number of disks, x is a list of integers where x[i] represents the x-coordinate of the center of the i-th disk, y is a list of integers where y[i] represents the y-coordinate of the center of the i-th disk, r is a list of integers where r[i] represents the radius of the i-th disk, visited is a boolean list of length n indicating whether each disk has been visited, and coef0 and coef1 are lists of length n used to store coefficients during the DFS traversal.
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
            
        #State: All `visited[j]` are `True`; `coef0[j]` and `coef1[j]` are updated based on the conditions; `nodes` remains unchanged.
    #State: All `visited[j]` are `True`; `coef0[j]` and `coef1[j]` are updated based on the conditions; `nodes` remains unchanged.
#Overall this is what the function does:The function `dfs(i)` performs a Depth-First Search (DFS) traversal starting from disk `i`. It marks the current disk as visited, adds its index to the `nodes` list, and recursively visits all directly touching unvisited disks. After visiting all such disks, all disks are marked as visited, their corresponding coefficients are updated based on the touching condition, and the `nodes` list remains unchanged.

