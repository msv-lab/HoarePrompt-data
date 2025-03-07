#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three integers (n, x, y) representing the size of the array and Polycarp's favorite integers, followed by a list of n integers representing the elements of the array. The integers n, x, and y satisfy 2 <= n <= 2 * 10^5, 1 <= x, y <= 10^9, and 1 <= a_i <= 10^9 for all elements a_i in the array. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: After the loop executes all the iterations, `results` will contain the sum of `count` for each iteration. `mod_x_map` and `mod_y_map` will be updated for each tuple in `test_cases`, and will contain the counts of all unique remainders for each modulo operation across all arrays. `count` will be the total sum of all occurrences where the modulo operations result in keys that have been previously seen and stored in `mod_x_map` and `mod_y_map`. `n`, `x`, `y`, and `arr` will have been processed for all tuples in `test_cases`.
    return results
    #The program returns a list named `results` which contains the sum of `count` for each iteration.
#Overall this is what the function does:The function accepts a list of tuples, where each tuple contains the size of an array (n), and two integers (x and y). It also includes a list of n integers representing the elements of the array. For each tuple, the function calculates the sum of counts for each element based on specific modulo operations with x and y. It then returns a list containing the sum of counts for each tuple in the input list.

