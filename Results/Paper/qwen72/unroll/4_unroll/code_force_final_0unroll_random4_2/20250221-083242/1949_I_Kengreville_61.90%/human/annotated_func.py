#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000.
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
        
    #State: `x` is a list of length `n` with all elements initialized to integers, `y` is a list of length `n` with all elements initialized to integers, `r` is a list of length `n` with all elements initialized to integers, `visited` is a list of length `n` with all elements initialized to `False`, `coef0` is a list of length `n` with all elements initialized to `None`, `coef1` is a list of length `n` with all elements initialized to `None`, `nodes` is an empty list.
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
        
    #State: Output State: `x` is a list of length `n` with all elements unchanged, `y` is a list of length `n` with all elements unchanged, `r` is a list of length `n` with all elements unchanged, `visited` is a list of length `n` with all elements unchanged, `coef0` is a list of length `n` with all elements initialized to `0`, `coef1` is a list of length `n` with all elements initialized to `1`, `nodes` is an empty list, `ok` is `True` if there is at least one element in `nodes` for which `c1` is not `0`, otherwise `ok` is `False`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: *`x`, `y`, `r`, and `visited` are lists of length `n` with all elements unchanged. `coef0` is a list of length `n` with all elements initialized to `0`, and `coef1` is a list of length `n` with all elements initialized to `1`. `nodes` is an empty list. If there is at least one element in `nodes` for which `c1` is not `0`, `ok` is `True`. Otherwise, `ok` is `False`.
#Overall this is what the function does:The function `func_1` reads an integer `n` from user input, where `1 <= n <= 1000`, and then reads `n` lines of input, each containing three integers. It initializes several lists of length `n` and performs a depth-first search (DFS) on the elements. After the search, it checks if there is at least one element in the `nodes` list for which the sum of `coef1` values is not zero. If such an element exists, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value. After the function concludes, the lists `x`, `y`, `r`, and `visited` remain unchanged, `coef0` is a list of length `n` with all elements set to `0`, `coef1` is a list of length `n` with all elements set to `1`, and `nodes` is an empty list.

#State of the program right berfore the function call: i is a non-negative integer such that 0 <= i < n, where n is the number of disks. The variables x, y, r, visited, nodes, coef0, and coef1 are lists of integers, and their lengths are all equal to n. The elements of x and y represent the integer coordinates of the centers of the disks, and the elements of r represent the positive integer radii of the disks. The lists visited, nodes, coef0, and coef1 are used to track the state of the disks during the depth-first search (DFS) process, with visited indicating whether a disk has been visited, nodes storing the sequence of visited disks, and coef0 and coef1 used to store coefficients related to the radii adjustments.
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
            
        #State: The loop will have iterated through all the disks (0 to n-1). For each disk `j` that is within the touching distance of disk `i` (i.e., the distance between the centers of disks `i` and `j` is exactly equal to the sum of their radii), the `visited[j]` will be set to `True`, `nodes` will include `j`, `coef0[j]` will be updated to `r[i] + r[j] - coef0[i]`, and `coef1[j]` will be updated to `-coef1[i]`. The `dfs(j)` function will be called for each such disk `j`. The values of `x`, `y`, and `r` remain unchanged.
    #State: *`i` is a non-negative integer such that 0 <= i < n. The lists `x`, `y`, `r`, `visited`, `nodes`, `coef0`, and `coef1` have lengths equal to `n`. If `visited[i]` is `False`, the loop will have iterated through all the disks (0 to n-1). For each disk `j` within the touching distance of disk `i` (i.e., the distance between the centers of disks `i` and `j` is exactly equal to the sum of their radii), `visited[j]` will be set to `True`, `nodes` will include `j`, `coef0[j]` will be updated to `r[i] + r[j] - coef0[i]`, and `coef1[j]` will be updated to `-coef1[i]`. The `dfs(j)` function will be called for each such disk `j`. The values of `x`, `y`, and `r` remain unchanged. If `visited[i]` is `True`, no changes are made to any of the lists.
#Overall this is what the function does:The function `dfs` accepts a non-negative integer `i` and performs a depth-first search (DFS) on a set of disks. It updates the `visited` list to mark disks as visited, appends the indices of visited disks to the `nodes` list, and updates the `coef0` and `coef1` lists based on the radii and positions of touching disks. The function does not return any value explicitly. After the function concludes, the `visited` list will indicate which disks have been visited, the `nodes` list will contain the indices of all visited disks in the order they were visited, and the `coef0` and `coef1` lists will be updated with coefficients related to the radii adjustments of the touching disks. The `x`, `y`, and `r` lists remain unchanged.

