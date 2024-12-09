#State of the program right berfore the function call: n and m are integers such that 2 <= n, m <= 50, and A is a 2D list of integers where each element is either 0 or 1 with dimensions n x m.
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
        
    #State of the program after the  for loop has been executed: `n` and `m` are integers between 2 and 50, `A` is a 2D list of integers (0s and 1s) with dimensions `n x m`, `ops` contains tuples representing the positions (i + 1, j + 1) for each pair of adjacent cells checked where at least one cell is equal to 1 across all iterations of the loop. If none of the cells in any 2x2 submatrix satisfied the condition during any iteration, then `ops` remains empty.
    if (len(ops) > 2500) :
        print(-1)
    else :
        print(len(ops))
        for op in ops:
            print(op[0], op[1])
            
        #State of the program after the  for loop has been executed: `n` and `m` are integers between 2 and 50; `A` is a 2D list of integers (0s and 1s) with dimensions `n x m`; `ops` is a list of tuples with dimensions equal to the number of tuples in `ops`; `op` will have been assigned to each tuple in `ops` during the loop execution; all tuples in `ops` have been printed.
    #State of the program after the if-else block has been executed: *`n` and `m` are integers between 2 and 50. If the length of `ops` is greater than 2500, then `ops` contains tuples representing the positions of adjacent cells checked where at least one cell is equal to 1 during the iterations of the loop. If the length of `ops` is less than or equal to 2500, then `ops` is a list of tuples with dimensions equal to the number of tuples in `ops`, each tuple representing positions of adjacent cells, and all tuples in `ops` have been printed.
#Overall this is what the function does:The function accepts two integers `n` and `m` (where 2 <= n, m <= 50) and a 2D list `A` of integers (0s and 1s) with dimensions `n x m`. It checks all 2x2 submatrices within `A` and collects the positions (1-based indices) of cells that are part of a submatrix containing at least one '1'. If the number of such positions exceeds 2500, it prints `-1`. Otherwise, it prints the count of collected positions followed by the positions themselves. If all cells in any 2x2 submatrix contain '1's, those positions are not included in the output.

