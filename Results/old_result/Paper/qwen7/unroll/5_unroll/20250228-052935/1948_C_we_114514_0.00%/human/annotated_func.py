#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, test_cases[i] contains three lines: the first line is an integer n such that 2 ≤ n ≤ 2⋅10^5 and n is even; the second and third lines are strings of length n consisting of characters '<' and/or '>', representing the arrows in the first and second rows of the grid, respectively.
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
        
    #State: Output State: `results` is a list containing either 'YES' or 'NO' based on whether the second row becomes reachable under the given conditions for each test case.
    return results
    #The program returns a list named 'results' containing either 'YES' or 'NO' based on whether the second row becomes reachable under the given conditions for each test case.
#Overall this is what the function does:The function `func_1` takes two parameters: `t`, a positive integer between 1 and 10^4 (inclusive), and `test_cases`, a list of test cases. Each test case consists of an integer `n` (even and between 2 and 2⋅10^5) and two strings of length `n` representing arrows in the first and second rows of a grid. The function checks, for each test case, whether the second row becomes reachable under the given conditions and returns a list named 'results' containing either 'YES' or 'NO' for each test case, indicating the reachability of the second row.

