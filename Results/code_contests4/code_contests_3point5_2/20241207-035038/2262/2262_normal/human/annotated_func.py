#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 100). n is a positive integer (1 ≤ n ≤ 300). The input grid contains characters '.' (empty cell) or 'X' (token type). The character 'O' does not appear in the input in the easy version.**
def func_1():
    return int(input())
    #The program returns the integer value obtained from the input
#Overall this is what the function does:The function func_1 reads an integer from the input and returns that integer value.

#State of the program right berfore the function call: t is a positive integer. n is a positive integer less than or equal to 300. Each character in the grid is either '.' or 'X'.**
def func_2():
    return list(map(int, input().split()))
    #The program returns a list of integers created by mapping the input split by spaces to integers
#Overall this is what the function does:The function does not accept any parameters. It reads user input consisting of a positive integer t, a positive integer n less than or equal to 300, and a grid of characters '.' or 'X'. It then returns a list of integers created by mapping the input split by spaces to integers.

#State of the program right berfore the function call: # Precondition

**t is a positive integer representing the number of test cases.**
**n is a positive integer representing the size of the grid for each test case.**
**The grid for each test case is represented by an n x n matrix where each cell contains either '.', 'X', or 'O'.**
**The character 'O' does not appear in the input of the easy version.**
def func_3():
    s = input()
    return list(s[:len(s) - 1])
    #The program returns a list containing the input for each test case represented by an n x n matrix where each cell contains either '.', 'X', or 'O'
#Overall this is what the function does:The function `func_3` reads an input string, removes the last character from it, and returns the modified string as a list. The input string represents the input for each test case, which is an n x n matrix where each cell contains either '.', 'X', or 'O'. The character 'O' does not appear in the input of the easy version.

#State of the program right berfore the function call: t is a positive integer. n is a positive integer such that 1 <= n <= 300. Each cell in the grid is either empty (denoted by '.') or contains a token (either 'X' or 'O'). The sum of n across all test cases does not exceed 300.**
def func_4():
    s = input()
    return s[:len(s) - 1]
    #The program returns the string s without the last character
#Overall this is what the function does:The function `func_4` takes an input string `s` and returns the string without the last character.

#State of the program right berfore the function call: t is a positive integer. n is a positive integer less than or equal to 300. The input grid contains characters '.', 'X', and 'O', with 'O' not appearing in the input of the easy version.**
def func_5():
    n = func_1()
    M = []
    k = 0
    for _ in xrange(n):
        M.append(func_3())
        
        k += sum([(1) for x in M[-1] if x in 'XO'])
        
    #State of the program after the  for loop has been executed: t is a positive integer, n is greater than 0, input grid contains characters '.', 'X', and 'O' with 'O' not appearing in the input of the easy version, k is the total sum of occurrences of 'X' in all elements of M, M contains the return values of func_3() for each iteration of the loop
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
        
    #State of the program after the  for loop has been executed: `clr` is a dictionary with key-value pairs (i, j) -> (i + j) % 3 if M[i][j] == 'X', otherwise (i, j) -> -1. `cnt` is a list with 3 elements, where each element represents the count of occurrences of 0, 1, and 2 respectively based on the values of (i + j) % 3. `i` remains 0, `n` is the same as the initial value, and `j` is equal to n for the loop to finish.
    use_clr = 0
    while use_clr < 3 and (cnt[use_clr] > K or cnt[use_clr] == 0):
        use_clr += 1
        
    #State of the program after the loop has been executed: `clr` remains unchanged, `cnt` remains unchanged, `i` remains 0, `n` remains the same as the initial value, `j` remains equal to n, `use_clr` is updated to 3 after the loop finishes
    chg = 0
    for i in xrange(n):
        for j in xrange(n):
            if clr[i, j] == use_clr:
                M[i][j] = 'O'
                chg += 1
        
    #State of the program after the  for loop has been executed: `clr` remains unchanged, `cnt` remains unchanged, `i` is equal to `n-1`, `n` is the same as the initial value, `j` is equal to `n`, `use_clr` is 3, `chg` is equal to the total number of times `clr[i, j] == use_clr` for all `j` in `xrange(n)`, all positions `(i, j)` in `clr` where `clr[i, j] == use_clr` have been updated to 'O' in `M`
    for i in xrange(n):
        print(''.join(M[i]))
        
    #State of the program after the  for loop has been executed: The loop will print each row of matrix M as a string until i reaches n-1, then it will stop. All other variables remain unchanged.
#Overall this is what the function does:The function `func_5` initializes a matrix `M` based on the return values of another function `func_3`. It then calculates the total occurrences of 'X' in `M` and assigns colors 'O' based on a specific condition. The function prints the modified matrix `M` row by row. The key functionality is updating the matrix `M` based on the color condition and printing it. The function does not accept any parameters and does not have a return value.

