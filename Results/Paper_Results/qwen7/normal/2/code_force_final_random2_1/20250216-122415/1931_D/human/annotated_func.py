#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; test_cases is a list of triples (n, x, y, a), where n is a positive integer such that 2 ≤ n ≤ 2⋅10^5, x and y are positive integers such that 1 ≤ x, y ≤ 10^9, and a is a list of n positive integers such that 1 ≤ a_i ≤ 10^9 for all i. The sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: `results` is a list containing the total count of beautiful pairs `(required_mod_x, required_mod_y)` found across all iterations of the loop; `a` is an empty array since it gets processed in each iteration and becomes empty after all test cases are processed; `beautiful_count` reflects the cumulative count of such pairs from all test cases; `freq` is an empty dictionary because it gets updated and cleared for each test case; `mod_x` and `mod_y` are undefined outside the loop context but within each iteration, they represent the remainders of the current number in `a` when divided by `x` and `y` respectively; `required_mod_x` is `(x - mod_x) % x` and `required_mod_y` is `mod_y`.
    return results
    #The program returns a list named 'results' which contains the total count of beautiful pairs (required_mod_x, required_mod_y) found across all iterations of the loop.
#Overall this is what the function does:The function `func_1` accepts two parameters: `t`, a positive integer such that 1 ≤ t ≤ 10^4, and `test_cases`, a list of triples (n, x, y, a). For each triple in `test_cases`, it processes `n` elements in `a` and counts the number of beautiful pairs (a_i % x, a_i % y). It then returns a list named 'results' containing the total count of such beautiful pairs for each test case.

