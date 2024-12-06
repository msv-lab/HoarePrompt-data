#State of the program right berfore the function call: A is a 2D list of integers containing only 0s and 1s, n and m are integers such that 2 <= n, m <= 50.
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
        
    #State of the program after the  for loop has been executed: `A` is a 2D list of integers containing only 0s and 1s, `n` is greater than 1, `m` is greater than 1, `ops` contains tuples indicating all unique positions `(i + 1, j + 1)` in `A` for which at least one of the elements `A[i][j]`, `A[i + 1][j]`, `A[i][j + 1]`, or `A[i + 1][j + 1]` is equal to 1, ensuring no duplicates in `ops`. If there are no such positions, `ops` remains empty.
    if (len(ops) > 2500) :
        print(-1)
    else :
        print(len(ops))
        for op in ops:
            print(op[0], op[1])
            
        #State of the program after the  for loop has been executed: `A` is a 2D list of integers containing only 0s and 1s, `n` is greater than 1, `m` is greater than 1, `ops` must contain tuples indicating positions in `A`, `op` will have the last tuple in `ops`, and the output will consist of the values of `op[0]` and `op[1]`. The final output is the integer value `len(ops)`, which represents the total number of tuples in `ops`.
    #State of the program after the if-else block has been executed: *`A` is a 2D list of integers containing only 0s and 1s, `n` is greater than 1, `m` is greater than 1, and `ops` contains tuples indicating unique positions in `A` where at least one of the elements `A[i][j]`, `A[i + 1][j]`, `A[i][j + 1]`, or `A[i + 1][j + 1]` is equal to 1. If the length of `ops` is greater than 2500, -1 has been printed. Otherwise, `ops` must contain tuples indicating positions in `A`, the last tuple in `ops` is stored in `op`, and the output consists of the values of `op[0]` and `op[1]`, with the final output being the integer value `len(ops)` representing the total number of tuples in `ops.`
#Overall this is what the function does:The function accepts a 2D list `A` of integers (containing only 0s and 1s) and two integers `n` and `m` (where 2 <= n, m <= 50). It checks all 2x2 submatrices of `A` for the presence of 1s. If a submatrix contains at least one 1, its top-left position (1-indexed) is added to a list. If the number of such positions exceeds 2500, the function prints `-1`. Otherwise, it prints the count of unique positions and their coordinates. The function does not return a value, and the output is printed directly.

