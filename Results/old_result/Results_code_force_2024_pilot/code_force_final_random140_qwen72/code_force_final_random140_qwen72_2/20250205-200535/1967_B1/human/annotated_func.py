#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func():
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = 0
        
        for b in range(1, min(n, m) + 1):
            ans = ans + n // b + 1
        
        print(ans)
        
    #State: After all iterations, `n` and `m` are integers from input such that `min(n, m) >= 1`, `b` is `min(n, m) + 1`, `t` is a positive integer, `T` is `t - 1`, `ans` is the sum of `n // i + 1` for each `i` from 1 to `min(n, m)` for each iteration.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two positive integers `n` and `m` (where 1 <= n, m <= 2 * 10^6). It then calculates a value `ans` by summing up `n // b + 1` for each `b` from 1 to `min(n, m)`. Finally, it prints the calculated `ans` for each test case. The function does not return any value; it only prints the results.

