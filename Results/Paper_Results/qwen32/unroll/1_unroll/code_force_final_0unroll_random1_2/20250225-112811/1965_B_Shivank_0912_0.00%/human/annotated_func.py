#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. cases is a list of tuples, where each tuple contains two integers n and k such that 2 <= n <= 10^6 and 1 <= k <= n. The sum of n over all tuples in cases does not exceed 10^7.
def func_1(t, cases):
    results = []
    sequence = [(2 ** i) for i in range(25)]
    for (n, k) in cases:
        results.append((25, sequence))
        
    #State: `t` is an integer such that 1 <= t <= 1000; `cases` is a list of tuples, where each tuple contains two integers n and k such that 2 <= n <= 10^6 and 1 <= k <= n; `results` is a list of tuples where each tuple is (25, sequence) repeated for each case in `cases`; `sequence` is a list containing [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216]
    return results
    #The program returns a list of tuples where each tuple is (25, sequence) repeated for each case in `cases`. Each `sequence` is a list containing [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216].
#Overall this is what the function does:The function accepts two parameters: `t`, an integer representing the number of cases, and `cases`, a list of tuples where each tuple contains two integers `n` and `k`. For each tuple in `cases`, the function generates a tuple `(25, sequence)` and appends it to a results list. The `sequence` is a predefined list of the first 25 powers of 2 starting from 2^0 up to 2^24. The function returns the results list containing these tuples for each case.

