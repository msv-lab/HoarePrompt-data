#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, and for each test case, n and k are integers such that 1 <= k <= n <= 10^3.
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
        
    #State: The loop reads each line from the input (excluding the first line) and processes it according to the given conditions. For each line, it splits the line into two integers n and k. If k is greater than or equal to 2, and n equals k, it prints a sequence of k integers, each equal to k. If k is greater than or equal to 2 and n does not equal k, it prints -1. If k is less than 2, it prints a sequence of integers from 1 to n. The values of t, n, and k remain unchanged after the loop execution, but the output is generated based on the input lines.
#Overall this is what the function does:The function reads multiple lines of input from the standard input, where the first line specifies the number of test cases `t` (1 <= t <= 10^3). For each subsequent line, it processes two integers `n` and `k` (1 <= k <= n <= 10^3). If `k` is greater than or equal to 2 and `n` equals `k`, it prints a sequence of `k` integers, each equal to `k`. If `k` is greater than or equal to 2 and `n` does not equal `k`, it prints `-1`. If `k` is less than 2, it prints a sequence of integers from 1 to `n`. The function does not return any value; it only prints the results to the standard output. The values of `t`, `n`, and `k` are not modified by the function.

