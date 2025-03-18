#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers n, x, and y where 2 ≤ n ≤ 2 · 10^5, 1 ≤ x, y ≤ 10^9, and a list a of n integers where 1 ≤ a_i ≤ 10^9. The sum of n across all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `test_cases` is a list containing at least one test case, `results` is a list containing the `beautiful_count` from all processed test cases, `case` is the last test case in `test_cases`, `n` is `case['params'][0]`, `x` is `case['params'][1]`, `y` is `case['params'][2]`, `a` is `case['array']`, `freq` is a dictionary containing the frequency of each `(mod_x, mod_y)` pair encountered during the last iteration of the loop, `beautiful_count` is the total count of "beautiful" pairs found during the last iteration of the loop. All test cases have been processed and their respective `beautiful_count` values have been appended to `results`.
    return results
    #The program returns `results`, which is a list containing the `beautiful_count` from all processed test cases. Each `beautiful_count` represents the total count of "beautiful" pairs found during the processing of each test case in `test_cases`.
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of integers `n`, `x`, `y`, and a list `a` of `n` integers. For each test case, it calculates the number of "beautiful" pairs based on specific modular conditions involving `x` and `y`, and returns a list of these counts for all test cases.

