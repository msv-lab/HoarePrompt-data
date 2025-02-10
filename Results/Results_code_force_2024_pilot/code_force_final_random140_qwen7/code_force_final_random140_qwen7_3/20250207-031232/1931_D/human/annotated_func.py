#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. Each test case in test_cases is a list containing three integers n, x, and y such that 2 <= n <= 2 * 10^5 and 1 <= x, y <= 10^9. Additionally, test_cases is a list of such triplets, and the sum of n over all test cases does not exceed 2 * 10^5. Each element a_i in the array a for each test case satisfies 1 <= a_i <= 10^9.
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
        
    #State: Output State: The `results` list will contain the final value of `beautiful_count` after all iterations of the loop have completed. This value represents the total count of pairs `(mod_x, required_mod_y)` found across all elements in all arrays specified in `test_cases`. All other variables such as `a`, `x`, `y`, `mod_x`, `mod_y`, `freq`, and `beautiful_count` will retain their final values from the last iteration of the loop. The `test_cases` list will also remain unchanged, as it was initialized and used within the loop but not modified outside of it.
    return results
    #The program returns the results list which contains the final value of beautiful_count after all iterations of the loop have completed. This value represents the total count of pairs (mod_x, required_mod_y) found across all elements in all arrays specified in test_cases. All other variables such as a, x, y, mod_x, mod_y, freq, and beautiful_count will retain their final values from the last iteration of the loop. The test_cases list will also remain unchanged, as it was initialized and used within the loop but not modified outside of it.
#Overall this is what the function does:The function `func_1` takes two parameters: `t`, a positive integer between 1 and 10^4, and `test_cases`, a list of triplets where each triplet consists of integers `n`, `x`, and `y`. For each triplet, it processes an array `a` of length `n`, where each element `a_i` is between 1 and 10^9. It calculates the total count of pairs `(mod_x, required_mod_y)` across all arrays specified in `test_cases` and returns a list containing this count. After processing, all local variables such as `a`, `x`, `y`, `mod_x`, `mod_y`, `freq`, and `beautiful_count` retain their final values from the last iteration of the loop, while `test_cases` remains unchanged.

