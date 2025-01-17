#State of the program right berfore the function call: test_cases is a list of strings, where each string represents a test case containing three integers separated by spaces (p_1, p_2, p_3) such that 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
def func_1(test_cases):
    results = []
    for (p1, p2, p3) in test_cases:
        total_points = p1 + p2 + p3
        
        if total_points % 2 != 0 or p3 > p1 + p2:
            results.append(-1)
            continue
        
        max_draws = min(p1, p3 - p2) + min(p2, p3 - p1)
        
        results.append(max_draws)
        
    #State of the program after the  for loop has been executed: `test_cases` is a list of tuples (p1, p2, p3) such that \(0 \leq p1 \leq p2 \leq p3 \leq 30\); `results` is a list that contains `-1` for each tuple (p1, p2, p3) that fails the condition `total_points % 2 != 0` or `p3 > p1 + p2`, and `max_draws` for each tuple (p1, p2, p3) that passes the condition, where `max_draws` is calculated as `min(p1, p3 - p2) + min(p2, p3 - p1).`
    return results
    #`results` is a list that contains `-1` for each tuple (p1, p2, p3) that fails the condition `total_points % 2 != 0` or `p3 > p1 + p2`, and `max_draws` for each tuple (p1, p3 - p2) that passes the condition, where `max_draws` is calculated as `min(p1, p3 - p2) + min(p2, p3 - p1)`
#Overall this is what the function does:The function `func_1` accepts a list of strings `test_cases`, where each string represents a test case containing three integers separated by spaces (p_1, p_2, p_3) such that 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30. It processes each test case to determine whether certain conditions are met. If the conditions `total_points % 2 != 0` or `p3 > p1 + p2` are not satisfied, the function appends `-1` to the `results` list. If the conditions are met, the function calculates `max_draws` using the formula `min(p1, p3 - p2) + min(p2, p3 - p1)` and appends this value to the `results` list. After processing all test cases, the function returns the `results` list.

