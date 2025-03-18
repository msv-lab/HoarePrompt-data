#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. Each element in cases is a tuple (n, k) where n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n. The sum of n over all test cases does not exceed 10^7.
def func_1(t, cases):
    results = []
    sequence = [(2 ** i) for i in range(25)]
    for (n, k) in cases:
        results.append((25, sequence))
        
    #State: `t` is an integer such that 1 <= t <= 1000. Each element in `cases` is a tuple (n, k) where n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n. The sum of n over all test cases does not exceed 10^7. `results` is a list containing `t` elements, each of which is a tuple (25, sequence). `sequence` is a list containing [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216].
    return results
    #The program returns a list `results` containing `t` elements, where each element is a tuple (25, sequence). The `sequence` is a predefined list of 25 integers: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216].
#Overall this is what the function does:The function `func_1` accepts an integer `t` and a list `cases` containing `t` tuples, where each tuple consists of two integers `n` and `k`. It returns a list `results` containing `t` elements, where each element is a tuple (25, sequence). The `sequence` is a predefined list of 25 integers: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216]. The values of `n` and `k` in each tuple do not influence the output sequence.

