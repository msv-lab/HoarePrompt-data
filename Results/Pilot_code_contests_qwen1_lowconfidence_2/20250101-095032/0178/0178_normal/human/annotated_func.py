#State of the program right berfore the function call: The input is given as a list of n strings, where each string represents a row of the n × n board and contains n space-separated integers. Each integer on the board is within the range [1, 100], and n is within the range [1, 30].
def func():
    n = int(input())
    T = [[(0) for loop in range(n)] for i in range(n)]
    for loop in range(n):
        T[loop] = list(map(int, raw_input().split(' ')))
        
    #State of the program after the  for loop has been executed: `T` is an `n x n` matrix where each element is an integer. For every row `i` (0 ≤ i < n), `T[i]` contains a list of integers `[int(a1), int(a2), ..., int(an)]`, where `a1, a2, ..., an` are the integers entered in the corresponding input lines during the loop iterations. The loop does not execute if `n` is 0.
    lig = [(0) for loop in range(n)]
    for i in range(n):
        for j in range(n):
            lig[i] += T[i][j]
        
    #State of the program after the  for loop has been executed: `lig[i]` is the sum of all elements in the `i`-th row of matrix `T` for every `i` in the range `[0, n-1]`, `i` is `n`, `j` is `n`, and `n` is a positive integer.
    col = [(0) for loop in range(n)]
    for i in range(n):
        for j in range(n):
            col[i] += T[j][i]
        
    #State of the program after the  for loop has been executed: `col[i]` is the sum of all elements `T[j][i]` for all `j` in the range `[0, n-1]`, `i` is `n`, `j` is `n`, `n` is a positive integer.
    compt = 0
    for i in range(n):
        for j in range(n):
            if col[i] > lig[j]:
                compt += 1
        
    #State of the program after the  for loop has been executed: `col[i]` is the sum of all elements `T[j][i]` for all `j` in the range [0, n-1], `i` is `n`, `j` is `n`, `n` is a positive integer, `compt` is the count of indices `j` for which `col[i] > lig[j]` for all `i` in the range [0, n-1].
    print(compt)
#Overall this is what the function does:The function processes an \( n \times n \) board represented as a list of \( n \) strings, where each string contains \( n \) space-separated integers. It calculates the sum of each row and each column in the board. Then, it counts the number of times the sum of a column is greater than the sum of any row. If \( n \) is 0, the function does nothing and does not produce any output. If \( n \) is less than or equal to 30, the function prints the count of such instances.

