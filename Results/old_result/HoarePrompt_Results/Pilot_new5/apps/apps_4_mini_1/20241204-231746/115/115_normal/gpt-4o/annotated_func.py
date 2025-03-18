#State of the program right berfore the function call: n and m are integers such that 2 <= n, m <= 50, and A is a 2D list of integers containing exactly n rows and m columns, where each element is either 0 or 1.
def func_1(n, m, A):
    operations = []
    B = [([0] * m) for _ in range(n)]
    for i in range(n - 1):
        for j in range(m - 1):
            if A[i][j] == 1 and A[i][j + 1] == 1 and A[i + 1][j] == 1 and A[i + 1][
                j + 1] == 1:
                B[i][j] = B[i][j + 1] = B[i + 1][j] = B[i + 1][j + 1] = 1
                operations.append((i + 1, j + 1))
        
    #State of the program after the  for loop has been executed: `n` and `m` are integers such that 2 <= `n` <= 50 and 2 <= `m` <= 50; `B` reflects the counts of all identified 2x2 blocks of 1s from `A`, `operations` is a list of tuples containing the positions of those blocks in 1-based indexing. If no 2x2 blocks are found, `B` remains a 2D list of zeros and `operations` is empty.
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return -1
        
    #State of the program after the  for loop has been executed: `n` is at least 2, `m` is at least 2, `i` is `n`, `j` is `m`, and all elements A[i][j] are equal to B[i][j] for all i in range [0, n-1] and j in range [0, m-1]. If any A[i][j] is not equal to B[i][j], the function would have returned -1.
    print(len(operations))
    for op in operations:
        print(op[0], op[1])
        
    #State of the program after the  for loop has been executed: `n` is at least 2, `m` is at least 2, `i` is `n`, `j` is `m`, all elements A[i][j] are equal to B[i][j] for all i in range [0, n-1] and j in range [0, m-1], length of `operations` is the total number of printed operations, and the printed output consists of all elements in `operations`.
#Overall this is what the function does:The function accepts two integers `n` and `m`, and a 2D list `A` of integers consisting of 0s and 1s. It identifies all 2x2 blocks of 1s in `A`, marking their positions in a new 2D list `B`. If any element in `A` does not match the corresponding element in `B`, the function returns -1. If all elements match, it prints the number of identified 2x2 blocks and their 1-based positions. The function does not return any value other than -1 for discrepancies, and it assumes `n` and `m` are always within the specified range.

