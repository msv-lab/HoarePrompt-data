#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), representing the number of test cases. Each test case consists of two lines: the first line contains three integers n, x, and y (2 ≤ n ≤ 2 · 10^5, 1 ≤ x, y ≤ 10^9), and the second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9). The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: After the loop executes all iterations, `t` remains a positive integer (1 ≤ t ≤ 10^4), `test_cases` remains a list of `t` test cases, `results` is a list containing `t` elements, each element being the `beautiful_count` for the corresponding test case. For each test case, `n` is the value of `case['params'][0]`, `x` is the value of `case['params'][1]`, `y` is the value of `case['params'][2]`, `a` is a list of `n` integers from `case['array']`, and `freq` is a dictionary where each key is a tuple `(mod_x, mod_y)` representing the remainders when an element of `a` is divided by `x` and `y`, respectively, and the value is the count of how many times this pair of remainders appears in `a`. The variable `beautiful_count` is the total count of pairs `(required_mod_x, required_mod_y)` found in `freq` during the loop execution for each test case.
    return results
    #The program returns a list `results` containing `t` elements, where `t` is a positive integer between 1 and 10,000. Each element in `results` represents the `beautiful_count` for the corresponding test case. The `beautiful_count` is the total count of pairs `(required_mod_x, required_mod_y)` found in the `freq` dictionary for each test case. The `freq` dictionary contains counts of how many times each pair of remainders `(mod_x, mod_y)` appears in the list `a` for each test case.
#Overall this is what the function does:The function `func_1` takes two parameters: `t`, a positive integer indicating the number of test cases, and `test_cases`, a list of dictionaries where each dictionary represents a test case. Each test case dictionary contains 'params' (a list of three integers: `n`, `x`, and `y`) and 'array' (a list of `n` integers). The function processes each test case to calculate the count of "beautiful" pairs of numbers in the array `a` for each test case. A pair is considered "beautiful" if the difference between the required remainders (`required_mod_x` and `required_mod_y`) when a number is divided by `x` and `y` respectively, matches a previously seen pair of remainders. The function returns a list `results` containing `t` elements, where each element is the count of "beautiful" pairs for the corresponding test case. The original `t` and `test_cases` remain unchanged.

