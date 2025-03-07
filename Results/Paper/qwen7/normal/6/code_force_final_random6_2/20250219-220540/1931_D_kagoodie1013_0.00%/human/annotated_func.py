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
        
    #State: `results` contains the cumulative sum of `count` values calculated for each iteration of the loop, `arr` is an empty list, `mod_x_map` and `mod_y_map` are dictionaries containing the frequencies of all possible remainders when elements of `arr` are divided by `x` and `y` respectively across all iterations, and `count` is the final sum of all `mod_x_map[mod_x_key]` and `mod_y_map[mod_y_key]` values for the last iteration.
    return results
    #The program returns the cumulative sum of `count` values calculated for each iteration of the loop, stored in the list `results`.
#Overall this is what the function does:The function accepts a list of tuples, where each tuple contains three integers (n, x, y) followed by a list of n integers. For each tuple, it calculates a count value based on the remainders when the list elements are divided by x and y. It then stores the cumulative sum of these count values in a list and returns this list.

