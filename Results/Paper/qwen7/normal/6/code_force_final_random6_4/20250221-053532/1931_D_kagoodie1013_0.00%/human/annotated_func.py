#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three integers (n, x, y) followed by a list of n integers (a_1, a_2, ..., a_n). The values of n, x, and y satisfy 2 <= n <= 2 * 10^5, 1 <= x, y <= 10^9, and 1 <= a_i <= 10^9 for all i. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: Output State: The `results` list will contain the sum of `count` values from all iterations of the loop. For each iteration, `count` is calculated as the sum of `mod_x_map.get(mod_x_key, 0) + mod_y_map.get(mod_y_key, 0)` for every `num` in `arr`. After all iterations, `mod_x_map` will contain the frequency of each `mod_x_key` (i.e., `num % x`) across all arrays processed, and `mod_y_map` will contain the frequency of each `mod_y_key` (i.e., `num % y`) across all arrays processed. `num`, `mod_x_key`, and `mod_y_key` will be undefined because they are local to each iteration of the loop. `count` will be the final accumulated value of counts from all iterations.
    #
    #In summary, `results` will be a list of integers where each integer represents the count value calculated in each iteration of the loop, and `mod_x_map` and `mod_y_map` will reflect the overall frequencies of remainders when all numbers in `arr` from all test cases are divided by `x` and `y`, respectively.
    return results
    #The program returns a list of integers where each integer represents the count value calculated in each iteration of the loop. Additionally, `mod_x_map` and `mod_y_map` reflect the overall frequencies of remainders when all numbers in `arr` from all test cases are divided by `x` and `y`, respectively.
#Overall this is what the function does:The function `func_1` accepts a list of tuples `test_cases` as input. Each tuple contains three integers (n, x, y) followed by a list of n integers (a_1, a_2, ..., a_n). For each tuple, it calculates the count value based on the remainders of the numbers in the list when divided by `x` and `y`. It then appends these count values to a list `results`. After processing all tuples, the function returns the `results` list, which contains the count values for each test case. Additionally, the function maintains two dictionaries, `mod_x_map` and `mod_y_map`, to keep track of the overall frequencies of remainders when all numbers in the lists from all test cases are divided by `x` and `y`, respectively.

