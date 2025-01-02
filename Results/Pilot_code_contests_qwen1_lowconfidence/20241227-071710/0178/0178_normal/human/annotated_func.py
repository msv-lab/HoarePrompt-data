#State of the program right berfore the function call: The input is provided as a string representing the first line containing an integer n (1 ≤ n ≤ 30), followed by n lines, each containing n space-separated integers. Each integer on the board is in the range from 1 to 100.
def func():
    n = int(input())
    T = [[(0) for loop in range(n)] for i in range(n)]
    for loop in range(n):
        T[loop] = list(map(int, raw_input().split(' ')))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `T` is an \( n \times n \) 2D list where the first `n` rows are lists of integers read from input and all other elements in \( T \) are 0, `loop` is `n-1`.
    lig = [(0) for loop in range(n)]
    for i in range(n):
        for j in range(n):
            lig[i] += T[i][j]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `T` is an \( n \times n \) 2D list where the first `n` rows are lists of integers read from input and all other elements in \( T \) are 0, `loop` is `n-1`, `lig` is a list of `n` elements where each element `lig[i]` is the sum of all elements in the `i`-th row of the matrix `T`.
    col = [(0) for loop in range(n)]
    for i in range(n):
        for j in range(n):
            col[i] += T[j][i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `T` is an \( n \times n \) 2D list, `loop` is `n-1`, `lig` is a list of sums of rows, `col` is a list of sums of columns where each element `col[i]` is the sum of all elements in the \( i \)-th column of the matrix \( T \).
    compt = 0
    for i in range(n):
        for j in range(n):
            if col[i] > lig[j]:
                compt += 1
        
    #State of the program after the  for loop has been executed: `i` is `n`, `n` is a positive integer, `compt` is the count of elements in `lig` that are less than their corresponding `col[i]` for all `i` from `0` to `n-1`, `j` is `n-1`, and the loop has executed `n^2` times.
    print(compt)
#Overall this is what the function does:The function reads an \( n \times n \) matrix from the input, where \( n \) is an integer between 1 and 30, and each element in the matrix is an integer between 1 and 100. It then calculates the sum of each row and each column. Afterward, it counts the number of elements in the row sums (`lig`) that are less than the corresponding column sums (`col`). Finally, it prints the count. Potential edge cases include the minimum and maximum values of \( n \) (1 and 30). If the input does not follow the specified format, the function may raise an exception due to incorrect data types or out-of-range values.

