#State of the program right berfore the function call: The input consists of two integers n and m (2 <= n, m <= 50) followed by n lines, each containing m integers. Each integer is either 0 or 1, representing the elements of matrix A. The goal is to transform matrix B into matrix A, where B is initially a matrix of the same size as A with all elements set to 0, by performing operations that set 2x2 submatrices of B to 1.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 50 (inclusive), `m` is an integer between 2 and 50 (inclusive), the matrix `A` consists of `n` lines, each containing `m` integers with values 0 or 1, `i` is `n - 2`, `j` is `m - 2`, and `ops` is a list of tuples containing the positions where at least one adjacent cell is 1, but not all four cells are 1.
    if (len(ops) > 2500) :
        print(-1)
    else :
        print(len(ops))
        for op in ops:
            print(op[0], op[1])
            
        #State of the program after the  for loop has been executed: `n` is an integer between 2 and 50 (inclusive), `m` is an integer between 2 and 50 (inclusive), the matrix `A` consists of `n` lines, each containing `m` integers with values 0 or 1, `i` is `n - 2`, `j` is `m - 2`, and all operations in the `ops` list have been printed if the list is not empty.
    #State of the program after the if-else block has been executed: `n` is an integer between 2 and 50 (inclusive), `m` is an integer between 2 and 50 (inclusive), the matrix `A` consists of `n` lines, each containing `m` integers with values 0 or 1, `i` is `n - 2`, `j` is `m - 2`. If the list `ops` has more than 2500 elements, the value -1 has been printed and returned. Otherwise, all operations in the `ops` list have been printed if the list is not empty.
#Overall this is what the function does:The function takes input of two integers n and m, and a matrix A of size n x m with binary values. It calculates the minimum number of 2x2 submatrix operations required to transform a matrix B of the same size into matrix A. The function then prints the number of operations and the positions of the operations if the number of operations does not exceed 2500. If the number of operations exceeds 2500, the function prints -1. The function does not actually transform matrix B into matrix A, but rather outputs the theoretical minimum number of operations required to do so. The function handles edge cases where the input matrix A has dimensions between 2 and 50, and where the number of operations is either within or exceeds the limit of 2500.

