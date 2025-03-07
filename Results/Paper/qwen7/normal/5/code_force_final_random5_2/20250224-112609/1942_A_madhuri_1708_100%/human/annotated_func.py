#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^3, and the sum of n over all test cases does not exceed 10^3.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k >= 2:
            if n == k:
                print(*[k for j in range(k)])
            else:
                print('-1')
        else:
            print(*[(j + 1) for j in range(n)])
        
    #State: Output State: The loop will continue to read lines from standard input until there are no more lines to read. For each line, it will parse `n` and `k` as integers. If `k` is greater than or equal to 2, the loop will check if `n` equals `k`. If they are equal, it will print a list with `k` occurrences of `k`. If `n` does not equal `k`, it will print `-1`. If `k` is less than 2, it will print a list with `n` occurrences of integers starting from 1 up to `n`.
    #
    #The final output state will be determined by all the lines processed by the loop. Each line processed will contribute to the output based on the conditions specified in the loop body. If the end of the input is reached, the loop will terminate, and the output will consist of all the printed lists from each iteration.
#Overall this is what the function does:The function processes input data from standard input, where each line contains two integers \( n \) and \( k \) separated by a space, with \( 1 \leq k \leq n \leq 10^3 \). For each line, if \( k \geq 2 \), it checks if \( n \) equals \( k \); if true, it prints a list with \( k \) occurrences of \( k \); otherwise, it prints \(-1\). If \( k < 2 \), it prints a list with \( n \) occurrences of integers starting from 1 up to \( n \). The function continues processing lines until the end of input is reached, and it does not return any value.

