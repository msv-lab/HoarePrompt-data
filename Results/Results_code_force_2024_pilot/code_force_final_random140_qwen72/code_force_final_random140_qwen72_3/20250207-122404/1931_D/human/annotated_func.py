#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of a tuple (n, x, y) where n is an integer such that 2 ≤ n ≤ 2 · 10^5, and x, y are integers such that 1 ≤ x, y ≤ 10^9. The array a for each test case is a list of n integers where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: After the loop has executed all iterations, the list `results` contains the final value of `beautiful_count` for each test case in `test_cases`. Each `beautiful_count` represents the total count of pairs `(i, j)` in the corresponding array `a` such that `(a[i] + a[j]) % x == 0` and `(a[i] + a[j]) % y == 0`. The dictionary `freq` for each test case will contain the frequency of each pair `(mod_x, mod_y)` for every element in the array `a`, where `mod_x` is the remainder when the element is divided by `x`, and `mod_y` is the remainder when the element is divided by `y`. All other variables (`t`, `test_cases`, `case`, `n`, `x`, `y`, `a`, `num`) retain their initial values or are reset for each new test case.
    return results
    #The program returns the list `results` which contains the final value of `beautiful_count` for each test case in `test_cases`. Each `beautiful_count` is the total count of pairs `(i, j)` in the corresponding array `a` such that `(a[i] + a[j]) % x == 0` and `(a[i] + a[j]) % y == 0`.
#Overall this is what the function does:The function `func_1` takes two parameters: a positive integer `t` and a list of test cases `test_cases`. Each test case is a dictionary containing a tuple `('params')` with three integers `(n, x, y)` and a list `('array')` of `n` integers. The function returns a list `results` where each element corresponds to the count of pairs `(i, j)` in the respective array `a` such that `(a[i] + a[j]) % x == 0` and `(a[i] + a[j]) % y == 0`. The original input parameters `t` and `test_cases` remain unchanged.

