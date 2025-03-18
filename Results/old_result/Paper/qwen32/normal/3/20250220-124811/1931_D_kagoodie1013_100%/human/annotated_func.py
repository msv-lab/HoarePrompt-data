#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple represents a test case. Each tuple contains three integers (n, x, y) and a list of integers a of length n, such that 2 ≤ n ≤ 2 · 10^5, 1 ≤ x, y ≤ 10^9, and 1 ≤ a_i ≤ 10^9 for each a_i in a. The total sum of n across all test cases does not exceed 2 · 10^5.
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
        
    #State: `test_cases` is an empty list; `results` is a list containing the final accumulated `count` values for each test case.
    return results
    #The program returns `results`, which is a list containing the final accumulated `count` values for each test case. Since `test_cases` is an empty list, it implies that no test cases were processed, and thus `results` is also an empty list.
#Overall this is what the function does:The function `func_1` processes a list of test cases, where each test case consists of integers `n`, `x`, `y`, and a list `a` of length `n`. For each test case, it computes a count based on specific residue conditions and returns a list of these counts. If the input list of test cases is empty, the function returns an empty list.

