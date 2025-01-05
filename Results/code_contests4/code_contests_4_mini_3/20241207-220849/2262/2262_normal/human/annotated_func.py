#State of the program right berfore the function call: t is an integer representing the number of test cases (1 ≤ t ≤ 100), n is an integer representing the size of the grid (1 ≤ n ≤ 300), and the grid is represented as a list of n strings, each containing n characters, where each character is either '.' or 'X'. The sum of n across all test cases does not exceed 300.
def func_1():
    return int(input())
    #The program returns an integer input representing the number of test cases, which is t (1 ≤ t ≤ 100)
#Overall this is what the function does:The function accepts no parameters and returns an integer representing the number of test cases, t, which must be input by the user and is constrained to be between 1 and 100.

#State of the program right berfore the function call: t is an integer (1 ≤ t ≤ 100) representing the number of test cases, n is an integer (1 ≤ n ≤ 300) representing the size of the grid for each test case, and the grid is represented as a list of n strings, each containing exactly n characters which are either '.' or 'X'. The character 'O' does not appear in the grid for the easy version. The total sum of n across all test cases does not exceed 300.
def func_2():
    return list(map(int, input().split()))
    #The program returns a list of integers generated from user input, where each integer is derived from space-separated values entered as a string.
#Overall this is what the function does:The function accepts no parameters and returns a list of integers generated from space-separated values entered as a string by the user. It does not handle any validation for the input, so if the input is not properly formatted or contains non-integer values, it may raise an error.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, n is an integer such that 1 ≤ n ≤ 300 for each test case, and the grid consists of n lines, each containing a string of n characters which are either '.' or 'X'. It is guaranteed that not all cells in the grid are empty.
def func_3():
    s = input()
    return list(s[:len(s) - 1])
    #The program returns a list containing the characters of the string 's' excluding the last character.
#Overall this is what the function does:The function does not accept any parameters and reads a string input from the user. It returns a list containing the characters of the string excluding the last character. This could lead to an empty list if the input string has only one character.

#State of the program right berfore the function call: t is an integer between 1 and 100, n is an integer between 1 and 300 for each test case, and the grid consists of n strings of length n containing only the characters 'X' or '.' (with at least one 'X' present). The total sum of n across all test cases does not exceed 300.
def func_4():
    s = input()
    return s[:len(s) - 1]
    #The program returns the string 's' excluding its last character
#Overall this is what the function does:The function accepts no parameters, reads a string input from the user, and returns the string excluding its last character. If the input string is empty, it will return an empty string as well.

#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 100) representing the number of test cases; for each test case, n is a positive integer (1 ≤ n ≤ 300) representing the size of the grid; the grid consists of n strings, each containing n characters which are either '.' or 'X', and it is guaranteed that at least one cell is not empty. The total sum of n across all test cases does not exceed 300.
def func_5():
    n = func_1()
    M = []
    k = 0
    for _ in xrange(n):
        M.append(func_3())
        
        k += sum([(1) for x in M[-1] if x in 'XO'])
        
    #State of the program after the  for loop has been executed: `t` is a positive integer (1 ≤ `t` ≤ 100), `n` is a positive integer (1 ≤ `n` ≤ 300), `M` is a list containing the return values of `func_3()` called `n` times, `k` is equal to the total count of 'X' and 'O' across all elements in `M`.
    K = int(k / 3.0)
    clr = dict()
    cnt = [0] * 3
    for i in xrange(n):
        for j in xrange(n):
            if M[i][j] == 'X':
                clr[i, j] = (i + j) % 3
                cnt[(i + j) % 3] += 1
            else:
                clr[i, j] = -1
        
    #State of the program after the  for loop has been executed: `t` is a positive integer (1 ≤ `t` ≤ 100), `n` is a positive integer (1 ≤ `n` ≤ 300), `M` is a list containing the return values of `func_3()` called `n` times, `k` is equal to the total count of 'X' and 'O' across all elements in `M`, `K` is equal to int(k / 3.0), `clr` contains entries for all elements in the matrix `M`, where each entry is either (i + j) % 3 if `M[i][j]` is 'X' or -1 if `M[i][j]` is not 'X', and `cnt` contains the counts of 'X' in `M` categorized by the values of (i + j) % 3 across all rows and columns of `M`.
    use_clr = 0
    while use_clr < 3 and (cnt[use_clr] > K or cnt[use_clr] == 0):
        use_clr += 1
        
    #State of the program after the loop has been executed: `t` is a positive integer, `n` is a positive integer, `M` is a list containing return values, `k` is equal to the total count of 'X' and 'O', `K` is equal to int(k / 3.0), `cnt[0]`, `cnt[1]`, and `cnt[2]` are adjusted to be less than or equal to `K` and at least one of them is equal to 0, `use_clr` is equal to 3.
    chg = 0
    for i in xrange(n):
        for j in xrange(n):
            if clr[i, j] == use_clr:
                M[i][j] = 'O'
                chg += 1
        
    #State of the program after the  for loop has been executed: `t` is a positive integer, `n` is a positive integer, `M` is a list containing 'O' at all positions where `clr[i, j]` equals `use_clr`, `k` is equal to the total count of 'X' and 'O', `K` is equal to int(k / 3.0), `cnt[0]`, `cnt[1]`, and `cnt[2]` are less than or equal to `K` and at least one of them is equal to 0, `use_clr` is equal to 3, `chg` is the total count of assignments made to 'O'.
    for i in xrange(n):
        print(''.join(M[i]))
        
    #State of the program after the  for loop has been executed: `t` is a positive integer, `n` is greater than or equal to 0, `M` is a list containing 'O' at all positions where `clr[i, j]` equals `use_clr`, `k` is equal to the total count of 'X' and 'O', `K` is equal to int(k / 3.0), `cnt[0]`, `cnt[1]`, and `cnt[2]` are less than or equal to `K` and at least one of them is equal to 0, `use_clr` is equal to 3, `chg` is the total count of assignments made to 'O', `i` is `n-1`; the output is the concatenation of the elements in `M` for all indices from 0 to `n-1`.
#Overall this is what the function does:The function processes a grid of characters ('X' and '.') for multiple test cases, converting specific 'X' characters to 'O' based on a calculated value. It aims to ensure that the counts of 'X' are distributed evenly across three categories derived from their indices, while ensuring at least one category has no 'X's. The output is the modified grid printed as strings, but the function does not handle cases where the grid is entirely empty or consists only of 'O' characters.

