#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case in test_cases is a tuple where the first element is an integer n such that 2 <= n <= 2 * 10^5, and the second and third elements are integers x and y such that 1 <= x, y <= 10^9. The fourth element is a list of n integers a_1, a_2, ..., a_n where each a_i is an integer such that 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4; each test case in `test_cases` is a tuple where the first element is an integer `n` such that 2 <= n <= 2 * 10^5, and the second and third elements are integers `x` and `y` such that 1 <= x, y <= 10^9; the fourth element is a list of `n` integers `a_1, a_2, ..., a_n` where each `a_i` is an integer such that 1 <= a_i <= 10^9; `results` is a list containing the count of beautiful pairs for each test case.
    return results
    #The program returns `results`, which is a list containing the count of beautiful pairs for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, two integers `x` and `y`, and a list of `n` integers. For each test case, it calculates and returns the count of "beautiful pairs" in the list, where a "beautiful pair" is defined based on specific modulo conditions involving `x` and `y`. The function returns a list of these counts, one for each test case.

