#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and test_cases is a list of tuples where each tuple contains three elements (n, x, y) and a list of n integers (a_1, a_2, ..., a_n). For each tuple, n is an integer such that 2 <= n <= 2 * 10^5, x and y are integers such that 1 <= x, y <= 10^9, and each a_i is an integer such that 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `results` is a list containing the count of beautiful pairs for each test case, and `test_cases` remains unchanged.
    return results
    #The program returns the list `results` which contains the count of beautiful pairs for each test case, while `test_cases` remains unchanged.
#Overall this is what the function does:The function `func_1` accepts an integer `t` and a list of dictionaries `test_cases`. Each dictionary in `test_cases` contains a tuple of three integers (n, x, y) under the key 'params' and a list of `n` integers under the key 'array'. The function processes each test case to count the number of "beautiful pairs" in the list of integers, where a "beautiful pair" is defined as a pair of integers (a_i, a_j) such that (a_i % x + a_j % x) % x = 0 and (a_i % y + a_j % y) % y = 0. The function returns a list `results` where each element corresponds to the count of beautiful pairs for each test case, and the `test_cases` list remains unchanged.

