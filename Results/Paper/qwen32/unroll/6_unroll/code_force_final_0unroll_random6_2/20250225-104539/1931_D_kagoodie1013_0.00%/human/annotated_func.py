#State of the program right berfore the function call: test_cases is a list of test cases, where each test case is a tuple containing three integers (n, x, y) and a list of n integers (a). Specifically, for each test case, 2 <= n <= 2 * 10^5, 1 <= x, y <= 10^9, and the list a contains n integers where 1 <= a_i <= 10^9. The total number of elements across all arrays in all test cases does not exceed 2 * 10^5.
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
        
    #State: `test_cases` remains unchanged as a list of test cases; `results` is a list where each element is the count of specific pairs calculated for each test case.
    return results
    #The program returns a list 'results' where each element is the count of specific pairs calculated for each test case.
#Overall this is what the function does:The function processes a list of test cases, where each test case includes integers `n`, `x`, `y`, and a list of `n` integers. It calculates a count of specific pairs for each test case based on the modular properties of the integers with respect to `x` and `y`, and returns a list of these counts.

