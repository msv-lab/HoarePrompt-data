#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; each test case in test_cases is a list containing three integers n, x, and y such that 2 ≤ n ≤ 2⋅10^5 and 1 ≤ x, y ≤ 10^9; and each test case also includes a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: `results` is a list containing the count of beautiful pairs for each test case processed. Each element in the list corresponds to the output of the `beautiful_count` variable for each iteration of the outer loop. The `beautiful_count` is calculated based on the conditions specified within the nested loop, considering the frequency of numbers with specific modular values relative to `x` and `y`.
    return results
    #The program returns a list called 'results' which contains the count of beautiful pairs for each test case processed. Each element in the list corresponds to the output of the 'beautiful_count' variable for each iteration of the outer loop. The 'beautiful_count' is calculated based on the conditions specified within the nested loop, considering the frequency of numbers with specific modular values relative to 'x' and 'y'.
#Overall this is what the function does:The function processes a list of test cases, where each test case includes an integer `n`, and two other integers `x` and `y`, along with a list of `n` integers. For each test case, it calculates the number of "beautiful pairs" based on specific modular conditions involving `x` and `y`. A "beautiful pair" is defined by the frequency of numbers in the list that meet certain modular criteria. The function returns a list of counts, one for each test case, representing the number of beautiful pairs found.

