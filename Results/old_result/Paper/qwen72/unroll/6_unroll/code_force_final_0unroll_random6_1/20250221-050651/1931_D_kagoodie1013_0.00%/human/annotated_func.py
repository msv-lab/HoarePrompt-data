#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three elements: n, x, y (2 ≤ n ≤ 2·10^5, 1 ≤ x, y ≤ 10^9) and a list a of n integers (1 ≤ a_i ≤ 10^9). The length of test_cases is between 1 and 10^4, and the sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: The `results` list will contain the count of pairs (i, j) for each test case, where 1 ≤ i < j ≤ n and (a_i + a_j) % x = 0 or (a_i - a_j) % y = 0. The `test_cases` list remains unchanged.
    return results
    #The program returns the `results` list, which contains the count of pairs (i, j) for each test case, where 1 ≤ i < j ≤ n and (a_i + a_j) % x = 0 or (a_i - a_j) % y = 0. The `test_cases` list remains unchanged.
#Overall this is what the function does:The function `func_1` accepts a list of test cases, where each test case is a tuple containing three integers (n, x, y) and a list of n integers (a). It returns a list of results, where each result is the count of pairs (i, j) in the list a such that 1 ≤ i < j ≤ n and either (a_i + a_j) % x = 0 or (a_i - a_j) % y = 0. The input `test_cases` list remains unchanged after the function execution.

