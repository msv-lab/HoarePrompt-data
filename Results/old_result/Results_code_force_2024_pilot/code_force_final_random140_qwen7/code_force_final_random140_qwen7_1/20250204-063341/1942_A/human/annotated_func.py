#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^3, and the sum of n over all test cases does not exceed 10^3.
def func():
    for _ in range(int(input())):
        n, k = list(map(int, input().split(' ')))
        
        if n == k:
            print(('1 ' * n)[:-1])
        elif k == 1:
            print(' '.join([str(x + 1) for x in range(n)]))
        else:
            print(-1)
        
    #State: Output State: The loop will continue to execute as long as there are more test cases indicated by `int(input())` being greater than 0. After all iterations, `n` and `k` will retain their values from each individual test case that was processed. There will be no final aggregated value for `n` and `k`; instead, they will reflect the last set of `n` and `k` values from the last test case executed.
    #
    #In other words, the output state after the loop executes all its iterations will be determined by the values of `n` and `k` from the last test case that was processed, with the condition that there must be at least one test case.
#Overall this is what the function does:The function processes multiple test cases, each containing integers \( n \) and \( k \). For each test case, it prints either a sequence of numbers or -1 based on the values of \( n \) and \( k \). Specifically, if \( n \) equals \( k \), it prints a sequence of \( n \) ones. If \( k \) equals 1, it prints a sequence of numbers from 1 to \( n \). Otherwise, it prints -1. After processing all test cases, the function outputs the result of the last test case, with no further aggregation of results.

