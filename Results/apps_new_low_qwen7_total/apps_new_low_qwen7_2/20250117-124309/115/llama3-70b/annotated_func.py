#State of the program right berfore the function call: $n$ and $m$ are integers such that $2 \le n, m \le 50$, and $A$ is a $n \times m$ matrix where each element is either $0$ or $1$.
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
        
    #State of the program after the  for loop has been executed: `i` is `n - 1`, `j` is `m`, `n` and `m` satisfy \(2 \leq n, m \leq 50\), and `A` is an \(n \times m\) matrix where each element is either 0 or 1. After the loop completes all its iterations, `ops` will contain the coordinates of all cells \((k, k+1)\) for \(k\) from \(i - 1\) to \(n - 2\), provided that at least one of the conditions \(A[k][k+1] == 1\) or \(A[k+1][k+2] == 1\) is true for those coordinates. If no such cells exist, `ops` will remain an empty list. The variable `i` starts at 0 and increments by 1 in each iteration of the outer loop, while `j` increments to `m - 1` and then to `m` as the inner loop completes. The loop continues to append the next coordinate to `ops` until no more valid cells are found, and finally, `i` reaches `n - 1`.
    if (len(ops) > 2500) :
        print(-1)
    else :
        print(len(ops))
        for op in ops:
            print(op[0], op[1])
            
        #State of the program after the  for loop has been executed: `i` is `n - 1`, `j` is `m`, `n` and `m` satisfy \(2 \leq n, m \leq 50\), `A` is an \(n \times m\) matrix where each element is either 0 or 1, `ops` is an empty list, and the printed value is the last printed tuple (if any).
    #State of the program after the if-else block has been executed: *`i` is an integer starting from 0 and incremented by 1 in each iteration of the outer loop, `j` is `m`, `n` and `m` satisfy \(2 \leq n, m \leq 50\), `A` is an \(n \times m\) matrix where each element is either 0 or 1, `ops` contains the coordinates of all cells \((k, k+1)\) for \(k\) from `i - 1` to `n - 2` (provided at least one of the conditions \(A[k][k+1] == 1\) or \(A[k+1][k+2] == 1\) is true for those coordinates), if no such cells exist, `ops` remains an empty list, and the loop continues to append the next coordinate to `ops` until no more valid cells are found, and finally, `i` reaches `n - 1`. If the length of `ops` is greater than 2500, `-1` is printed. Otherwise, the printed value is the last printed tuple (if any).
#Overall this is what the function does:The function processes an \( n \times m \) matrix \( A \) where each element is either 0 or 1. It identifies pairs of adjacent cells \((k, k+1)\) where at least one of the cells is 1. If more than 2500 such pairs are found, it prints -1. Otherwise, it prints the count of such pairs followed by the coordinates of these pairs.

