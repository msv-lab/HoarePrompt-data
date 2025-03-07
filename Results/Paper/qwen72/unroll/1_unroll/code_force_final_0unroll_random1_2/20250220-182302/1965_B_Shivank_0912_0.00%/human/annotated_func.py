#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and cases is a list of tuples where each tuple contains two integers n and k such that 2 <= n <= 10^6 and 1 <= k <= n.
def func_1(t, cases):
    results = []
    sequence = [(2 ** i) for i in range(25)]
    for (n, k) in cases:
        results.append((25, sequence))
        
    #State: `t` is an integer such that 1 <= t <= 1000, `cases` is a list of tuples where each tuple contains two integers n and k such that 2 <= n <= 10^6 and 1 <= k <= n. `results` is a list containing `t` elements, where each element is the tuple (25, sequence). `sequence` is a list of 25 elements where each element is 2 raised to the power of its index (i.e., `sequence[0] = 1`, `sequence[1] = 2`, `sequence[2] = 4`, ..., `sequence[24] = 16777216`).
    return results
    #The program returns a list `results` containing `t` elements, where each element is a tuple (25, sequence). The `sequence` in each tuple is a list of 25 elements, with each element being 2 raised to the power of its index, starting from 0. Therefore, `sequence[0] = 1`, `sequence[1] = 2`, `sequence[2] = 4`, ..., `sequence[24] = 16777216`.
#Overall this is what the function does:The function `func_1` accepts two parameters: `t`, an integer such that 1 <= t <= 1000, and `cases`, a list of tuples where each tuple contains two integers `n` and `k` such that 2 <= n <= 10^6 and 1 <= k <= n. It returns a list `results` containing `t` elements, where each element is the tuple (25, sequence). The `sequence` in each tuple is a list of 25 elements, with each element being 2 raised to the power of its index, starting from 0 (i.e., `sequence[0] = 1`, `sequence[1] = 2`, `sequence[2] = 4`, ..., `sequence[24] = 16777216`). The input parameters `t` and `cases` remain unchanged after the function call.

