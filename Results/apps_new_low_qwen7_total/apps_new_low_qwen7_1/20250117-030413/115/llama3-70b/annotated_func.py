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
        
    #State of the program after the  for loop has been executed: n is at least 2, m is at least 3, and `ops` contains all tuples \((i + 1, j + 1)\) for \(i\) in the range \([1, n]\) and \(j\) in the range \([0, m - 2]\) if any of the elements \(A[i][j]\), \(A[i + 1][j]\), \(A[i][j + 1]\), or \(A[i + 1][j + 1]\) are equal to 1 for any \(i\) and \(j\). Otherwise, `ops` remains empty.
    if (len(ops) > 2500) :
        print(-1)
    else :
        print(len(ops))
        for op in ops:
            print(op[0], op[1])
            
        #State of the program after the  for loop has been executed: Output State: `n` is at least 2, `m` is at least 3, `ops` is a list of tuples representing valid operations, and the loop prints each tuple in `ops`. After the loop completes, `ops` is empty because all tuples have been printed, and no more valid operations exist. The final output state is that `ops` is empty, and the loop has executed `len(ops)` times.
        #
        #To summarize:
        #- **Invariant Variables**: None of the variables (`n`, `m`, or `ops`) change their state within the loop except for the consumption of `ops` entries.
        #- **Final Values**: 
        #  - `n`: At least 2 (unchanged)
        #  - `m`: At least 3 (unchanged)
        #  - `ops`: Empty (all tuples have been printed)
        #- **Conditions**: The loop continues to execute as long as `ops` is not empty. Once `ops` is empty, the loop stops executing.
        #
        #Thus, the final output state is:
        #Output State: `n` is at least 2, `m` is at least 3, `ops` is an empty list, and the loop has executed `len(ops)` times.
    #State of the program after the if-else block has been executed: `n` is at least 2, `m` is at least 3, and `ops` is an empty list. If the length of `ops` is greater than 2500, then `-1` is printed. Otherwise, the loop executes `len(ops)` times and prints each tuple in `ops`, resulting in `ops` being empty by the end.
#Overall this is what the function does:The function processes a binary matrix \( A \) of size \( n \times m \) (where \( n \geq 2 \) and \( m \geq 3 \)) and identifies certain "valid" operations based on specific conditions. It then checks if the number of valid operations exceeds 2500. If it does, the function prints \(-1\); otherwise, it prints the count of valid operations followed by each valid operation's coordinates. After processing, the list of valid operations is emptied.

