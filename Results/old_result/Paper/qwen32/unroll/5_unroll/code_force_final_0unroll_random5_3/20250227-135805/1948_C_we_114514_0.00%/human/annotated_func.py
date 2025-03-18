#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case in test_cases is a tuple (n, row1, row2) where n is an even integer such that 2 <= n <= 2 * 10^5, and row1 and row2 are strings of length n consisting of characters '<' and '>'. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: The `results` list will contain a series of `'YES'` and `'NO'` strings corresponding to each test case in `test_cases`. The other variables `t` and `test_cases` will remain unchanged.
    #
    #Output State:
    return results
    #The program returns the list `results` which contains a series of 'YES' and 'NO' strings corresponding to each test case in `test_cases`.
#Overall this is what the function does:The function `func_1` takes an integer `t` and a list of test cases. Each test case consists of an integer `n` and two strings `row1` and `row2` of length `n` containing '<' and '>' characters. The function returns a list of 'YES' or 'NO' strings indicating whether it is possible to reach the end of the second row starting from the beginning of the first row, following the rules defined by the characters in `row1` and `row2`.

