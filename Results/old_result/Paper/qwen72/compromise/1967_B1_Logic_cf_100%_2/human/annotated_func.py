#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func():
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: After all iterations of the loop, `n` and `m` are integers with `min(n, m) >= 2`, `t` is the input integer, `T` is `t - 1`, `ans` is `n + sum((n + b) // (b * b) for b in range(2, min(n, m) + 1))`, and `b` is `min(n, m) + 1`.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two positive integers `n` and `m` from the input. It then calculates a value `ans` starting from `n` and adds to it the sum of `(n + b) // (b * b)` for all integers `b` from 2 to `min(n, m)`. Finally, it prints the calculated value `ans` for each test case. After the function completes, the input values `t`, `n`, and `m` are consumed, and the function has no side effects other than printing the results.

