#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), representing the number of test cases. Each test case in test_cases is a tuple containing three integers n, x, y (2 ≤ n ≤ 2·10^5, 1 ≤ x, y ≤ 10^9) and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9). The sum of n over all test cases does not exceed 2·10^5.
def func_1(t, test_cases):
    results = []
    for case in test_cases:
        n, x, y = case['params']
        
        a = case['array']
        
        freq = defaultdict(int)
        
        beautiful_count = 0
        
        for num in a:
            mod_x = num % x
            mod_y = num % y
            required_mod_x = (x - mod_x) % x
            required_mod_y = mod_y
            if (required_mod_x, required_mod_y) in freq:
                beautiful_count += freq[required_mod_x, required_mod_y]
            freq[mod_x, mod_y] += 1
        
        results.append(beautiful_count)
        
    #State: After the loop executes all iterations, `t` remains a positive integer (1 ≤ t ≤ 10^4), `test_cases` is a list of test cases that has been fully processed, `results` is a list containing the final value of `beautiful_count` for each test case, `case` is the last test case in `test_cases`, `n` is the value of `case['params'][0]` for the last test case, `x` is the value of `case['params'][1]` for the last test case, `y` is the value of `case['params'][2]` for the last test case, `a` is the list of integers from the last test case, `freq` is a `defaultdict(int)` where each key is a tuple `(mod_x, mod_y)` representing the frequency of pairs of remainders when elements of `a` are divided by `x` and `y`, respectively, and `beautiful_count` is the total count of pairs of elements in `a` such that the first element can be transformed into the second element by adding some integer multiple of `x` and the result is divisible by `y`.
    return results
    #The program returns a list `results` containing the final value of `beautiful_count` for each test case in `test_cases`. Each value in `results` represents the total count of pairs of elements in the corresponding test case's list `a` such that the first element can be transformed into the second element by adding some integer multiple of `x` and the result is divisible by `y`.
#Overall this is what the function does:The function `func_1` takes two parameters: a positive integer `t` indicating the number of test cases, and a list `test_cases` where each test case is a dictionary containing a tuple of three integers (`n`, `x`, `y`) and a list of `n` integers. The function processes each test case to count the number of pairs of elements in the list such that the first element can be transformed into the second element by adding some integer multiple of `x` and the result is divisible by `y`. It returns a list `results` containing the count of such pairs for each test case. After the function completes, `t` remains unchanged, `test_cases` is fully processed, and `results` contains the final counts for each test case.

