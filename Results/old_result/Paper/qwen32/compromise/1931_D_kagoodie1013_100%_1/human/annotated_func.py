#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple represents a test case. Each test case is a tuple containing a tuple (n, x, y) and a list a. Here, n is an integer (2 ≤ n ≤ 2 · 10^5), x and y are integers (1 ≤ x, y ≤ 10^9), and a is a list of n integers (1 ≤ a_i ≤ 10^9). The length of the test_cases list is t (1 ≤ t ≤ 10^4), and the sum of n across all test cases does not exceed 2 · 10^5.
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
        
    #State: `test_cases` remains unchanged, `results` contains the final value of `count` for each test case in `test_cases`, `count` is the total number of times a pair `(r_x, r_y)` has been encountered before for each element in `arr` for each test case, `residue_map` is re-initialized for each test case and contains the frequency of each `(num % x, num % y)` pair encountered in `arr` for that specific test case.
    return results
    #The program returns `results` which contains the final value of `count` for each test case in `test_cases`. Each `count` represents the total number of times a pair `(r_x, r_y)` has been encountered before for each element in `arr` for each test case.
#Overall this is what the function does:The function processes a list of test cases, where each test case consists of integers `n`, `x`, `y`, and a list `a` of `n` integers. For each test case, it calculates the number of times a specific pair of residues `(r_x, r_y)` has been encountered before for each element in the list `a`. The result for each test case is stored in a list `results`, which is returned at the end. The input `test_cases` remains unchanged.

