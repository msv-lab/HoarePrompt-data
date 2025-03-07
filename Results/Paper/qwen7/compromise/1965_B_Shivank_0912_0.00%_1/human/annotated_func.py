#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and cases is a list of tuples, where each tuple contains two integers n and k such that 2 <= n <= 10^6 and 1 <= k <= n. Additionally, the sum of n over all test cases does not exceed 10^7.
def func_1(t, cases):
    results = []
    sequence = [(2 ** i) for i in range(25)]
    for (n, k) in cases:
        results.append((25, sequence))
        
    #State: Output State: `t` is a positive integer such that 1 <= t <= 1000, `cases` is a list of tuples where each tuple contains two integers n and k such that 2 <= n <= 10^6 and 1 <= k <= n, and `results` is a list of tuples where each tuple contains (25, [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608]), and `sequence` is a list containing the first 25 powers of 2 starting from 2^0.
    return results
    #The program returns a list of tuples, where each tuple contains (25, [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608]), and the sequence is a list containing the first 25 powers of 2 starting from 2^0.
#Overall this is what the function does:The function `func_1` accepts two parameters: `t`, a positive integer between 1 and 1000, and `cases`, a list of tuples where each tuple contains two integers `n` and `k` with specific constraints. The function creates a fixed list `sequence` containing the first 25 powers of 2 starting from \(2^0\). For each tuple in `cases`, the function appends a tuple `(25, sequence)` to the `results` list. Finally, the function returns the `results` list, which consists of tuples where each tuple contains (25, [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608]).

