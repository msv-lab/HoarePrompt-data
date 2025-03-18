#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple represents a test case. Each test case consists of three integers (n, x, y) and a list of n integers (a). The integers n, x, and y satisfy 2 <= n <= 2 * 10^5, 1 <= x, y <= 10^9, and the elements of the list a satisfy 1 <= a_i <= 10^9. The total number of elements across all test cases does not exceed 2 * 10^5.
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
        
    #State: results is a list containing the count of pairs for each test case, where each count is determined by the logic described above.
    return results
    #The program returns the list 'results' which contains the count of pairs for each test case.
#Overall this is what the function does:The function `func_1` processes a list of test cases, where each test case consists of integers `n`, `x`, `y`, and a list `a` of `n` integers. For each test case, it calculates and returns the count of pairs `(a_i, a_j)` with `i < j` such that the product of `a_i` and `a_j` is divisible by both `x` and `y`. The function returns a list of these counts, one for each test case.

