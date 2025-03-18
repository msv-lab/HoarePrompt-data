#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three integers (n, x, y) representing the size of the array and Polycarp's favorite integers, followed by a list of n integers (a_1, a_2, ..., a_n) representing the elements of the array. The constraints are 1 <= len(test_cases) <= 10^4, 2 <= n <= 2 * 10^5, 1 <= x, y <= 10^9, and 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: results is [6, 13, 3, 3]
    return results
    #The program returns the list [6, 13, 3, 3]
#Overall this is what the function does:The function `func_1` processes a list of test cases, where each test case consists of integers `n`, `x`, `y`, and a list of `n` integers. It calculates a count based on the modular arithmetic properties of the integers in the list relative to `x` and `y`, and returns a list of these counts.

