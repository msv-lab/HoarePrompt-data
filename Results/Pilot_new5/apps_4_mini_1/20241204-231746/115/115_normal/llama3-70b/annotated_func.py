#State of the program right berfore the function call: n and m are integers such that 2 <= n, m <= 50, and A is a 2D list of integers with dimensions n x m where each element is either 0 or 1.
def func():
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    ops = []
    for i in range(n - 1):
        for j in range(m - 1):
            if A[i][j] == 1 and A[i + 1][j] == 1 and A[i][j + 1] == 1 and A[i + 1][
                j + 1] == 1:
                continue
            if A[i][j] == 1 or A[i + 1][j] == 1 or A[i][j + 1] == 1 or A[i + 1][j + 1
                ] == 1:
                ops.append((i + 1, j + 1))
        
    #State of the program after the  for loop has been executed: `n` is between 2 and 50, `m` is between 2 and 50, `A` is a 2D list of integers with dimensions `n x m`, `i` is `n - 2`, `j` is `m - 2`, and `ops` contains tuples of the form (k, l) for each (k, l) where at least one of `A[k-1][l-1]`, `A[k][l-1]`, `A[k-1][l]`, or `A[k][l]` is equal to 1, with `k` in range 1 to `n` and `l` in range 1 to `m`.
    if (len(ops) > 2500) :
        print(-1)
    else :
        print(len(ops))
        for op in ops:
            print(op[0], op[1])
            
        #State of the program after the  for loop has been executed: `n` is between 2 and 50, `m` is between 2 and 50, `A` is a 2D list of integers with dimensions `n x m`, `i` is `n - 2`, `j` is `m - 2`, `ops` is a list of tuples containing (k, l) where at least one of `A[k-1][l-1]`, `A[k][l-1]`, `A[k-1][l]`, or `A[k][l]` is equal to 1; the length of `ops` is the total number of tuples printed.`
    #State of the program after the if-else block has been executed: *`n` is between 2 and 50, `m` is between 2 and 50, `A` is a 2D list of integers with dimensions `n x m`, `i` is `n - 2`, `j` is `m - 2`, if the length of `ops` is greater than 2500, then no additional conditions are specified for `ops`. Otherwise, `ops` is a list of tuples containing (k, l) where at least one of `A[k-1][l-1]`, `A[k][l-1]`, `A[k-1][l]`, or `A[k][l]` is equal to 1, and the length of `ops` is the total number of tuples printed.
#Overall this is what the function does:The function accepts two integers `n` and `m`, which define the dimensions of a 2D list `A` of integers (where each element is either 0 or 1) and processes it to find the positions of the cells that have at least one adjacent cell (including diagonally) with a value of 1. If the count of such positions exceeds 2500, it prints -1; otherwise, it prints the count of positions found and the positions themselves.

