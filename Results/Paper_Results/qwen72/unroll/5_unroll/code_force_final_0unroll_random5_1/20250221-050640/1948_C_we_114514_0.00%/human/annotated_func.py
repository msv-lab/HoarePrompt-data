#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, test_cases is a list of tuples where each tuple contains an integer n (2 <= n <= 2 * 10^5 and n is even) and two strings of length n consisting of characters '<' and '>', representing the arrows in the first and second rows of the grid, respectively. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: t is an integer such that 1 <= t <= 10^4, test_cases is a list of tuples where each tuple contains an integer n (2 <= n <= 2 * 10^5 and n is even) and two strings of length n consisting of characters '<' and '>', representing the arrows in the first and second rows of the grid, respectively. The sum of n over all test cases does not exceed 2 * 10^5. results is a list of strings, where each string is either 'YES' or 'NO', indicating whether the second row is reachable from the first row for each test case.
    return results
    #The program returns the list 'results' where each element is either 'YES' or 'NO', indicating whether the second row is reachable from the first row for each test case in the list 'test_cases'.
#Overall this is what the function does:The function `func_1` accepts an integer `t` and a list of tuples `test_cases`. Each tuple in `test_cases` contains an integer `n` and two strings of length `n` with characters '<' and '>'. The function evaluates whether it is possible to move from the first row to the second row in each test case, based on the direction of the arrows. It returns a list `results` where each element is 'YES' if the second row is reachable from the first row, or 'NO' otherwise, for each test case.

