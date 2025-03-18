#State of the program right berfore the function call: n and m are integers such that 2 <= n, m <= 50, and A is a list of n lists, each containing m integers where each integer is either 0 or 1.
def func_1(n, m, A):
    operations = []
    B = [([0] * m) for _ in range(n)]
    for i in range(n - 1):
        for j in range(m - 1):
            if A[i][j] == 1 and A[i][j + 1] == 1 and A[i + 1][j] == 1 and A[i + 1][
                j + 1] == 1:
                B[i][j] = B[i][j + 1] = B[i + 1][j] = B[i + 1][j + 1] = 1
                operations.append((i + 1, j + 1))
        
    #State of the program after the  for loop has been executed: `B` contains `1` at positions where the corresponding `2x2` submatrices in `A` were all `1`, `operations` contains tuples for each successful transformation, if any. If no transformations occur, `B` remains a list initialized to `0`, and `operations` remains empty.
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return -1
        
    #State of the program after the  for loop has been executed: `B` contains positions indicating successful transformations, `operations` reflects any transformations applied or is empty, `A[i][j]` equals `B[i][j]` for all `i` from `0` to `n-1` and `j` from `0` to `m-1`, `n` is the number of rows, `m` is the number of columns, and neither can be zero (both must be positive integers).
    print(len(operations))
    for op in operations:
        print(op[0], op[1])
        
    #State of the program after the  for loop has been executed: `B` contains positions indicating successful transformations, `operations` is a list of transformations with length equal to the number of transformations applied, `n` is a positive integer, `m` is a positive integer, the first two elements of each `op` have been printed for each transformation in `operations`. If `operations` is empty, `B` remains unchanged and `operations` is an empty list.
#Overall this is what the function does:The function accepts two integers `n` and `m`, and a list `A` containing `n` sublists each with `m` binary integers (0 or 1). It attempts to create a new list `B` where positions corresponding to 2x2 blocks of `1`s in `A` are set to `1`. The function returns -1 if there are discrepancies between `A` and `B` after the transformation, indicating that not all elements in `A` match those in `B` based on the transformation criteria. If transformations are successful, it prints the number of transformations and their 1-indexed positions without returning any other output. The function does not explicitly handle cases where no transformations occur, nor does it address any potential errors with empty or malformed input lists.

