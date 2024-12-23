#State of the program right berfore the function call: $n$ and $m$ are positive integers such that $2 \le n, m \le 50$; $A$ is a $n \times m$ matrix where each element is either $0$ or $1$.
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
        
    #State of the program after the  for loop has been executed: `m` is greater than 1, `ops` is a list containing all valid tuples `(i+1, j+1)` for which at least one of the conditions `A[i][j] == 1`, `A[i + 1][j] == 1`, `A[i][j + 1] == 1`, or `A[i + 1][j + 1] == 1` is true, `i` is `n-1`, `j` is `m-1`.
    if (len(ops) > 2500) :
        print(-1)
    else :
        print(len(ops))
        for op in ops:
            print(op[0], op[1])
            
        #State of the program after the  for loop has been executed: `m` is greater than 1, `ops` is a list containing all valid tuples `(i+1, j+1)` for which at least one of the conditions `A[i][j] == 1`, `A[i + 1][j] == 1`, `A[i][j + 1] == 1`, or `A[i + 1][j + 1] == 1` is true, `i` is `n-1`, `j` is `m-1`, and all elements of `ops` are printed.
    #State of the program after the if-else block has been executed: *`m` is greater than 1, `ops` is a list containing all valid tuples `(i+1, j+1)` for which at least one of the conditions `A[i][j] == 1`, `A[i + 1][j] == 1`, `A[i][j + 1] == 1`, or `A[i + 1][j + 1] == 1` is true, `i` is `n-1`, `j` is `m-1`. If the length of `ops` is greater than 2500, the output is `-1`. Otherwise, all elements of `ops` are printed.
#Overall this is what the function does:The function accepts a \(n \times m\) matrix \(A\) where each element is either 0 or 1, along with the dimensions \(n\) and \(m\) (where \(2 \le n, m \le 50\)). It identifies all positions \((i+1, j+1)\) within the matrix where at least one of the four adjacent cells (top, bottom, left, right) is 1. It then checks if the number of such positions is greater than 2500. If it is, the function prints -1. Otherwise, it prints the count of these positions followed by the positions themselves.

