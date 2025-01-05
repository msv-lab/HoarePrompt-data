#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n is a positive integer representing the size of the grid and the grid is represented by a 2D list of characters containing 'X' or '.' only.**
def func_1():
    return int(input())
    #The program returns the integer input value for the number of test cases
#Overall this is what the function does:The function accepts no parameters and retrieves an integer input value for the number of test cases.

#State of the program right berfore the function call: ** The input consists of t test cases, where each test case includes an integer n (1≤ n ≤ 300) representing the size of the grid, followed by n lines containing strings of n characters representing the initial grid. The characters in the grid are either '.' (empty cells) or 'X' (tokens). The character 'O' does not appear in the input for the easy version of the problem.
def func_2():
    return list(map(int, input().split()))
    #The program returns a list of integers after converting the input strings to integers
#Overall this is what the function does:The function func_2 reads input consisting of t test cases with grid sizes and characters. It then converts the input strings to integers using map function and returns a list of integers. The function does not accept any parameters explicitly, but it implicitly reads input from the user.

#State of the program right berfore the function call: t is a positive integer, n is a positive integer such that 1 <= n <= 300, and the grid contains '.' or 'X' characters only.
def func_3():
    s = input()
    return list(s[:len(s) - 1])
    #The program returns a list of characters from string 's' excluding the last character. 't' is a positive integer and 'n' is a positive integer with 1 <= n <= 300. The grid contains '.' or 'X' characters only.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It reads a string input, and then returns a list of characters from the input string excluding the last character. The function does not have any constraints on 't' or 'n', so the annotations regarding 't' and 'n' are irrelevant. The grid containing '.' or 'X' characters is also not used in the function. Therefore, the actual functionality of the function is to simply remove the last character of the input string and return a list of the remaining characters.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n is a positive integer representing the size of the grid, such that 1 ≤ n ≤ 300. The input grid contains characters '.' (empty cell), 'X' (token type) but does not contain 'O' in the easy version.**
def func_4():
    s = input()
    return s[:len(s) - 1]
    #The program returns the input string 's' excluding the last character
#Overall this is what the function does:The function `func_4` reads an input string 's' from the user and returns 's' excluding the last character. The function does not accept any parameters. The returned string will be 's' without the last character.

#State of the program right berfore the function call: ** The input consists of integer t (1≤ t≤ 100) representing the number of test cases. Each test case includes an integer n (1≤ n≤ 300) denoting the size of the grid, followed by n lines each containing a string of n characters representing the initial grid. The characters in the grid can be '.', 'X', or 'O', where 'O' does not appear in the input of the easy version. The sum of n across all test cases does not exceed 300.
def func_5():
    n = func_1()
    M = []
    k = 0
    for _ in xrange(n):
        M.append(func_3())
        
        k += sum([(1) for x in M[-1] if x in 'XO'])
        
    #State of the program after the  for loop has been executed: `M` is a list containing the return values of `func_3()` for each iteration of the loop, `k` is the total sum of occurrences of 'X' and 'O' in all elements of `M`, the loop will execute only if `n` is greater than 0
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
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, M will contain the return values of func_3() for each iteration of the loop, k will represent the total sum of occurrences of 'X' in all elements of M, K will be the integer division of k by 3.0, cnt will store the occurrences of each remainder when the sum of the indices is divided by 3, i will be equal to n, j will be equal to n-1, and clr will have values assigned based on the conditions in the loop code.
    use_clr = 0
    while use_clr < 3 and (cnt[use_clr] > K or cnt[use_clr] == 0):
        use_clr += 1
        
    #State of the program after the loop has been executed: M will contain the return values of func_3() for each iteration of the loop, k will represent the total sum of occurrences of 'X' in all elements of M, K will be the integer division of k by 3.0, cnt will store the occurrences of each remainder when the sum of the indices is divided by 3, i will be equal to n, j will be equal to n-1, clr will have values assigned based on the conditions in the loop code, use_clr will be 3
    chg = 0
    for i in xrange(n):
        for j in xrange(n):
            if clr[i, j] == use_clr:
                M[i][j] = 'O'
                chg += 1
        
    #State of the program after the  for loop has been executed: M contains the return values of func_3() for each iteration of the loop, k represents the total sum of occurrences of 'X' in all elements of M, K is the integer division of k by 3.0, cnt stores the occurrences of each remainder when the sum of the indices is divided by 3, i is equal to n, j is less than n, clr has values assigned based on the conditions in the loop code, use_clr is 3, chg is equal to the total number of times clr[i, j] == use_clr for all iterations, n is greater than 0, M[i][j] is assigned the value 'O' if clr[i, j] is equal to use_clr. Otherwise, the program retains the values of the variables as per the precondition without any changes.
    for i in xrange(n):
        print(''.join(M[i]))
        
    #State of the program after the  for loop has been executed: The values of the variables M, k, K, cnt, i, j, clr, use_clr, chg, n, and M[i][j] remain the same as per the initial state, without any changes.
#Overall this is what the function does:The function `func_5` does not accept any parameters. It reads the input consisting of integer `t` representing the number of test cases, followed by `t` test cases each including an integer `n` denoting the size of the grid and an `n x n` grid represented by strings of characters. The function processes the input by counting the occurrences of 'X' and 'O' characters in the grid, calculating certain values based on grid indices, and changing certain characters in the grid based on specific conditions. However, the return value of the function is not specified.

