#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. Each test case in test_cases is a list containing three elements: n (an integer such that 1 <= n <= 10^5), x (an integer such that 0 <= x < 2^30), and a list of n integers a_1, a_2, ..., a_n (each a_i is an integer such that 0 <= a_i < 2^30). The sum of the values of n across all test cases does not exceed 10^5.
def func_1(t, test_cases):
    results = []
    for case in test_cases:
        n, x, a = case
        
        prefix_xor = [0] * (n + 1)
        
        for i in range(1, n + 1):
            prefix_xor[i] = prefix_xor[i - 1] ^ a[i - 1]
        
        current_xor = 0
        
        segment_count = 0
        
        valid = False
        
        for i in range(1, n + 1):
            current_xor ^= a[i - 1]
            if current_xor | prefix_xor[n] <= x:
                segment_count += 1
                current_xor = 0
                valid = True
        
        if valid:
            results.append(segment_count)
        else:
            results.append(-1)
        
    #State of the program after the  for loop has been executed: `prefix_xor` is a list of length `n + 1` where `prefix_xor[i]` is the cumulative XOR of the first `i-1` elements of the list `a`, `i` is `n + 1`, `current_xor` is `0`, `segment_count` is the total number of segments found, `valid` is `True` if any segment was found satisfying the condition, `results` is a list containing `segment_count` if `valid` is `True`, otherwise `results` is `[-1]`
    return results
    #The program returns results which is a list containing `segment_count` if `valid` is `True`, otherwise `results` is `[-1]`
#Overall this is what the function does:The function `func_1` accepts a positive integer `t` and a list of test cases. Each test case consists of an integer `n`, an integer `x`, and a list of `n` integers `a`. The function calculates the number of segments within each list `a` such that the bitwise XOR of the segment and the bitwise XOR of the remaining elements in the list do not exceed `x`. If such segments exist, it counts them; otherwise, it returns `-1` for that test case. The function returns a list of results, where each result corresponds to a test case in the input and indicates the count of valid segments or `-1` if no valid segments are found.

