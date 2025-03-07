#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, x, y, and r are lists of integers where x[i], y[i] are the coordinates of the center of the i-th disk and r[i] is the radius of the i-th disk, with -10^9 <= x[i], y[i] <= 10^9 and 1 <= r[i] <= 10^9 for all i in the range [0, n-1]. visited is a list of boolean values initialized to False, and coef is a list of None values that will be used to store coefficients during the DFS traversal.
def func_1():
    n = int(input())
    x = [None] * n
    y = [None] * n
    r = [None] * n
    visited = [False] * n
    coef = [None] * n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
        
    #State: `n` is the input integer (within the range 1 to 1000), `x` is a list of integers with length `n` where each `x[i]` is the first integer from the `i-th` input, `y` is a list of integers with length `n` where each `y[i]` is the second integer from the `i-th` input, `r` is a list of integers with length `n` where each `r[i]` is the third integer from the `i-th` input, `visited` is a list of `False` values with length `n`, `coef` is a list of `None` values with length `n`.
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
        
    #State: `n` is the input integer (within the range 1 to 1000); `x` is a list of integers with length `n`; `y` is a list of integers with length `n`; `r` is a list of integers with length `n`; `visited` is a list of `True` values with length `n`; `coef` is a list of integers with length `n` (values depend on `dfs` logic); `tot` is an integer (value depends on `dfs` logic); `bipartite` is a boolean (value depends on `dfs` logic); `ok` is `True` if any iteration found a bipartite component with a non-zero `tot`, otherwise `False`.
    if ok :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: `n` is the input integer within the range 1 to 1000; `x` is a list of integers with length `n`; `y` is a list of integers with length `n`; `r` is a list of integers with length `n`; `visited` is a list of `True` values with length `n`; `coef` is a list of integers with length `n` (values depend on `dfs` logic); `tot` is an integer (value depends on `dfs` logic); `bipartite` is a boolean (value depends on `dfs` logic); `ok` is `True` if at least one iteration found a bipartite component with a non-zero `tot`, otherwise `False`.
#Overall this is what the function does:The function reads the number of disks and their respective centers and radii, then determines if the disks can be partitioned into two groups such that no two disks in the same group intersect. It prints "YES" if such a partition exists and "NO" otherwise.

