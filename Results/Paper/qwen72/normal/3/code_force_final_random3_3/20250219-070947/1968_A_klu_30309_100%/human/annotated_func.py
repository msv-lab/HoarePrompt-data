#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and test_cases is a list of integers where each integer x satisfies 2 <= x <= 1000.
def func_1(t, test_cases):
    results = []
    for x in test_cases:
        max_sum = 0
        
        best_y = 1
        
        for y in range(x - 1, 0, -1):
            gcd_val = math.gcd(x, y)
            current_sum = gcd_val + y
            if current_sum > max_sum:
                max_sum = current_sum
                best_y = y
                break
        
        results.append(best_y)
        
    #State: `t` is an integer such that 1 <= t <= 1000, `test_cases` is a list of integers where each integer x satisfies 2 <= x <= 1000, `results` is a list containing the value of `best_y` for each integer in `test_cases`, where `best_y` is 1 for each integer in `test_cases`.
    return results
    #The program returns a list `results` where each element is 1, corresponding to the `best_y` value for each integer in the `test_cases` list.
#Overall this is what the function does:The function `func_1` accepts an integer `t` and a list of integers `test_cases`, where each integer `x` in `test_cases` satisfies 2 <= x <= 1000. It returns a list `results` where each element is the value of `best_y` for each integer in `test_cases`. The value of `best_y` is the largest integer `y` (where 1 <= y < x) that maximizes the sum of `y` and the greatest common divisor (GCD) of `x` and `y`. If no such `y` is found, `best_y` is set to 1.

