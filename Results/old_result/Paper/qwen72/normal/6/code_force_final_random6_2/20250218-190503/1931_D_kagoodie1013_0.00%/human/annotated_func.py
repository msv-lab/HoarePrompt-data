#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three elements: n, x, y, and a list a. n is an integer such that 2 ≤ n ≤ 2 · 10^5, x and y are integers such that 1 ≤ x, y ≤ 10^9, and a is a list of n integers such that 1 ≤ a_i ≤ 10^9. The total sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The `test_cases` list remains unchanged. The `results` list contains as many elements as there are tuples in `test_cases`, where each element is the final value of `count` for the corresponding tuple. Each `count` value is the sum of the values of `mod_x_map.get(mod_x, 0) + mod_y_map.get(mod_y, 0)` for each `num` in the respective `arr`. The `mod_x_map` and `mod_y_map` dictionaries for each tuple are no longer empty and contain keys representing the unique remainders of `num % x` and `num % y` for each `num` in the respective `arr`, with values representing the count of times each remainder appears. The `num` variable is the last element of the `arr` for the last tuple in `test_cases`, `mod_x` is the value of `-num % x` for this `num`, `mod_y` is the value of `num % y` for this `num`, `mod_x_key` is the value of `num % x` for this `num`, and `mod_y_key` is the value of `num % y` for this `num`.
    return results
    #The program returns the `results` list, which contains as many elements as there are tuples in `test_cases`. Each element in `results` is the final value of `count` for the corresponding tuple, where `count` is the sum of the values of `mod_x_map.get(mod_x, 0) + mod_y_map.get(mod_y, 0)` for each `num` in the respective `arr`. The `mod_x_map` and `mod_y_map` dictionaries for each tuple contain keys representing the unique remainders of `num % x` and `num % y` for each `num` in the respective `arr`, with values representing the count of times each remainder appears.
#Overall this is what the function does:The function `func_1` accepts a list of tuples `test_cases`, where each tuple contains four elements: `n`, `x`, `y`, and a list `a` of `n` integers. It returns a list `results` where each element corresponds to the number of pairs `(i, j)` in the respective list `a` such that `a[i] % x == -a[j] % x` or `a[i] % y == a[j] % y`. The `test_cases` list remains unchanged, and the `results` list contains as many elements as there are tuples in `test_cases`. Each element in `results` is the final value of `count` for the corresponding tuple, which is the sum of the counts of such pairs for each integer in the respective `a`.

