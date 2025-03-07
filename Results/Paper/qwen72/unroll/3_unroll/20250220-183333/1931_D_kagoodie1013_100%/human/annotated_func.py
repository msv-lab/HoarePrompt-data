#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three elements: n, x, and y, and a list a. n is an integer such that 2 ≤ n ≤ 2 · 10^5, x and y are integers such that 1 ≤ x, y ≤ 10^9, and a is a list of n integers such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: Output State: `results` is a list containing the number of pairs `(i, j)` for each test case, where `0 ≤ i < j < n` and `a_i + a_j` is divisible by both `x` and `y`. The other variables (`test_cases`) remain unchanged.
    return results
    #The program returns the list `results` which contains the number of pairs `(i, j)` for each test case, where `0 ≤ i < j < n` and `a_i + a_j` is divisible by both `x` and `y`. The other variables (`test_cases`) remain unchanged.
#Overall this is what the function does:The function `func_1` accepts a list of test cases, where each test case is a tuple containing four elements: `n`, `x`, `y`, and a list `a`. The function returns a list `results` where each element corresponds to the count of pairs `(i, j)` in the respective test case such that `0 ≤ i < j < n` and the sum `a_i + a_j` is divisible by both `x` and `y`. The input `test_cases` remains unchanged after the function execution.

