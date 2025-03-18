#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4) representing the number of test cases. test_cases is a list of tuples, where each tuple contains three elements: n, x, and y, and a list of n integers a. For each tuple, n is an integer (2 ≤ n ≤ 2 · 10^5), x and y are integers (1 ≤ x, y ≤ 10^9), and a is a list of n integers (1 ≤ a_i ≤ 10^9). The sum of n over all test cases does not exceed 2 · 10^5.
def func_1(t, test_cases):
    results = []
    for case in test_cases:
        n, x, y = case['params']
        
        a = case['array']
        
        freq = {}
        
        beautiful_count = 0
        
        print(f'Processing Test Case: n = {n}, x = {x}, y = {y}, array = {a}')
        
        for num in a:
            mod_x = num % x
            mod_y = num % y
            required_mod_x = (x - mod_x) % x
            required_mod_y = mod_y
            print(
                f'Number: {num}, mod_x: {mod_x}, mod_y: {mod_y}, required_mod_x: {required_mod_x}, required_mod_y: {required_mod_y}'
                )
            if (required_mod_x, required_mod_y) in freq:
                beautiful_count += freq[required_mod_x, required_mod_y]
            if (mod_x, mod_y) not in freq:
                freq[mod_x, mod_y] = 0
            freq[mod_x, mod_y] += 1
        
        print(f'Beautiful pairs count: {beautiful_count}')
        
        results.append(beautiful_count)
        
    #State: `results` is a list of integers where each integer represents the count of beautiful pairs for each test case in `test_cases`. The length of `results` is equal to `t`. The `freq` dictionary and `beautiful_count` variable are reset for each test case, so they do not retain values between different test cases.
    return results
    #The program returns a list of integers `results` where each integer represents the count of beautiful pairs for each test case in `test_cases`. The length of `results` is equal to `t`.
#Overall this is what the function does:The function `func_1` accepts a positive integer `t` and a list of tuples `test_cases`. Each tuple in `test_cases` contains a dictionary with keys 'params' and 'array', where 'params' is a tuple of three integers `n`, `x`, and `y`, and 'array' is a list of `n` integers. The function processes each test case to count the number of "beautiful pairs" in the list `a`. A "beautiful pair" is defined as a pair of numbers in `a` where the first number can be incremented by some integer to make it divisible by `x` and the second number is already divisible by `y`. The function returns a list `results` of length `t`, where each element is the count of beautiful pairs for the corresponding test case.

