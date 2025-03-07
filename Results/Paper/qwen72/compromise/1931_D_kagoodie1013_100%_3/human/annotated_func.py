#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three elements: an integer n (2 ≤ n ≤ 2 · 10^5), an integer x (1 ≤ x ≤ 10^9), and an integer y (1 ≤ y ≤ 10^9), followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9). The sum of n over all test cases does not exceed 2 · 10^5.
def func_1(test_cases):
    results = []
    for (n, x, y, arr) in test_cases:
        count = 0
        
        residue_map = {}
        
        for num in arr:
            r_x = -num % x
            r_y = num % y
            count += residue_map.get((r_x, r_y), 0)
            current_key = num % x, num % y
            residue_map[current_key] = residue_map.get(current_key, 0) + 1
        
        results.append(count)
        
    #State: The `test_cases` list remains unchanged. The `results` list contains the value of `count` for each tuple in `test_cases`. Each `count` value represents the total number of pairs of elements in the corresponding `arr` list that have the same remainders when divided by `x` and `y`.
    return results
    #The program returns the `results` list, which contains the value of `count` for each tuple in the `test_cases` list. Each `count` value represents the total number of pairs of elements in the corresponding `arr` list that have the same remainders when divided by `x` and `y`.
#Overall this is what the function does:The function `func_1` accepts a list of tuples `test_cases`, where each tuple contains an integer `n`, two integers `x` and `y`, and a list of `n` integers. It returns a list `results` where each element is the count of pairs of elements in the corresponding `arr` list that have the same remainders when divided by `x` and `y`. The `test_cases` list remains unchanged after the function execution.

