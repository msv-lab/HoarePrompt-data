#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), and test_cases is a list of tuples, where each tuple contains three elements: n, x, y, and a list a of n integers. For each tuple, n is an integer (2 ≤ n ≤ 2 · 10^5), x and y are positive integers (1 ≤ x, y ≤ 10^9), and a is a list of n integers (1 ≤ a_i ≤ 10^9). The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: t is a positive integer (1 ≤ t ≤ 10^4), test_cases is a list of tuples, where each tuple contains three elements: n, x, y, and a list a of n integers. For each tuple, n is an integer (2 ≤ n ≤ 2 · 10^5), x and y are positive integers (1 ≤ x, y ≤ 10^9), and a is a list of n integers (1 ≤ a_i ≤ 10^9). The sum of n over all test cases does not exceed 2 · 10^5. results is a list of integers where each integer represents the count of beautiful pairs for each test case.
    return results
    #The program returns a list of integers 'results', where each integer represents the count of beautiful pairs for each test case in the list 'test_cases'.
#Overall this is what the function does:The function `func_1` accepts a positive integer `t` and a list of dictionaries `test_cases`. Each dictionary in `test_cases` contains a key 'params' with a tuple of three integers (n, x, y) and a key 'array' with a list of n integers. The function processes each test case to count the number of "beautiful pairs" in the list `a`, where a "beautiful pair" is defined as a pair of numbers (a[i], a[j]) such that i < j and (a[i] + a[j]) % x == 0 and (a[i] + a[j]) % y == 0. The function returns a list of integers `results`, where each integer represents the count of beautiful pairs for the corresponding test case.

