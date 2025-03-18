#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers such that 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        print((k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k ==
            4 * n - 2))
        
    #State: Output State: The loop will continue to execute until there are no more lines of input left in the file. For each line, `s` will be the line of input, `n` will be the first integer split from `s`, and `k` will be the second integer split from `s`. After all iterations, the final output will consist of the results of the expression `(k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k == 4 * n - 2)` evaluated for each line of input.
    #
    #In simpler terms, after all iterations of the loop, the output will include the result of the given expression for every line of input provided, where each line contains two integers `n` and `k`.
#Overall this is what the function does:The function processes multiple lines of input, each containing two integers \( n \) and \( k \). For each line, it evaluates and prints the result of the expression \((k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k == 4 * n - 2)\). The function reads inputs from standard input until no more lines are available, then outputs the computed values for each line of input.

