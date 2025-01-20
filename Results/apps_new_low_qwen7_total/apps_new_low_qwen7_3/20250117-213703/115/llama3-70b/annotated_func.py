#State of the program right berfore the function call: $n$ and $m$ are integers such that $2 \le n, m \le 50$, and $A$ is an $n \times m$ matrix where each element is either $0$ or $1$.
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
        
    #State of the program after the  for loop has been executed: `i` is `n-2`, `j` is `m-2`, `n` is greater than or equal to 2, `m` is greater than or equal to 2, the matrix `A` has the first row and first column containing at least one '1', and the list `ops` contains all valid positions `(i+1, j+1)` where the condition `(A[i][j] == 1 or A[i + 1][j] == 1 or A[i][j + 1] == 1 or (A[i + 1][j + 1] == 1))` is satisfied.
    if (len(ops) > 2500) :
        print(-1)
    else :
        print(len(ops))
        for op in ops:
            print(op[0], op[1])
            
        #State of the program after the  for loop has been executed: ops is an empty list, i is n-2, j is m-2, A remains unchanged.
    #State of the program after the if-else block has been executed: `i` is `n-2`, `j` is `m-2`, `n` is greater than or equal to 2, `m` is greater than or equal to 2, the matrix `A` has the first row and first column containing at least one '1'. If the length of `ops` is greater than 2500, -1 is printed. Otherwise, `ops` is an empty list and the matrix `A` remains unchanged.
#Overall this is what the function does:The function processes an \(n \times m\) matrix \(A\), where \(n\) and \(m\) are integers between 2 and 50, inclusive, and each element is either 0 or 1. It identifies positions in the matrix where four adjacent 1s form a square or two horizontal/vertical lines of 1s. For each identified position, it adds the coordinates \((i+1, j+1)\) to a list `ops`. If the number of such positions exceeds 2500, the function prints -1; otherwise, it prints the count of positions in `ops` followed by the coordinates of these positions. If no such positions are found, the matrix \(A\) remains unchanged.

