#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three elements (n, x, y) and a list of n integers (a_1, a_2, ..., a_n). Each n is an integer such that 2 ≤ n ≤ 2 · 10^5, each x and y are integers such that 1 ≤ x, y ≤ 10^9, and each a_i is an integer such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `test_cases` is a list of tuples that has been fully iterated. `results` is a list containing the final value of `count` for each tuple in `test_cases`. Each `count` is the total sum of the values of `mod_x_map.get(mod_x, 0)` and `mod_y_map.get(mod_y, 0)` for all elements in the corresponding `arr`. `mod_x_map` and `mod_y_map` are dictionaries that contain the frequency of each `num % x` and `num % y` for all elements in the corresponding `arr` for each tuple, but these dictionaries are not retained after each tuple's iteration.
    return results
    #The program returns a list `results` containing the final value of `count` for each tuple in `test_cases`. Each `count` is the total sum of the values of `mod_x_map.get(mod_x, 0)` and `mod_y_map.get(mod_y, 0)` for all elements in the corresponding `arr`.
#Overall this is what the function does:The function `func_1` accepts a list of tuples, where each tuple contains an integer `n`, two integers `x` and `y`, and a list of `n` integers. It returns a list of integers, where each integer represents the total count of pairs of elements in the corresponding list that, when one element is negated and taken modulo `x`, or taken modulo `y`, match the same remainder in the list. The function does not modify the input `test_cases` and the final state of the program includes the `results` list containing these counts for each tuple.

