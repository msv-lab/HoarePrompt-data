#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; each test case is a list containing three integers n, x, and y such that 2 ≤ n ≤ 2⋅10^5 and 1 ≤ x, y ≤ 10^9; and each test case also includes a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: The `results` list will contain the final value of `beautiful_count` after processing all test cases.
    return results
    #The program returns the list 'results' which contains the final value of 'beautiful_count' after processing all test cases.
#Overall this is what the function does:The function accepts a positive integer `t` and a list of test cases. Each test case consists of three integers `n`, `x`, and `y`, along with a list of `n` integers `a_1, a_2, ..., a_n`. It processes each test case to count the number of "beautiful pairs" based on certain conditions involving the modulo operations of the elements in the list `a` with `x` and `y`. A "beautiful pair" is defined by specific modulo requirements. After processing all test cases, it returns a list containing the count of beautiful pairs for each test case.

