#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three elements: n, x, y (2 ≤ n ≤ 2·10^5, 1 ≤ x, y ≤ 10^9) and a list a of n integers (1 ≤ a_i ≤ 10^9). The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: The `test_cases` list remains unchanged, `results` is a list containing the final value of `count` for each tuple in `test_cases`, and the `residue_map` dictionary is reset to an empty dictionary after each tuple is processed.
    return results
    #The program returns the list `results` which contains the final value of `count` for each tuple in `test_cases`. The `test_cases` list remains unchanged, and the `residue_map` dictionary is reset to an empty dictionary after each tuple is processed.
#Overall this is what the function does:The function `func_1` accepts a list of tuples `test_cases`, where each tuple contains four elements: `n`, `x`, `y`, and a list `a` of `n` integers. It processes each tuple to count how many pairs of integers in `a` satisfy the condition that the negative residue of the first integer modulo `x` and the positive residue of the second integer modulo `y` are the same. The function returns a list `results` containing the count for each tuple in `test_cases`. The `test_cases` list remains unchanged, and any internal state (like the `residue_map` dictionary) is reset after processing each tuple.

