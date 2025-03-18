#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple represents a test case. Each test case consists of three integers (n, x, y) and a list of n integers (a). Specifically, 1 <= len(test_cases) <= 10^4, 2 <= n <= 2 * 10^5, 1 <= x, y <= 10^9, and 1 <= a_i <= 10^9 for each element a_i in the list a. The sum of n across all test cases does not exceed 2 * 10^5.
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
        
    #State: `test_cases` is a list of tuples, where each tuple contains `n`, `x`, `y`, and `arr`; `results` is a list containing the final value of `count` for each processed tuple; `count` is the final computed value after processing all elements in `arr` for each tuple; `mod_x_map` and `mod_y_map` are dictionaries that exist only within the scope of each iteration of the outer loop and are re-initialized for each tuple; `results` contains a count for each tuple processed, representing the total number of pairs `(mod_x, mod_y)` encountered for that specific tuple.
    return results
    #The program returns `results`, which is a list containing the final value of `count` for each processed tuple in `test_cases`. Each `count` represents the total number of pairs `(mod_x, mod_y)` encountered for that specific tuple.
#Overall this is what the function does:The function processes a list of test cases, where each test case consists of integers `n`, `x`, `y`, and a list `a` of `n` integers. For each test case, it calculates the total number of pairs `(mod_x, mod_y)` that can be formed from the list `a`, where `mod_x` is the remainder of an element when divided by `x` and `mod_y` is the remainder when divided by `y`. The function returns a list of these counts, one for each test case.

