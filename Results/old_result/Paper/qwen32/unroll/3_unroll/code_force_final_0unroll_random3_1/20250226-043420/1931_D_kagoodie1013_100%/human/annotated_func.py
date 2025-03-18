#State of the program right berfore the function call: test_cases is a list of test cases where each test case is a tuple containing three integers (n, x, y) and a list of integers a. Specifically, n is an integer such that 2 <= n <= 2 * 10^5, x and y are integers such that 1 <= x, y <= 10^9, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9. The total number of elements in all lists a across all test cases does not exceed 2 * 10^5.
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
        
    #State: `test_cases` is a list of test cases where each test case is a tuple containing three integers (n, x, y) and a list of integers a; `results` is a list of integers where each integer represents the count of valid pairs for the corresponding test case in `test_cases`.
    return results
    #The program returns `results` which is a list of integers where each integer represents the count of valid pairs for the corresponding test case in `test_cases`.
#Overall this is what the function does:The function `func_1` accepts a list of test cases, where each test case consists of three integers (n, x, y) and a list of integers a. It calculates and returns a list of integers, where each integer represents the count of valid pairs for the corresponding test case.

