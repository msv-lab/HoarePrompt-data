#State of the program right berfore the function call: n and m are integers such that 2 <= n <= 50 and 2 <= m <= 50, and A is a 2D list of integers with n rows and m columns where each integer is either 0 or 1.
def func_1(n, m, A):
    operations = []
    B = [([0] * m) for _ in range(n)]
    for i in range(n - 1):
        for j in range(m - 1):
            if A[i][j] == 1 and A[i][j + 1] == 1 and A[i + 1][j] == 1 and A[i + 1][
                j + 1] == 1:
                B[i][j] = B[i][j + 1] = B[i + 1][j] = B[i + 1][j + 1] = 1
                operations.append((i + 1, j + 1))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= n <= 50, `m` is an integer such that 2 <= m <= 50, `A` is a 2D list of integers with `n` rows and `m` columns, `B` is a 2D list of integers with `n` rows and `m` columns where `B[i][j]` equals 1 if `A[i][j]` equals 1 and is part of a 2x2 sub-matrix with all elements equal to 1, `operations` is a list containing tuples `(i + 1, j + 1)` for each such sub-matrix.
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return -1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= n <= 50, `m` is an integer such that 2 <= m <= 50, `A` is a 2D list of integers with `n` rows and `m` columns, `B` is a 2D list of integers with `n` rows and `m` columns, either `A` is equal to `B` or the program has returned -1 (in which case `A` and `B`'s states are unchanged and there exists an `i` and `j` such that `A[i][j]` is not equal to `B[i][j]`), `i` is `n` if the loop completes without returning -1, `j` equals `m` if the loop completes without returning -1 for any given `i`.
    print(len(operations))
    for op in operations:
        print(op[0], op[1])
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= n <= 50, `m` is an integer such that 2 <= m <= 50, `A` is a 2D list of integers with `n` rows and `m` columns, `B` is a 2D list of integers with `n` rows and `m` columns, either `A` is equal to `B` or there exists an `i` and `j` such that `A[i][j]` is not equal to `B[i][j]`, `i` is `n` if the loop completes without returning -1, `j` is `m` if the loop completes without returning -1, and all operations in `operations` have been printed.
#Overall this is what the function does:The function accepts integers `n` and `m` between 2 and 50, and a 2D list `A` with `n` rows and `m` columns containing 0 or 1, and returns -1 if `A` cannot be transformed into a matrix with all elements set to 1 in 2x2 sub-matrices, otherwise it prints the number of operations and the coordinates of each operation required to transform `A` into the target matrix

