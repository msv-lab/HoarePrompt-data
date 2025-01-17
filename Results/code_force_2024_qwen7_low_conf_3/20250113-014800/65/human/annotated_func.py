#State of the program right berfore the function call: test_cases is a list of strings, where each string contains three space-separated integers p_1, p_2, and p_3 representing the scores of the three players, and it is guaranteed that 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30 and the number of test cases is 1 ≤ t ≤ 500.
def func_1(test_cases):
    results = []
    for (p1, p2, p3) in test_cases:
        total_points = p1 + p2 + p3
        
        if total_points % 2 != 0 or p3 > p1 + p2:
            results.append(-1)
            continue
        
        max_draws = min(p1, p3 - p2) + min(p2, p3 - p1)
        
        results.append(max_draws)
        
    #State of the program after the  for loop has been executed: `test_cases` is a list of strings, `results` is a list of `min(p1, p3 - p2) + min(p2, p3 - p1)` for each test case, `p1` is the first player's score for each test case, `p2` is the second player's score for each test case, `p3` is the third player's score for each test case, `t` is the number of test cases, `total_points` is the sum of `p1`, `p2`, and `p3` for each test case, `i` is the index of the last processed test case, `max_draws` is `min(p1, p3 - p2) + min(p2, p3 - p1)` for the last processed test case.
    return results
    #`The program returns the list of results, which contains the value of min(p1, p3 - p2) + min(p2, p3 - p1) for each test case`
#Overall this is what the function does:The function `func_1` accepts a parameter `test_cases`, which is a list of strings. Each string contains three space-separated integers `p_1`, `p_2`, and `p_3`. The function processes each test case and calculates the value of `min(p1, p3 - p2) + min(p2, p3 - p1)` if the total points (`p1 + p2 + p3`) are even and `p3` is not greater than `p1 + p2`. If these conditions are not met, it appends `-1` to the results list. After processing all test cases, the function returns a list of results. This list contains either the calculated value or `-1` for each test case based on the specified conditions.

