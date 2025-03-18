#State of the program right berfore the function call: $n$ and $m$ are integers such that $2 \le n, m \le 50$, and $A$ is a matrix of integers where each element is either $0$ or $1$.
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
        
    #State of the program after the  for loop has been executed: `i` is `n - 1`, `n` is a non-negative integer with at least 3, `m` is an integer such that \(2 \le m \le 50\), `A` is a matrix of size `n` by `m` where each element is either 0 or 1, `ops` is a list containing all the tuples `(i + 1, j + 1)` for which any of the conditions `A[i][j] == 1`, `A[i + 1][j] == 1`, `A[i][j + 1] == 1`, or `A[i + 1][j + 1] == 1` are satisfied for every valid index `j` in the range `[0, m - 2]` during the entire iteration range of `i`, and `j` is in the range \([0, m - 2]\).
    if (len(ops) > 2500) :
        print(-1)
    else :
        print(len(ops))
        for op in ops:
            print(op[0], op[1])
            
        #State of the program after the  for loop has been executed: `i` is `n - 1`, `n` is a non-negative integer with at least 3, `m` is an integer such that \(2 \le m \le 50\), `A` is a matrix of size `n` by `m` where each element is either 0 or 1, `ops` is a list containing at least one tuple based on the specified conditions, and the length of `ops` is less than or equal to 2500, `op[0]` is the first element of the last tuple in `ops`, `op[1]` is the second element of the last tuple in `ops`.
    #State of the program after the if-else block has been executed: *`i` is `n - 1`, `n` is a non-negative integer with at least 3, `m` is an integer such that \(2 \le m \le 50\), `A` is a matrix of size `n` by `m` where each element is either 0 or 1, `ops` is a list containing all the tuples `(i + 1, j + 1)` for which any of the conditions `A[i][j] == 1`, `A[i + 1][j] == 1`, `A[i][j + 1] == 1`, or `A[i + 1][j + 1] == 1` are satisfied for every valid index `j` in the range `[0, m - 2]` during the entire iteration range of `i`, and `j` is in the range \([0, m - 2]\). If the length of `ops` is greater than 2500, the output is `-1`. Otherwise, the length of `ops` is less than or equal to 2500, `op[0]` is the first element of the last tuple in `ops`, and `op[1]` is the second element of the last tuple in `ops`.
#Overall this is what the function does:The function processes a binary matrix \(A\) of dimensions \(n \times m\), where \(2 \le n, m \le 50\), and identifies positions where there are adjacent '1's in either a vertical or horizontal direction. Specifically, it finds all cells \((i+1, j+1)\) where any of the cells \((i, j)\), \((i+1, j)\), \((i, j+1)\), or \((i+1, j+1)\) contain a '1'. It collects these positions into a list `ops` and prints the length of this list followed by the positions themselves. If the list `ops` contains more than 2500 elements, the function outputs `-1` instead. After processing, the function ends without returning any value.

