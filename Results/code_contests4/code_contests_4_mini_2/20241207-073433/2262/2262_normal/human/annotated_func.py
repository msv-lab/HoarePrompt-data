#State of the program right berfore the function call: t is an integer representing the number of test cases (1 ≤ t ≤ 100), n is an integer representing the size of the grid for each test case (1 ≤ n ≤ 300), and each grid is represented by n strings of length n containing characters '.' or 'X', with at least one cell not empty. The total sum of n across all test cases does not exceed 300.
def func_1():
    return int(input())
    #The program returns an integer input value that represents the number of test cases 't'
#Overall this is what the function does:The function accepts no parameters and returns an integer that represents the number of test cases `t`, as input by the user. It does not handle any edge cases related to input validation, so if the input is not a valid integer, it may raise an error.

#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 100) representing the number of test cases; for each test case, n is a positive integer (1 ≤ n ≤ 300) indicating the size of the grid, followed by n strings of length n, each containing characters '.', 'X', or 'O', where 'O' is not present in the easy version. The total size of all grids combined does not exceed 300.
def func_2():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained by mapping the input strings split by spaces into integers
#Overall this is what the function does:The function accepts input from the user, which is expected to be a series of space-separated integers, and returns a list of these integers. It does not directly interact with the parameters `t` or `n`, as there is no functionality implemented to handle multiple test cases, grids, or the specific characters mentioned in the annotations. The function simply processes the input and outputs a list of integers derived from that input.

#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 100) representing the number of test cases, n is a positive integer (1 ≤ n ≤ 300) representing the size of the grid for each test case, and the grid consists of n strings, each containing exactly n characters which are either '.' or 'X'. The total sum of n across all test cases does not exceed 300.
def func_3():
    s = input()
    return list(s[:len(s) - 1])
    #The program returns a list containing all characters of the string 's' except the last character, which is a row of the grid with exactly n characters that are either '.' or 'X'.
#Overall this is what the function does:The function accepts no parameters and reads a string input `s`, returning a list containing all characters of the string except the last character. This effectively excludes the final character of the input string from the returned list. If the input string is empty, the function will return an empty list.

#State of the program right berfore the function call: t is an integer with 1 ≤ t ≤ 100, n is an integer with 1 ≤ n ≤ 300 for each test case, and the grid consists of n strings of length n containing only the characters 'X' or '.' (no 'O' characters allowed), with at least one non-empty cell. The sum of n across all test cases does not exceed 300.
def func_4():
    s = input()
    return s[:len(s) - 1]
    #The program returns the string 's' excluding its last character
#Overall this is what the function does:The function accepts no parameters and returns the input string `s` excluding its last character. It does not handle cases where the input string is empty, which may lead to unexpected behavior. If the input string is a single character, the function will return an empty string.

#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 100) representing the number of test cases, and for each test case, n is a positive integer (1 ≤ n ≤ 300) representing the size of the grid. The grid consists of n strings, each containing n characters that are either '.' or 'X'. It is guaranteed that not all cells are empty across the test cases, and the total sum of n does not exceed 300.
def func_5():
    n = func_1()
    M = []
    k = 0
    for _ in xrange(n):
        M.append(func_3())
        
        k += sum([(1) for x in M[-1] if x in 'XO'])
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `M` is a list containing the results of `func_3()` executed `n` times, `k` is the total count of 'X' and 'O' in all elements of `M`, `_` is `n`.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `clr` contains assigned values based on whether each element of `M` was 'X' or not for all indices, and `cnt` contains the counts of how many times `(i + j) % 3` was incremented for each `i` and `j` in that range.
    use_clr = 0
    while use_clr < 3 and (cnt[use_clr] > K or cnt[use_clr] == 0):
        use_clr += 1
        
    #State of the program after the loop has been executed: `use_clr` is 3, `n` is a positive integer, `cnt[0]`, `cnt[1]`, and `cnt[2]` must be such that `cnt[0]` is greater than K or `cnt[0]` is equal to 0, `cnt[1]` is greater than K or `cnt[1]` is equal to 0, and `cnt[2]` allows the loop to terminate since `use_clr` cannot increment further.
    chg = 0
    for i in xrange(n):
        for j in xrange(n):
            if clr[i, j] == use_clr:
                M[i][j] = 'O'
                chg += 1
        
    #State of the program after the  for loop has been executed: `use_clr` is 3, `n` is a positive integer, `i` is `n`, `j` is `n`, `M[i][j]` is 'O' where `clr[i, j]` equals `use_clr` for all occurrences, and `chg` is the total count of all occurrences of `use_clr` in the `clr` matrix.
    for i in xrange(n):
        print(''.join(M[i]))
        
    #State of the program after the  for loop has been executed: `use_clr` is 3, `n` is a positive integer, `i` is `n`, `j` is `n`, and the output is a string formed by joining the elements of each list in M for all indices from 0 to n-1.
#Overall this is what the function does:The function processes multiple test cases of grid configurations, where each grid consists of characters 'X' and '.'. For each grid, it counts the occurrences of 'X' and assigns a color based on the grid coordinates. It then determines which color to use for conversion based on certain conditions and replaces the corresponding 'X' characters with 'O'. Finally, it prints the modified grid. The function does not return any values; it only outputs the modified grids directly.

