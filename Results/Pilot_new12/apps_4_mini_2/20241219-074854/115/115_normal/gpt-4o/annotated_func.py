#State of the program right berfore the function call: n and m are integers such that 2 <= n, m <= 50, and A is a 2D list of integers where each integer is either 0 or 1, with dimensions n x m.
def func_1(n, m, A):
    operations = []
    B = [([0] * m) for _ in range(n)]
    for i in range(n - 1):
        for j in range(m - 1):
            if A[i][j] == 1 and A[i][j + 1] == 1 and A[i + 1][j] == 1 and A[i + 1][
                j + 1] == 1:
                B[i][j] = B[i][j + 1] = B[i + 1][j] = B[i + 1][j + 1] = 1
                operations.append((i + 1, j + 1))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= `n` <= 50, `m` is an integer such that 2 <= `m` <= 50, `A` is a 2D list of integers with dimensions `n x m`, `operations` contains tuples for each found 2x2 block of 1s in `A`; `B` contains 1s in positions corresponding to all found 2x2 blocks, otherwise `B` remains a 2D list of integers with elements all 0.
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return -1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= `n` <= 50, `m` is an integer such that 2 <= `m` <= 50, `A` is a 2D list of integers where all elements are equal to 0, `B` is a 2D list of integers with all elements equal to 0, `i` is equal to `n`, `j` is equal to `m`, indicating that all corresponding elements in `A` and `B` are equal. The loop has verified that for every position `(i, j)`, `A[i][j]` equals `B[i][j]`, confirming that both arrays are completely filled with zeros.
    print(len(operations))
    for op in operations:
        print(op[0], op[1])
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= `n` <= 50, `m` is an integer such that 2 <= `m` <= 50, `A` is a 2D list of integers where all elements are equal to 0, `B` is a 2D list of integers with all elements equal to 0, `i` is `n`, `j` is `m`, `operations` is defined and contains elements of variable length; all elements in `operations` are printed sequentially for each iteration, until the last element is reached, with the loop executed exactly `len(operations)` times.
#Overall this is what the function does:The function `func_1` takes three parameters: two integers `n` and `m`, and a 2D list `A` of integers (either 0 or 1) with dimensions `n x m`, where `2 <= n, m <= 50`. It identifies all 2x2 blocks within `A` that are filled with 1s and logs their top-left coordinates in the `operations` list. After scanning through the input list `A`, the function creates a new list `B` to represent these blocks, marking their positions with 1s. It then compares `A` with `B`. If any element in `A` does not match the corresponding element in `B`, the function returns -1, indicating an inconsistency. Ultimately, the function only ever returns -1 regardless of the input, and it also prints the count of found 2x2 blocks of 1s and their coordinates, but these outputs do not influence the return value. Additionally, the implementation does not handle cases where `A` does not contain any 2x2 blocks or if it contains any 1s, as it every time returns -1 under the current logic.

