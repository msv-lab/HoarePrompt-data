#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers n, x, and y where 2 ≤ n ≤ 2 · 10^5, 1 ≤ x, y ≤ 10^9, and a list of n integers a where 1 ≤ a_i ≤ 10^9. The sum of n across all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `test_cases` is a list of at least one test case where each test case is a tuple (n, x, y, a), `results` is a list containing the final `beautiful_count` for each test case, `case` is the last test case processed in `test_cases`, `n` is the first element of `case['params']`, `x` is the second element of `case['params']`, `y` is the third element of `case['params']`, `a` is `case['array']`, `freq` is a dictionary with the count of each `(mod_x, mod_y)` pair encountered in the last test case, `beautiful_count` is the total number of beautiful pairs found in the last test case.
    return results
    #The program returns `results`, which is a list containing the final `beautiful_count` for each test case.
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of integers `n`, `x`, and `y`, and a list of `n` integers `a`. For each test case, it calculates the number of "beautiful pairs" based on specific modular conditions and returns a list of these counts for all test cases.

