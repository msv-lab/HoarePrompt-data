#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^3, and the sum of n over all test cases does not exceed 10^3.
def func():
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: Output State: After the loop executes all the iterations, `res` is either `[1] * n` if `k` equals `n`, `range(n)` if `k` equals `1`, otherwise `[-1]`, `t` is `0`.
    #
    #Explanation: The loop runs `t` times, where `t` is the initial input integer. After all iterations, `t` will be reduced to `0` since we subtract `1` from `t` in each iteration of the loop. Therefore, after all the executions of the loop have finished, `t` will be `0`. The value of `res` will depend on the values of `n` and `k` provided during each iteration of the loop, but it will be one of the three possible states defined within the loop body: `[1] * n` if `k` equals `n`, `range(n)` if `k` equals `1`, otherwise `[-1]`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( k \), where \( 1 \leq k \leq n \leq 10^3 \). For each test case, it generates a list `res` based on the values of \( n \) and \( k \): if \( k \) equals \( n \), it creates a list of \( n \) ones; if \( k \) equals 1, it creates a list of integers from 0 to \( n-1 \); otherwise, it creates a list containing only -1. The function prints the list `res` for each test case and does not return any value. After processing all test cases, it outputs the final state where the loop counter `t` is reduced to 0.

