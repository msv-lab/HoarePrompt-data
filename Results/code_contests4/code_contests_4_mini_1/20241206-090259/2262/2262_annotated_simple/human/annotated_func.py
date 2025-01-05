#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, n is an integer such that 1 ≤ n ≤ 300. The grid consists of n strings, each containing n characters where each character is either '.' or 'X'. It is guaranteed that not all cells are empty and the character 'O' does not appear in the input. The total number of characters across all test cases does not exceed 300.
def func_1():
    return int(input())
    #The program returns an integer value input by the user, which is within the range of 1 to 100 for 't' and 1 to 300 for 'n'.
#Overall this is what the function does:The function accepts an integer input from the user and returns that integer. There are no checks to ensure the input is within the specified range of 1 to 100 for `t` or 1 to 300 for `n`, which means it could potentially return any integer value based on user input.

#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 100) representing the number of test cases; for each test case, n is a positive integer (1 ≤ n ≤ 300) indicating the size of the grid; each grid consists of n strings of length n, containing only the characters 'X' or '.', and at least one cell is not empty. The total sum of n across all test cases does not exceed 300.
def func_2():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained by splitting the input string and converting each part to an integer.
#Overall this is what the function does:The function accepts input from the user, splits that input string into parts, converts each part into an integer, and returns a list of these integers. It does not process any test cases or grids; it simply returns a list of integers based on the direct input provided.

#State of the program right berfore the function call: t is an integer between 1 and 100 inclusive, n is an integer between 1 and 300 inclusive for each test case, and the grid consists of n strings of n characters each, where each character is either '.' or 'X'. The total sum of n across all test cases does not exceed 300.
def func_3():
    s = input()
    return list(s[:len(s) - 1])
    #The program returns a list containing all characters of the string 's' except the last character.
#Overall this is what the function does:The function accepts no parameters and returns a list containing all characters of the input string `s` except the last character. If `s` is an empty string, it returns an empty list.

#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 100) representing the number of test cases, and for each test case, n is a positive integer (1 ≤ n ≤ 300) representing the size of the grid. The grid consists of n strings, each containing n characters, where each character is either '.' (empty cell) or 'X' (token), and 'O' does not appear in the input. The total number of cells across all test cases is guaranteed not to exceed 300.
def func_4():
    s = input()
    return s[:len(s) - 1]
    #The program returns the string `s` with the last character removed, where `s` represents a row of the grid consisting of `n` characters, each being either '.' or 'X'
#Overall this is what the function does:The function accepts a string input `s` and returns the string with the last character removed. It does not handle any edge cases for an empty string or any specific characters since it directly removes the last character regardless of the content of `s`.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; n is an integer such that 1 ≤ n ≤ 300 for each test case; the grid consists of n strings of length n, where each character is either '.' or 'X', and it is guaranteed that not all cells are empty; the sum of n across all test cases does not exceed 300.
def func_5():
    n = func_1()
    M = []
    k = 0
    for _ in xrange(n):
        M.append(func_3())
        
        k += sum([(1) for x in M[-1] if x in 'XO'])
        
    #State of the program after the  for loop has been executed: `t` is an integer such that 1 ≤ `t` ≤ 100, `n` is an integer such that 1 ≤ `n` ≤ 300, `M` is a list containing `n` results from `func_3()`, `k` is the total count of 'X' and 'O' in all elements of `M`.
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
        
    #State of the program after the  for loop has been executed: `t` is an integer such that 1 ≤ `t` ≤ 100; `n` is an integer such that 1 ≤ `n` ≤ 300; `cnt` is updated to reflect the counts of 'X' found in `M`; `clr` is a dictionary with keys (i, j) for all i, j in range(n) with values as `(i + j) % 3` for 'X' or -1 for non-'X' entries.
    use_clr = 0
    while use_clr < 3 and (cnt[use_clr] > K or cnt[use_clr] == 0):
        use_clr += 1
        
    #State of the program after the loop has been executed: `use_clr` is 3, and `cnt[0]`, `cnt[1]`, and `cnt[2]` must all be less than or equal to K for the loop to terminate. `t` is an integer between 1 and 100, `n` is an integer between 1 and 300.
    chg = 0
    for i in xrange(n):
        for j in xrange(n):
            if clr[i, j] == use_clr:
                M[i][j] = 'O'
                chg += 1
        
    #State of the program after the  for loop has been executed: `use_clr` is 3, `cnt[0]`, `cnt[1]`, and `cnt[2]` are all less than or equal to K, `t` is between 1 and 100, `n` is an integer between 1 and 300, `chg` is the total count of all instances where `clr[i, j]` equals `use_clr` across all iterations, and `M[i][j]` is set to 'O' for each corresponding `(i, j)` where this condition holds true.
    for i in xrange(n):
        print(''.join(M[i]))
        
    #State of the program after the  for loop has been executed: `M[i]` contains rows of 'O's for each `i` from 0 to `n-1` based on `clr[i, j]` equaling `use_clr`, `cnt` remains unchanged, `chg` is the total count of instances where `clr[i, j]` equals `use_clr`.
#Overall this is what the function does:The function does not accept parameters and processes a grid of size n x n consisting of characters '.' and 'X'. It counts the occurrences of 'X' and 'O' in the grid, modifying the grid by replacing some 'X' characters with 'O' based on specific conditions. Finally, it prints the modified grid. The function relies on the output of other functions (`func_1` and `func_3`) to gather input data and does not return any value.

