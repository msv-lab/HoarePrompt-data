#State of the program right berfore the function call: n and m are positive integers such that 2 <= n, m <= 50, and A is a 2D list of integers where each integer is either 0 or 1.
def func_1(n, m, A):
    operations = []
    B = [([0] * m) for _ in range(n)]
    for i in range(n - 1):
        for j in range(m - 1):
            if A[i][j] == 1 and A[i][j + 1] == 1 and A[i + 1][j] == 1 and A[i + 1][
                j + 1] == 1:
                B[i][j] = B[i][j + 1] = B[i + 1][j] = B[i + 1][j + 1] = 1
                operations.append((i + 1, j + 1))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 2 and 50 (inclusive), `m` is a positive integer between 2 and 50 (inclusive), `A` is a 2D list of integers where each integer is either 0 or 1, `B` is a 2D list of size `n` by `m` where each element is 0, `operations` is a list of tuples. For each tuple `(i + 1, j + 1)` in `operations`, the submatrix defined by `A[i][j]`, `A[i][j + 1]`, `A[i + 1][j]`, and `A[i + 1][j + 1]` in `A` are all 1s, and the corresponding cells in `B` are set to 1.
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return -1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 2 and 50, `m` is a positive integer between 2 and 50, `A` is a 2D list of integers where each integer is either 0 or 1, `B` is a 2D list of size `n` by `m` where each element is 0, `operations` is a list of tuples, `i` is `n-1`, `j` is `m-1`. For all `i` in the range [0, `n-1`] and `j` in the range [0, `m-1`], `A[i][j] == B[i][j]`. If any `A[i][j]` is not equal to `B[i][j]`, the function returns -1. Otherwise, the function returns 0 after completing all iterations.
    print(len(operations))
    for op in operations:
        print(op[0], op[1])
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 2 and 50, `m` is a positive integer between 2 and 50, `A` is a 2D list of integers where each integer is either 0 or 1, `B` is a 2D list of size `n` by `m` where each element is 0, `operations` is a list of tuples, `i` is the index of the last tuple's first element, `j` is the index of the last tuple's second element, and the values of `op[0]` and `op[1]` from all tuples in `operations` are printed.
#Overall this is what the function does:The function `func_1` takes three parameters: `n` and `m`, which are the dimensions of a 2D list `A` containing only 0s and 1s. The function aims to identify and mark certain submatrices within `A` where all four corners are 1s, creating a new 2D list `B` of the same size as `A` where these marked submatrices are also set to 1s. It records the coordinates of these submatrices in a list called `operations`. After processing, the function checks if `A` and `B` are identical; if not, it returns -1 indicating that the two matrices do not match. If they match, the function prints the number of operations performed and the coordinates of the operations. The function can return -1 under various conditions, including when the matrices do not match or when no valid submatrices are found.

