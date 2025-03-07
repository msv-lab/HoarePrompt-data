#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an even integer such that 2 <= n <= 2 * 10^5. The test_cases is a list of tuples, where each tuple contains an integer n and two strings of length n, each consisting of characters '<' and/or '>'. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `results` is a list of strings, each being either 'YES' or 'NO', corresponding to whether the second row is reachable from the first row for each test case.
    return results
    #The program returns a list of strings, each being either 'YES' or 'NO', corresponding to whether the second row is reachable from the first row for each test case.
#Overall this is what the function does:The function `func_1` takes an integer `t` representing the number of test cases and a list `test_cases` of tuples. Each tuple contains an even integer `n` and two strings of length `n` consisting of '<' and/or '>'. It returns a list of strings, each being either 'YES' or 'NO', indicating whether the second string in each tuple is reachable from the first string based on specific movement rules for each test case.

