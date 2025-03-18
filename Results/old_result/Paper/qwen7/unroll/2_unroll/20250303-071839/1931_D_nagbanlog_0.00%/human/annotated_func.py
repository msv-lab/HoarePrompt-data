#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; test_cases is a list of tuples, where each tuple contains three integers n, x, and y such that 2 ≤ n ≤ 2⋅10^5, 1 ≤ x, y ≤ 10^9; and a list of n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9 for all i. The sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: `results` is a list containing the count of beautiful pairs for each test case, where a beautiful pair `(num, a_i)` satisfies the condition that the number `num` can be transformed into `a_i` by performing a series of operations where each operation consists of either adding `x` or subtracting `y` modulo `x` and `y`. The `print` statements are informational and do not affect the final state of the `results` list.
    return results
    #The program returns the list `results` containing the count of beautiful pairs for each test case.
#Overall this is what the function does:The function `func_1` accepts two parameters: `t`, a positive integer between 1 and 10^4, and `test_cases`, a list of tuples. Each tuple contains three integers `n`, `x`, and `y` (where 2 ≤ n ≤ 2⋅10^5, 1 ≤ x, y ≤ 10^9), and a list of `n` integers `a_1, a_2, ..., a_n` (where 1 ≤ a_i ≤ 10^9 for all i). For each test case, the function calculates the count of beautiful pairs `(num, a_i)` where `num` can be transformed into `a_i` by performing a series of operations consisting of either adding `x` or subtracting `y` modulo `x` and `y`. It then appends these counts to a list `results`. Finally, the function returns the list `results` containing the count of beautiful pairs for each test case.

