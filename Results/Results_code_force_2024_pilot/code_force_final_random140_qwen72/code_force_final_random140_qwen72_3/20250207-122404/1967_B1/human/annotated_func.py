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
        
    #State: After the loop executes all the iterations, `T` is `t - 1`, `t` is the initial value of `t`, `n` and `m` are the last pair of integers read from the input, `b` is `min(n, m) + 1`, and `ans` is the sum of `n // i + 1` for all `i` from 1 to `min(n, m)` for the last iteration.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two positive integers `n` and `m` (1 <= n, m <= 2 * 10^6). It calculates the sum of `n // i + 1` for all `i` from 1 to `min(n, m)` and prints the result. After processing all test cases, the function has no return value, but it has printed the results for each test case. The final state of the program includes the variable `T` being equal to `t - 1`, `t` retaining its initial value, `n` and `m` holding the values of the last test case, and `b` being `min(n, m) + 1`.

