#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three integers (n, x, y) and a list of n integers a, such that 1 <= len(test_cases) <= 10^4, 2 <= n <= 2 * 10^5, 1 <= x, y <= 10^9, and 1 <= a_i <= 10^9 for each a_i in a. The sum of n over all test cases does not exceed 2 * 10^5.
def func_1(test_cases):
    results = []
    for (n, x, y, arr) in test_cases:
        count = 0
        
        mod_x_map = {}
        
        mod_y_map = {}
        
        for num in arr:
            mod_x = -num % x
            mod_y = num % y
            count += mod_x_map.get(mod_x, 0) + mod_y_map.get(mod_y, 0)
            mod_x_key = num % x
            mod_y_key = num % y
            mod_x_map[mod_x_key] = mod_x_map.get(mod_x_key, 0) + 1
            mod_y_map[mod_y_key] = mod_y_map.get(mod_y_key, 0) + 1
        
        results.append(count)
        
    #State: `test_cases` is a list of tuples, `results` is a list containing the final values of `count` for each tuple in `test_cases`, `count` is the final count after all iterations for the last tuple in `test_cases`, `mod_x_map` is a dictionary with keys as `mod_x_key` values from `arr` and values as their respective counts for the last tuple in `test_cases`, `mod_y_map` is a dictionary with keys as `mod_y_key` values from `arr` and values as their respective counts for the last tuple in `test_cases`, `n`, `x`, `y`, and `arr` are the values of the last tuple in `test_cases`.
    return results
    #The program returns `results`, which is a list containing the final values of `count` for each tuple in `test_cases`.
#Overall this is what the function does:The function `func_1` processes a list of test cases, where each test case consists of three integers (n, x, y) and a list of n integers. It calculates a count for each test case based on specific conditions involving the modulo of the integers with x and y, and returns a list of these counts.

