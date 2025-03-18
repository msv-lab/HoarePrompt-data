#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; each test case in test_cases is a list containing three elements: an integer n (2 ≤ n ≤ 2⋅10^5 and n is even), and two strings representing the first and second rows of the grid, where each string consists of exactly n characters that are either '<' or '>'
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
        
    #State: The `results` list will contain either 'YES' or 'NO' for each test case in `test_cases`, depending on whether the conditions within the loop were met for each test case.
    return results
    #The program returns a list named 'results' which contains either 'YES' or 'NO' for each test case in 'test_cases', depending on whether the conditions within the loop were met for each test case.
#Overall this is what the function does:The function accepts a positive integer `t` and a list of test cases. Each test case includes an even integer `n` and two strings representing the first and second rows of a grid. The function checks, for each test case, whether it's possible to move from the first row to the second row by only moving right ('>') and returns a list of 'YES' or 'NO' based on whether the condition is met for each test case.

