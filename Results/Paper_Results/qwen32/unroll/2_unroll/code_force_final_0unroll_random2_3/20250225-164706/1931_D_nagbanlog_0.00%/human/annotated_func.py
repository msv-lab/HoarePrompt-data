#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case is represented by a tuple (n, x, y, a), where n is an integer such that 2 <= n <= 2 * 10^5, x and y are integers such that 1 <= x, y <= 10^9, and a is a list of n integers such that 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `results` is a list containing the count of beautiful pairs for each test case. Each element in `results` corresponds to the `beautiful_count` computed for each test case in `test_cases`. The other variables like `t`, `test_cases` remain unchanged.
    return results
    #The program returns the list `results` which contains the count of beautiful pairs for each test case.
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of a list of integers and two additional integers. For each test case, it calculates the number of "beautiful pairs" within the list, where a "beautiful pair" is defined by specific modular conditions involving the additional integers. The function returns a list of counts, each corresponding to the number of beautiful pairs found in the respective test case.

