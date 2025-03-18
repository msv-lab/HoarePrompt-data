#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and test_cases is a list of tuples where each tuple contains an integer n (2 <= n <= 2 * 10^5, n is even) and two strings of length n consisting of characters '<' and/or '>'. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: results is a list of length `t` where each element is either 'YES' or 'NO', determined by the reachability of the end of `row2` from the start of `row1` for each test case.
    return results
    #The program returns a list `results` of length `t` where each element is either 'YES' or 'NO', determined by the reachability of the end of `row2` from the start of `row1` for each test case.
#Overall this is what the function does:The function `func_1` takes an integer `t` representing the number of test cases and a list of tuples `test_cases`. Each tuple contains an integer `n` and two strings `row1` and `row2` of length `n` consisting of '<' and/or '>'. It returns a list of length `t` where each element is either 'YES' or 'NO', indicating whether it is possible to reach the end of `row2` from the start of `row1` for each test case.

