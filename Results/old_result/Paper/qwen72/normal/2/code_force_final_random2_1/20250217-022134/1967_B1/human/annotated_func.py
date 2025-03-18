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
        
    #State: After all iterations of the loop, `n` and `m` are integers such that they are the last values read from input, `b` is `min(n, m) + 1`, `t` is the total number of iterations specified initially, `T` is `t - 1`, and `ans` is the final value calculated as `n + sum((n + b) // (b * b) for b in range(2, min(n, m) + 1))` for each iteration.
#Overall this is what the function does:The function reads an integer `t` from the input, representing the number of test cases. For each test case, it reads two positive integers `n` and `m` (where 1 <= n, m <= 2 * 10^6) from the input. It then calculates a value `ans` based on the formula `n + sum((n + b) // (b * b) for b in range(2, min(n, m) + 1))` and prints this value. After processing all `t` test cases, the function completes. The final state of the program includes the last values of `n` and `m` read from the input, the variable `b` set to `min(n, m) + 1`, `t` as the total number of test cases, and `T` as `t - 1`.

