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
        
    #State: `t` is an integer such that 1 <= t <= 1000, `test_cases` is a list of integers where each integer x satisfies 2 <= x <= 1000, `results` is a list containing the value of `best_y` for each `x` in `test_cases`, `max_sum` is the maximum sum found for the last `x` processed, `best_y` is the value of `y` that gave the maximum sum for the last `x` processed, `x` is the last `x` processed, `y` is the value that gave the maximum `current_sum` for the last `x` processed, or the value where the loop broke, and `gcd_val` and `current_sum` are the values from the last iteration for the last `x` processed.
    return results
    #The program returns a list `results` containing the value of `best_y` for each `x` in `test_cases`. Each `best_y` is the value of `y` that gave the maximum sum for the corresponding `x` processed.
#Overall this is what the function does:The function `func_1` takes an integer `t` and a list of integers `test_cases`. For each integer `x` in `test_cases`, it finds the integer `y` (where `1 <= y < x`) that maximizes the sum of `y` and the greatest common divisor (GCD) of `x` and `y`. It returns a list of these `y` values corresponding to each `x` in `test_cases`.

