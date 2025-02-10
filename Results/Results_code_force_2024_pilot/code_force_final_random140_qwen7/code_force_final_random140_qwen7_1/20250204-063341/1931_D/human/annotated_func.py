#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; each test case is a list containing three integers n, x, and y such that 2 ≤ n ≤ 2⋅10^5 and 1 ≤ x, y ≤ 10^9; and each test case also includes a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: After all iterations of the loop have finished, `results` will contain a list of integers where each integer represents the value of `beautiful_count` computed for each `case` in `test_cases`. The length of `results` will be equal to the number of cases in `test_cases`. For each case, `beautiful_count` is calculated based on the given logic involving modulus operations and frequency counting of specific `(mod_x, mod_y)` pairs within the array `a`.
    return results
    #The program returns a list of integers named 'results', where each integer represents the value of 'beautiful_count' computed for each 'case' in 'test_cases'. The length of 'results' is equal to the number of cases in 'test_cases'. Each 'beautiful_count' is calculated based on the given logic involving modulus operations and frequency counting of specific (mod_x, mod_y) pairs within the array 'a'.
#Overall this is what the function does:The function accepts a positive integer `t` and a list of test cases, where each test case consists of three integers `n`, `x`, and `y`, followed by a list of `n` integers. For each test case, it calculates the number of "beautiful" elements in the array based on specific modulus conditions and stores these counts in a list. Finally, it returns this list of counts.

