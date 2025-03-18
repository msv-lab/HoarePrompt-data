#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three elements: n (an integer such that 2 ≤ n ≤ 2 · 10^5), x (an integer such that 1 ≤ x ≤ 10^9), and y (an integer such that 1 ≤ y ≤ 10^9), followed by a list of n integers a (each a_i is an integer such that 1 ≤ a_i ≤ 10^9). The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `results` is a list of integers, where each integer represents the count of pairs in the corresponding test case's array `arr` such that the first element of the pair, when negated and taken modulo `x`, and the second element of the pair, when taken modulo `y`, both result in values that have been previously seen in the array. The length of `results` is equal to the number of test cases in `test_cases`.
    return results
    #The program returns the list `results`, where each integer in the list represents the count of pairs in the corresponding test case's array `arr` such that the first element of the pair, when negated and taken modulo `x`, and the second element of the pair, when taken modulo `y`, both result in values that have been previously seen in the array. The length of `results` is equal to the number of test cases in `test_cases`.
#Overall this is what the function does:The function `func_1` accepts a list of test cases, where each test case is a tuple containing three integers `n`, `x`, and `y`, and a list of `n` integers `arr`. It returns a list `results` where each element is the count of pairs `(i, j)` in the corresponding test case's array `arr` such that `i < j`, `-arr[i] % x` and `arr[j] % y` both result in values that have been previously seen in the array. The length of `results` is equal to the number of test cases in `test_cases`.

