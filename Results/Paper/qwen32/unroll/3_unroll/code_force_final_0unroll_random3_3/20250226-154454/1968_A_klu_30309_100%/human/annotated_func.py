#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and test_cases is a list of integers where each integer x satisfies 2 ≤ x ≤ 1000.
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
        
    #State: `results` is a list where each element is one less than the corresponding element in `test_cases`.
    return results
    #The program returns a list `results` where each element is one less than the corresponding element in `test_cases`.
#Overall this is what the function does:The function accepts an integer `t` and a list of integers `test_cases`. It returns a list `results` where each element is one less than the corresponding element in `test_cases`.

