#State of the program right berfore the function call: The function takes no arguments, but the input is given through a series of read operations where the first line contains two integers n and m (2 <= n, m <= 50), and then n lines follow, each containing m integers. The j-th integer in the i-th line is either 0 or 1.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 50, `m` is an integer between 2 and 50, `A` is a list of `n` sublists of input integers with length at least `m`, `ops` is a list of tuples `(row, column)` representing the positions where any of the values `A[row - 1][column - 1]`, `A[row - 1][column]`, `A[row][column - 1]`, or `A[row][column]` is 1, unless all four values are 1, for `row` in the range `1` to `n` and `column` in the range `1` to `m`. If `n` is less than 2 or `m` is less than 2, `ops` is an empty list.
    if (len(ops) > 2500) :
        print(-1)
    else :
        print(len(ops))
        for op in ops:
            print(op[0], op[1])
            
        #State of the program after the  for loop has been executed: `n` is an integer between 2 and 50, `m` is an integer between 2 and 50, `A` is a list of `n` sublists of input integers with length at least `m`, `ops` is a list of tuples `(row, column)` with length less than or equal to 2500, and all operations in `ops` have been printed.
    #State of the program after the if-else block has been executed: `n` is an integer between 2 and 50, `m` is an integer between 2 and 50, `A` is a list of `n` sublists of input integers with length at least `m`, if the length of `ops` is more than 2500, the value -1 has been printed, otherwise, all operations in `ops` have been printed.
#Overall this is what the function does:The function reads input through a series of operations, starting with two integers `n` and `m`, followed by `n` lines of `m` integers (0 or 1), and then identifies positions where at least one of the four adjacent values (up, down, left, right) is 1, unless all four values are 1. It prints the count of such positions if it's less than or equal to 2500, along with the positions themselves. If the count exceeds 2500, it prints -1. The function does not return any value, it only prints the results. The input values `n` and `m` must be between 2 and 50. The function does not handle cases where `n` or `m` is outside this range, or where the input values are not 0 or 1, as this is not specified in the provided code. It only checks for the specified condition within the given input range. The function's output is printed to the console, and its state after execution includes the printed output and the input values `n`, `m`, and the list `A`, but these are not returned or further processed.

