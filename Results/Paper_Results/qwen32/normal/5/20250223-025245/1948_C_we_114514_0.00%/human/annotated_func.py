#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case consists of an integer n (2 <= n <= 2 * 10^5) which is even, followed by two strings of length n consisting of '<' and '>' characters. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: results
    return results
    #The program returns 'results'
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of an even integer `n` and two strings of length `n` containing only '<' and '>' characters. For each test case, it determines if it is possible to reach the end of the second string starting from the beginning of the first string, moving only to the right ('>') or switching to the corresponding position in the other string if the current character is '<'. The function returns a list of 'YES' or 'NO' for each test case, indicating whether the end of the second string is reachable.

