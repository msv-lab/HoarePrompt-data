#State of the program right berfore the function call: n and m are integers such that 2 <= n, m <= 50, and A is a 2D list of integers where each element is either 0 or 1, with dimensions n x m.
def func_1(n, m, A):
    operations = []
    B = [([0] * m) for _ in range(n)]
    for i in range(n - 1):
        for j in range(m - 1):
            if A[i][j] == 1 and A[i][j + 1] == 1 and A[i + 1][j] == 1 and A[i + 1][
                j + 1] == 1:
                B[i][j] = B[i][j + 1] = B[i + 1][j] = B[i + 1][j + 1] = 1
                operations.append((i + 1, j + 1))
        
    #State of the program after the  for loop has been executed: `B` is a 2D list of integers (0 or 1) with dimensions n x m, where all valid 2x2 submatrices of `A` containing only 1's have been set to 1 in `B`; `operations` contains tuples of the form `(i + 1, j + 1)` for each valid 2x2 submatrix found in `A` that meets the specified conditions; `A` is a 2D list of integers (0 or 1), `n` and `m` are integers such that 2 <= n, m <= 50.`
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return -1
        
    #State of the program after the  for loop has been executed: `B` is a 2D list of integers (0 or 1) with dimensions n x m, `A` is a 2D list of integers (0 or 1) with dimensions n x m, `n` is an integer greater than or equal to 2, `m` is an integer greater than or equal to 2, and for all `i` in range(n) and for all `j` in range(m), `A[i][j]` is equal to `B[i][j]`.
    print(len(operations))
    for op in operations:
        print(op[0], op[1])
        
    #State of the program after the  for loop has been executed: `B` is a 2D list of integers (0 or 1) with dimensions n x m, `A` is a 2D list of integers (0 or 1) with dimensions n x m, `n` is greater than or equal to 2, `m` is greater than or equal to 2, `operations` contains all operations, `op` is the last operation in the list, and the values printed are `op[0]` and `op[1]` for each operation in `operations`.
#Overall this is what the function does:The function accepts two integers `n` and `m`, and a 2D list `A` of integers, checks for 2x2 submatrices of 1s in `A`, sets corresponding elements in a new matrix `B`, and returns -1 if `A` and `B` do not match. The function prints the count of valid operations and their indices but does not provide any return value indicating success or the operations performed if there are no mismatches.

