#State of the program right berfore the function call: n and m are integers such that 2 <= n, m <= 50, and A is a 2D list of integers where each element is either 0 or 1, with dimensions n x m.
def func_1(n, m, A):
    operations = []
    B = [([0] * m) for _ in range(n)]
    for i in range(n - 1):
        for j in range(m - 1):
            if A[i][j] == 1 and A[i][j + 1] == 1 and A[i + 1][j] == 1 and A[i + 1][
                j + 1] == 1:
                B[i][j] = B[i][j + 1] = B[i + 1][j] = B[i + 1][j + 1] = 1
                operations.append((i + 1, j + 1))
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 50, `m` is an integer between 2 and 50, `A` is a 2D list of integers with dimensions `n x m`, `B` is a 2D list of integers with dimensions `n x m` where each element is either 0 or 1 indicating the presence of detected 2x2 blocks of 1s from `A`, `operations` contains the coordinates of all detected 2x2 blocks of 1s in `A`, if any were found; if no 2x2 blocks were found, then `operations` remains empty and `B` remains a matrix of zeros.
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return -1
        
    #State of the program after the  for loop has been executed: `n` and `m` are integers between 2 and 50, `i` is `n - 1`, `j` is `m - 1`, and all values of `A[i][j]` are equal to the corresponding values of `B[i][j]` for all valid indices, indicating that all elements in the 2D list `A` are equal to those in the 2D list `B`. If no discrepancies were found, the function completes successfully without errors.
    print(len(operations))
    for op in operations:
        print(op[0], op[1])
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 50, `m` is an integer between 2 and 50, `i` is `n - 1`, `j` is `m - 1`, and all elements of `operations` have been printed.
#Overall this is what the function does:The function accepts two integers `n` and `m`, along with a 2D list `A` of dimensions `n x m` filled with integers (0 or 1). It identifies all 2x2 blocks of ones in `A` and records their top-left coordinates in a list called `operations`. If all elements in `A` match the corresponding elements in a newly created 2D list `B` (which is populated based on the identified blocks of ones), it prints the number of found operations and their coordinates. If there are discrepancies between `A` and `B`, the function returns -1. The function does not return any result other than -1 when discrepancies are found, nor does it have specified behavior for the case when no blocks are found.

