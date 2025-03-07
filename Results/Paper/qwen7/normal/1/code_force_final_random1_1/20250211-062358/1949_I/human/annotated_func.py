#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000, x and y are lists of n integers each, representing the x and y coordinates of the centers of the disks respectively, r is a list of n integers, representing the radii of the disks respectively, visited is a list of n boolean values indicating whether a disk has been visited during the DFS, and coef is a list of n floating-point numbers used to calculate the coefficients for the disks' tangency conditions.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: Output State: All values of `i` from `0` to `n-1` are integers representing the indices that were updated during the loop's iterations. Specifically, `x[i]`, `y[i]`, and `r[i]` for each `i` from `0` to `n-1` are the integers entered by the user for each iteration of the loop. The variable `n` remains unchanged and represents the original length of the lists `x`, `y`, and `r`. The lists `visited` and `coef` remain as they were initially, with all elements set to `False` and `None`, respectively.
    #
    #In simpler terms, after the loop completes all its iterations, each element in the lists `x`, `y`, and `r` will contain an integer value that was input by the user, corresponding to the index position. The variable `n` keeps track of how many such inputs were made, and the other lists (`visited` and `coef`) remain unaltered from their initial state.
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
        
    #State: All elements in `visited` are set to True, `coef` contains 1s at indices where nodes were visited, `tot` is 0, `bipartite` remains True or False based on the graph's bipartiteness, and `ok` is True if any `bipartite` is True and `tot` is not 0 during any iteration, otherwise `ok` remains False.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
#Overall this is what the function does:The function processes a set of disks defined by their centers' coordinates (x, y) and radii (r). It performs a depth-first search (DFS) on the disks to determine if they form a bipartite graph based on their tangency conditions. If any connected component of the graph is bipartite and contains more than one disk, the function prints 'YES'. Otherwise, it prints 'NO'. The function does not return any value.

