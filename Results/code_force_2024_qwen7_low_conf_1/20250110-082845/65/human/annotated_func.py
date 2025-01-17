#State of the program right berfore the function call: test_cases is a list of lists, where each inner list contains three non-negative integers p_1, p_2, and p_3 such that 0 <= p_1 <= p_2 <= p_3 <= 30.
def func_1(test_cases):
    results = []
    for (p1, p2, p3) in test_cases:
        total_points = p1 + p2 + p3
        
        if total_points % 2 != 0 or p3 > p1 + p2:
            results.append(-1)
            continue
        
        max_draws = min(p1, p3 - p2) + min(p2, p3 - p1)
        
        results.append(max_draws)
        
    #State of the program after the  for loop has been executed: `test_cases` is a list of lists where each inner list contains three non-negative integers p_1, p_2, and p_3 such that 0 <= p_1 <= p_2 <= p_3 <= 30, `results` is a list of integers where each element is either -1 or `max_draws`, `max_draws` is defined as `min(p1, p3 - p2) + min(p2, p3 - p1)` if the conditions `total_points % 2 != 0` or `p3 > p1 + p2` are not met, otherwise the element is -1.
    return results
    #`The program returns a list of integers where each element is either -1 or max_draws, with max_draws being defined as min(p1, p3 - p2) + min(p2, p3 - p1) if the conditions total_points % 2 != 0 or p3 > p1 + p2 are not met, otherwise the element is -1`
#Overall this is what the function does:The function `func_1` accepts a parameter `test_cases`, a list of lists where each inner list contains three non-negative integers \( p_1, p_2, \) and \( p_3 \) such that \( 0 \leq p_1 \leq p_2 \leq p_3 \leq 30 \). It returns a list of integers where each element is either \(-1\) or `max_draws`. Here, `max_draws` is defined as \( \min(p_1, p_3 - p_2) + \min(p_2, p_3 - p_1) \) if the conditions `total_points % 2 != 0` or \( p_3 > p_1 + p_2 \) are not met; otherwise, the element is \(-1\).

