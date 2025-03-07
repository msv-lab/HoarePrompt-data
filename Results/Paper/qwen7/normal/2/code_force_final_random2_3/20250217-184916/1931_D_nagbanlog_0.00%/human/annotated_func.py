#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4; each test case in test_cases is a list containing three integers n, x, and y such that 2 <= n <= 2 * 10^5 and 1 <= x, y <= 10^9; and each test case also includes a list of n integers a_1, a_2, ..., a_n where 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: Output State: `results` is a list containing the total count of beautiful pairs for all test cases processed. For each test case, `beautiful_count` is calculated based on the frequency of `(mod_x, mod_y)` pairs in the `freq` dictionary. Specifically, `beautiful_count` accumulates the count of pairs `(required_mod_x, required_mod_y)` that exist in `freq`. The `freq` dictionary tracks the occurrences of each unique `(mod_x, mod_y)` pair across all numbers in the arrays provided by the test cases. After all iterations of the loop, `results` will contain the final `beautiful_count` for each test case, representing the total number of beautiful pairs found across all test cases.
    return results
    #The program returns a list named `results` which contains the total count of beautiful pairs for all test cases processed. Each element in the list represents the `beautiful_count` for a specific test case, calculated based on the frequency of `(mod_x, mod_y)` pairs in the `freq` dictionary. The `beautiful_count` for each test case accumulates the count of pairs `(required_mod_x, required_mod_y)` that exist in `freq`, representing the total number of beautiful pairs found across all test cases for that particular test case.
#Overall this is what the function does:The function `func_1` processes a list of test cases, each containing parameters `n`, `x`, `y`, and an array of integers `a`. It calculates the total count of "beautiful pairs" for each test case based on the frequency of specific modulo pairs. A "beautiful pair" is defined by the conditions `(required_mod_x, required_mod_y)` derived from the given `x` and `y` values. The function returns a list of counts, where each count corresponds to the total number of beautiful pairs found for each test case.

