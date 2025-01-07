#State of the program right berfore the function call: n and m are integers such that 2 <= n, m <= 50, and A is a 2D list of integers with each element being either 0 or 1, where A has n rows and m columns.
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
        
    #State of the program after the  for loop has been executed: `A` is a 2D list of integers containing 0s and 1s, `n` is an integer from 2 to 50, `m` is an integer from 2 to 50, `ops` contains tuples `(i + 1, j + 1)` for every `(i, j)` pair where at least one of the elements in the positions `A[i][j]`, `A[i + 1][j]`, `A[i][j + 1]`, or `A[i + 1][j + 1]` is equal to 1, for `i` in the range `0` to `n - 2` and `j` in the range `0` to `m - 2`. If no elements in these positions are 1 for all iterations, `ops` remains empty.
    if (len(ops) > 2500) :
        print(-1)
    else :
        print(len(ops))
        for op in ops:
            print(op[0], op[1])
            
        #State of the program after the  for loop has been executed: `A` is a 2D list of integers containing 0s and 1s, `n` is an integer from 2 to 50, `m` is an integer from 2 to 50, `ops` contains tuples `(i + 1, j + 1)` for every `(i, j)` pair where at least one of the elements in positions `A[i][j]`, `A[i + 1][j]`, `A[i][j + 1]`, or `A[i + 1][j + 1]` is equal to 1; `len(ops)` could be 0 if no valid pairs were found, or a positive integer indicating the number of valid operations; the printed values will correspond to all the elements in `ops`, representing each operation performed by the loop.
    #State of the program after the if-else block has been executed: *`A` is a 2D list of integers containing 0s and 1s, `n` is an integer from 2 to 50, `m` is an integer from 2 to 50, `ops` contains tuples `(i + 1, j + 1)` for every `(i, j)` pair where at least one of the elements in positions `A[i][j]`, `A[i + 1][j]`, `A[i][j + 1]`, or `A[i + 1][j + 1]` is equal to 1; if the length of `ops` is greater than 2500, -1 is printed. Otherwise, the printed values will correspond to all the elements in `ops`, indicating each operation performed by the loop, with `len(ops)` potentially being 0 if no valid pairs were found or a positive integer indicating the number of valid operations.
#Overall this is what the function does:Functionality: ** The function accepts two integers, `n` and `m`, and a 2D list `A` of integers (0s and 1s) of size `n x m`. It checks for every 2x2 sub-square within `A` whether at least one of the four positions contains a 1. If the count of such positions (stored in `ops`) exceeds 2500, it prints -1. Otherwise, it prints the count of valid operations and the coordinates of each 2D pair where at least one position within the sub-square contains a 1. If there are no valid positions, it will print 0 and not print any coordinates.

