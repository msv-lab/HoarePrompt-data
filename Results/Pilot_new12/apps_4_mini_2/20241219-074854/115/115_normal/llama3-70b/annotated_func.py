#State of the program right berfore the function call: n and m are integers such that 2 <= n, m <= 50, and A is a 2D list of integers containing exactly n rows and m columns where each element is either 0 or 1. Matrix B is initialized to a 2D list of zeros with the same dimensions as A.
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
        
    #State of the program after the  for loop has been executed: `A` is a 2D list of integers (dimensions n x m), `B` is a 2D list of zeros (dimensions n x m), `n` is at least 2, `m` is between 2 and 50, `ops` contains tuples with coordinates of all cells (i + 1, j + 1) where at least one of `A[i][j]`, `A[i + 1][j]`, `A[i][j + 1]`, or `A[i + 1][j + 1]` equals 1 for all valid pairs of (i, j) examined in the loops. If no such cells are found, `ops` remains empty.
    if (len(ops) > 2500) :
        print(-1)
    else :
        print(len(ops))
        for op in ops:
            print(op[0], op[1])
            
        #State of the program after the  for loop has been executed: `A` is a 2D list of integers (dimensions n x m), `B` is a 2D list of zeros (dimensions n x m), `n` is at least 2, `m` is between 2 and 50, `ops` is a list with up to 2500 entries; all entries in `ops` have been printed. If `ops` is empty, the loop does not execute and the state of `ops` is an empty list.
    #State of the program after the if-else block has been executed: *`A` is a 2D list of integers with dimensions n x m, `B` is a 2D list of zeros with dimensions n x m, `n` is at least 2, and `m` is between 2 and 50. If the length of `ops` is greater than 2500, -1 is printed. Otherwise, `ops` contains up to 2500 entries, all of which have been printed. If `ops` is empty, no entries are printed and `ops` remains an empty list.
#Overall this is what the function does:The function accepts two integers, n and m, representing the dimensions of a 2D list A, and reads this list from input. It initializes a list called ops to store coordinates where certain conditions regarding the adjacent elements of A are met. Specifically, for all pairs of adjacent 2x2 submatrices within A, if at least one of the four corners contains a 1, the coordinates of the bottom-right corner (i + 1, j + 1) are added to ops. After iterating through the potential submatrices, if ops contains more than 2500 entries, the function prints -1; otherwise, it prints the length of ops and then each coordinate stored in ops. Thus, the function either indicates a failure condition (when ops is too long) or provides information on the positions of the found conditions, while the state of A remains unchanged throughout. In case no valid positions are found, ops will be empty and the function will print 0. The function also doesn't handle any incorrect input scenarios or edge cases related to invalid dimensions or non-integer values.

