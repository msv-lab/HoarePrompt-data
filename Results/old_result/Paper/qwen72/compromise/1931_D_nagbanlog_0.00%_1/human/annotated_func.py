#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), and test_cases is a list of tuples, where each tuple contains three elements: n, x, y, and a list a. For each tuple, n is an integer (2 ≤ n ≤ 2 · 10^5), x and y are integers (1 ≤ x, y ≤ 10^9), and a is a list of n integers (1 ≤ a_i ≤ 10^9). The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: After all iterations of the loop, `t` is a positive integer (1 ≤ t ≤ 10^4), `test_cases` is a list of tuples containing `t` tuples, `case` is the last tuple in `test_cases`, `results` is a list containing `t` elements where each element is the `beautiful_count` for the corresponding test case, `n` is the first value from the last `case['params']`, `x` is the second value from the last `case['params']`, `y` is the third value from the last `case['params']`, `a` is the array from the last `case['array']` and has been fully iterated over, `freq` is a dictionary where each key is a tuple `(mod_x, mod_y)` representing the modulus results of each element in the last `a` with `x` and `y`, and the corresponding value is the count of how many times that specific `(mod_x, mod_y)` pair appears in the last `a`. `beautiful_count` is the total count of "beautiful" pairs found in the last `a`, where a "beautiful" pair is defined as a pair of elements `(a[i], a[j])` such that `i < j` and `a[i] + x` is divisible by `x` and `a[i] + y` is divisible by `y`. The variables `num`, `mod_x`, `mod_y`, `required_mod_x`, and `required_mod_y` will hold the values corresponding to the last element processed in the last `a`.
    return results
    #The program returns a list `results` containing `t` elements, where each element is the `beautiful_count` for the corresponding test case. The `beautiful_count` is the total count of "beautiful" pairs found in each `a` array, where a "beautiful" pair is defined as a pair of elements `(a[i], a[j])` such that `i < j` and both `a[i] + x` is divisible by `x` and `a[i] + y` is divisible by `y`.
#Overall this is what the function does:The function `func_1` takes a positive integer `t` and a list of tuples `test_cases` as input. Each tuple in `test_cases` contains an integer `n`, two integers `x` and `y`, and a list `a` of `n` integers. The function processes each test case to count the number of "beautiful" pairs in the list `a`. A "beautiful" pair `(a[i], a[j])` is defined as a pair where `i < j` and both `a[i] + x` is divisible by `x` and `a[i] + y` is divisible by `y`. The function returns a list `results` of length `t`, where each element is the count of "beautiful" pairs for the corresponding test case.

