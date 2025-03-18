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
        
    #State: `n` and `m` are integers derived from the input string such that `min(n, m)` must be at least 2, `b` is `min(n, m) + 1`, `t` is 0, `T` is `t`, `ans` is the sum of `n + sum((n + b) // (b * b) for b in range(2, min(n, m) + 1))` for each iteration.
#Overall this is what the function does:The function reads an integer `t` from the input, representing the number of test cases. For each test case, it reads two integers `n` and `m` from the input, where both are positive integers between 1 and 2 * 10^6. It then calculates a value `ans` starting from `n` and adds to it the result of `(n + b) // (b * b)` for each integer `b` from 2 to `min(n, m)`. Finally, it prints the calculated value `ans` for each test case. After processing all test cases, the function completes without returning any value.

