#State of the program right berfore the function call: t is a non-negative integer such that 1 <= t <= 1000, and test_cases is a list of integers where each integer x satisfies 2 <= x <= 1000.
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
        
    #State: `t` is a non-negative integer such that 1 <= t <= 1000, `test_cases` is a list of integers where each integer x satisfies 2 <= x <= 1000 and must have `t` integers, `results` is a list containing `t` integers, each being the value of `best_y` for the corresponding `x` in `test_cases`, `max_sum` is the greatest value of `gcd_val + y` encountered during the last iteration of the loop, `best_y` is the value of `y` that produced the greatest `max_sum` for the last `x` in `test_cases`, and `y` is 1.
    return results
    #The program returns a list `results` containing `t` integers, where each integer is the value of `best_y` for the corresponding `x` in `test_cases`.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `t` and a list of integers `test_cases`. It returns a list `results` containing `t` integers, where each integer is the value of `best_y` for the corresponding `x` in `test_cases`. The value of `best_y` for each `x` is the largest `y` (1 ≤ y < x) such that the sum of the greatest common divisor (GCD) of `x` and `y`, and `y` itself, is maximized. If multiple `y` values produce the same maximum sum, the function selects the largest `y` among them.

