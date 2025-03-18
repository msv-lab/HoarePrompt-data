#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. test_cases is a list of tuples, where each tuple contains an integer n and two strings of length n, where n is an even integer such that 2 ≤ n ≤ 2 \cdot 10^5, and the strings consist only of the characters '<' and '>'. The sum of all n values in test_cases does not exceed 2 \cdot 10^5.
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
    #The program returns the variable 'results'
#Overall this is what the function does:The function `func_1` processes a list of test cases, each consisting of two strings of equal even length containing only '<' and '>'. It determines for each test case whether it is possible to reach the end of the second string starting from the beginning of the first string by following the '>' characters, and returns a list of 'YES' or 'NO' based on the result for each test case.

