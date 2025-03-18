#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n (an integer representing the size of the array), x and y (integers representing Polycarp's favorite integers), followed by a list of n integers representing the elements of the array (a_1, a_2, ..., a_n). The constraints are 1 ≤ t ≤ 10^4, 2 ≤ n ≤ 2 ⋅ 10^5, 1 ≤ x, y ≤ 10^9, and 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: `results` is a list where each element is the count of pairs `(mod_x, mod_y)` found in the corresponding `arr` for each `test_case`, with `mod_x` calculated as `-num % x` and `mod_y` as `num % y`.
    return results
    #The program returns a list 'results' where each element is the count of pairs (mod_x, mod_y) found in the corresponding 'arr' for each 'test_case', with mod_x calculated as -num % x and mod_y as num % y.
#Overall this is what the function does:The function accepts a list of test cases, where each test case includes the size of an array, two integers (x and y), and the array elements. For each test case, it calculates the count of pairs (mod_x, mod_y) for each element in the array, with mod_x being -num % x and mod_y being num % y. It then appends these counts to a results list, which it returns.

