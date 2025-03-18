#State of the program right berfore the function call: The input consists of two integers n and m (2 <= n, m <= 50) representing the number of rows and columns in matrices A and B, followed by n lines, each containing m integers (either 0 or 1) representing the elements of matrix A.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 50 (inclusive), `m` is an integer between 2 and 50 (inclusive), `A` is a 2D list of size `n x m` containing integers, `i` is `n - 1`, `j` is `m - 1`, and `ops` contains tuples `(i + 1, j + 1)` for every position `(i, j)` where the corresponding 2x2 sub-matrix in `A` has at least one 1 but not all 1s.
    if (len(ops) > 2500) :
        print(-1)
    else :
        print(len(ops))
        for op in ops:
            print(op[0], op[1])
            
        #State of the program after the  for loop has been executed: `n` is an integer between 2 and 50 (inclusive), `m` is an integer between 2 and 50 (inclusive), `A` is a 2D list of size `n x m` containing integers, `i` is `n - 1`, `j` is `m - 1`, `ops` is an empty list if it was not empty initially, and all operations in the original `ops` list have been printed.
    #State of the program after the if-else block has been executed: *`n` is an integer between 2 and 50 (inclusive), `m` is an integer between 2 and 50 (inclusive), `A` is a 2D list of size `n x m` containing integers, `i` is `n - 1`, `j` is `m - 1`. If `ops` initially contains more than 2500 elements, then -1 has been printed. Otherwise, `ops` is an empty list and all operations in the original `ops` list have been printed.
#Overall this is what the function does:The function accepts the dimensions and elements of matrix A as input, identifies 2x2 sub-matrices with at least one 1 but not all 1s, and prints the number and coordinates of these sub-matrices, or -1 if there are more than 2500 such sub-matrices.

