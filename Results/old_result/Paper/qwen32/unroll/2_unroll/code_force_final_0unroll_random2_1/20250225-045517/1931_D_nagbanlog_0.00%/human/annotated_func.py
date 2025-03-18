#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. test_cases is a list of tuples, where each tuple contains an integer n such that 2 <= n <= 2 * 10^5, two integers x and y such that 1 <= x, y <= 10^9, and a list a of n integers where each integer a_i satisfies 1 <= a_i <= 10^9. The sum of all n across all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `test_cases` is a list of tuples, where each tuple contains an integer n such that 2 <= n <= 2 * 10^5, two integers x and y such that 1 <= x, y <= 10^9, and a list a of n integers where each integer a_i satisfies 1 <= a_i <= 10^9; `results` is a list of integers representing the count of beautiful pairs for each test case.
    return results
    #The program returns `results`, which is a list of integers representing the count of beautiful pairs for each test case.
#Overall this is what the function does:The function `func_1` processes multiple test cases, where each test case consists of a list of integers and two additional integers `x` and `y`. For each test case, it calculates and returns the count of "beautiful pairs" in the list. A "beautiful pair" is defined based on the remainders of the elements when divided by `x` and `y`. The function returns a list of counts, one for each test case.

