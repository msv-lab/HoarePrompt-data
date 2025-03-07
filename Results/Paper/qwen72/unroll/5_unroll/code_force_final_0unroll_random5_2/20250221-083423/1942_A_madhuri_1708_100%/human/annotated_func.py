#State of the program right berfore the function call: The function should take two integers, n and k, as input where 1 ≤ k ≤ n ≤ 10^3, and return a list of n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9 for each 1 ≤ i ≤ n, and exactly k of the n cyclic shifts of the list are sorted. If no such list exists, the function should return -1.
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
        
    #State: The loop reads each line from the input (excluding the first line), splits the line into two integers n and k, and then prints a list of n integers based on the conditions: if k is greater than or equal to 2, it prints a list of n integers all equal to k if n equals k, otherwise it prints -1. If k is less than 2, it prints a list of integers from 1 to n. The loop continues until all lines are processed.
#Overall this is what the function does:The function reads multiple lines of input, each containing two integers `n` and `k` (1 ≤ k ≤ n ≤ 10^3). For each line, it prints a list of `n` integers based on the following conditions: If `k` is greater than or equal to 2, it prints a list of `n` integers all equal to `k` if `n` equals `k`, otherwise it prints `-1`. If `k` is less than 2, it prints a list of integers from 1 to `n`. The function does not return any value; it only prints the results. After processing all lines, the function concludes.

