#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three elements (n, x, y) and a list of n integers a. Each n is an integer such that 2 ≤ n ≤ 2 · 10^5, each x and y are integers such that 1 ≤ x, y ≤ 10^9, and each a is a list of integers such that 1 ≤ a_i ≤ 10^9. The sum of all n values across all test cases does not exceed 2 · 10^5.
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
        
    #State: `test_cases` is a list of tuples that has been fully iterated through. `results` is a list containing the final value of `count` for each tuple in `test_cases`. Each `count` is the sum of all values of `mod_x_map.get(mod_x, 0) + mod_y_map.get(mod_y, 0)` for each `num` in the corresponding `arr`. `mod_x_map` and `mod_y_map` are dictionaries that have been updated for each tuple, where `mod_x_map` contains the count of each unique `num % x` and `mod_y_map` contains the count of each unique `num % y` for the corresponding `arr`.
    return results
    #The program returns a list `results` where each element is the sum of all values of `mod_x_map.get(mod_x, 0) + mod_y_map.get(mod_y, 0)` for each `num` in the corresponding `arr` from the `test_cases` list. `mod_x_map` and `mod_y_map` are dictionaries that have been updated for each tuple in `test_cases`, containing the count of each unique `num % x` and `num % y` for the corresponding `arr`.
#Overall this is what the function does:The function `func_1` accepts a list of test cases, where each test case is a tuple containing four elements: an integer `n`, two integers `x` and `y`, and a list `arr` of `n` integers. It returns a list `results` where each element corresponds to the sum of the counts of specific remainders for the numbers in `arr`. Specifically, for each number in `arr`, the function calculates the remainder when the number is divided by `x` and the remainder when the number is divided by `y`. It then adds to the count the number of times these remainders have been seen before in the current test case. The final state of the program is that `test_cases` remains unchanged, and `results` contains the computed counts for each test case.

