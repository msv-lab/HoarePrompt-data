#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. test_cases is a list of tuples, where each tuple contains an integer n and two strings of length n. n is an even integer such that 2 <= n <= 2 * 10^5. Each string consists of characters '<' and '>' only. The sum of all n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `results` is a list containing 'YES' or 'NO' for each test case based on whether the second row is reachable from the first row according to the rules specified in the loop. The other variables `t`, `test_cases` remain unchanged.
    return results
    #The program returns the list `results` which contains 'YES' or 'NO' for each test case based on whether the second row is reachable from the first row according to the rules specified in the loop.
#Overall this is what the function does:The function `func_1` takes an integer `t` and a list of tuples `test_cases`. Each tuple contains an integer `n` and two strings of length `n` consisting of characters '<' and '>'. The function determines for each test case whether the second row is reachable from the first row based on specific movement rules and returns a list of 'YES' or 'NO' corresponding to each test case.

