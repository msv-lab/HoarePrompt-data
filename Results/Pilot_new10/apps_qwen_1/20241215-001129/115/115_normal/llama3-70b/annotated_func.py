#State of the program right berfore the function call: $n$ and $m$ are positive integers such that $2 \le n, m \le 50$, and $A$ is a $n \times m$ matrix where each element is either $0$ or $1$.
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
        
    #State of the program after the  for loop has been executed: Output State: `ops` is a list containing all tuples \((i + 1, j + 1)\) for each position \((i, j)\) in the matrix \(A\) that satisfy the condition \(A[i][j] == 1\) or \(A[i + 1][j] == 1\) or \(A[i][j + 1] == 1\) or \(A[i + 1][j + 1] == 1\), `n` is a non-negative integer at least 2, `m` is an integer between 2 and 50, and `A` is an \(n \times m\) matrix where each element is either 0 or 1.
    if (len(ops) > 2500) :
        print(-1)
    else :
        print(len(ops))
        for op in ops:
            print(op[0], op[1])
            
        #State of the program after the  for loop has been executed: `ops` is a list of tuples representing positions in the matrix \(A\) that satisfy the given conditions; `n` is a non-negative integer at least 2; `m` is an integer between 2 and 50; `A` is an \(n \times m\) matrix where each element is either 0 or 1; `op[0]` and `op[1]` are the first and second elements of a tuple in `ops`, respectively.
    #State of the program after the if-else block has been executed: *`ops` is a list of tuples representing positions in the matrix \(A\) that satisfy the given conditions. `n` is a non-negative integer at least 2. `m` is an integer between 2 and 50. `A` is an \(n \times m\) matrix where each element is either 0 or 1. If `len(ops) > 2500`, `-1` is printed. Otherwise, the list `ops` remains unchanged.
#Overall this is what the function does:The function accepts an \(n \times m\) matrix \(A\) where each element is either 0 or 1, and \(n\) and \(m\) are positive integers such that \(2 \le n, m \le 50\). It identifies all positions \((i, j)\) in the matrix where at least one of the four adjacent cells (top, bottom, left, right) is 1. These positions are stored in the list `ops`. If the length of `ops` exceeds 2500, the function prints -1. Otherwise, it prints the length of `ops` followed by the coordinates of each position in `ops`.

