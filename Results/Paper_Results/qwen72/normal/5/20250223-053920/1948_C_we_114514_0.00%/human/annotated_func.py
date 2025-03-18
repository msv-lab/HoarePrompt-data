#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, representing the number of test cases. test_cases is a list of tuples, where each tuple contains an integer n (2 <= n <= 2 * 10^5 and n is even) and two strings of length n, consisting of characters '<' and '>', representing the first and second rows of the grid, respectively. The sum of n over all test cases does not exceed 2 * 10^5.
def func_1(t, test_cases):
    results = []
    for test_case in test_cases:
        n, (row1, row2) = test_case
        
        reachable_first_row = True
        
        reachable_second_row = False
        
        for j in range(n):
            if reachable_first_row:
                if row1[j] == '>':
                    if j == n - 1:
                        reachable_second_row = True
                else:
                    reachable_first_row = False
                    if j < n - 1 and row2[j] == '>':
                        reachable_second_row = True
            if reachable_second_row:
                if row2[j] == '>':
                    if j == n - 1:
                        reachable_second_row = True
        
        if reachable_second_row:
            results.append('YES')
        else:
            results.append('NO')
        
    #State: results is a list containing 'YES' or 'NO' for each test case, indicating whether it is possible to reach the second row from the first row in the grid. The initial variables t and test_cases remain unchanged.
    return results
    #The program returns a list 'results' containing 'YES' or 'NO' for each test case, indicating whether it is possible to reach the second row from the first row in the grid.
#Overall this is what the function does:The function `func_1` accepts a positive integer `t` and a list `test_cases` of tuples. Each tuple contains an integer `n` and two strings of length `n` with characters '<' and '>'. The function returns a list `results` with 'YES' or 'NO' for each test case, indicating whether it is possible to move from the first row to the second row in the grid. The initial variables `t` and `test_cases` remain unchanged.

