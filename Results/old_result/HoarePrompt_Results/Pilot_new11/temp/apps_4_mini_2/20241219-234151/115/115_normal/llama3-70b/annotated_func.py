#State of the program right berfore the function call: n and m are integers such that 2 <= n, m <= 50; A is a 2D list of integers with dimensions n x m, where each element is either 0 or 1.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 50, `m` is an integer between 2 and 50, `A` is a 2D list of integers with dimensions `n` x `m`, and `ops` contains tuples `(i + 1, j + 1)` for each position where at least one of `A[i][j]`, `A[i + 1][j]`, `A[i][j + 1]`, or `A[i + 1][j + 1]` is equal to 1. If no such positions are found, `ops` will be an empty list.
    if (len(ops) > 2500) :
        print(-1)
    else :
        print(len(ops))
        for op in ops:
            print(op[0], op[1])
            
        #State of the program after the  for loop has been executed: `n` is an integer between 2 and 50, `m` is an integer between 2 and 50, `A` is a 2D list of integers with dimensions `n x m`, `ops` contains all valid tuples `(i + 1, j + 1)` where at least one of `A[i][j]`, `A[i + 1][j]`, `A[i][j + 1]`, or `A[i + 1][j + 1]` is equal to 1, and the printed output consists of all `op[0], op[1]` pairs from every tuple in `ops`.
    #State of the program after the if-else block has been executed: *`n` and `m` are integers between 2 and 50, `A` is a 2D list of integers with dimensions `n` x `m`, and `ops` contains tuples `(i + 1, j + 1)` for positions where at least one of `A[i][j]`, `A[i + 1][j]`, `A[i][j + 1]`, or `A[i + 1][j + 1]` is equal to 1. If the length of `ops` is greater than 2500, -1 is printed; otherwise, all pairs `op[0]` and `op[1]` from each tuple in `ops` are printed.
#Overall this is what the function does:The function processes a 2D list `A` of integers with dimensions `n x m`, where `n` and `m` are integers between 2 and 50, and each element is either 0 or 1. It identifies positions in a 2x2 section of the list where at least one of the elements is 1 and stores the 1-based coordinates of those positions in the list `ops`. If the count of identified positions exceeds 2500, it prints -1; otherwise, it prints the count of valid positions followed by the coordinates of each position stored in `ops`. The function does not handle cases where the input does not comply with the specified constraints, nor does it validate the content of the input list `A` beyond the assumption that it contains integers 0 and 1.

