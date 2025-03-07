#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n and k are integers where 1 ≤ n, k ≤ 2 · 10^5, and a is a list of n integers where -10^9 ≤ a_i ≤ 10^9. The sum of the values of n and k for all test cases does not exceed 2 · 10^5.
def func():
    MOD = 1000000007
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        n, k = map(int, sys.stdin.readline().strip().split())
        
        a = list(map(int, sys.stdin.readline().strip().split()))
        
        s = sum(a)
        
        t, tmp = 0, 0
        
        for x in a:
            tmp += x
            if tmp < 0:
                tmp = 0
            t = max(tmp, t)
        
        ans = ((s + t) % MOD + MOD) % MOD
        
        for i in range(k - 1):
            t *= 2
            t %= MOD
            ans += t
            ans %= MOD
        
        print(ans)
        
    #State: The variable `T` is decremented by the number of iterations that have been completed. The variables `n`, `k`, and `a` are updated for each iteration based on the input. The variable `s` is the sum of the list `a` for the current iteration. The variable `t` is the maximum subarray sum ending at any index in the list `a` for the current iteration, but reset to 0 at the start of each iteration. The variable `tmp` is the running sum used to calculate `t` and is reset to 0 at the start of each iteration. The variable `ans` is the final computed value for the current iteration, which is printed. The variable `MOD` remains unchanged.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of the integers `n` and `k`, followed by a list `a` of `n` integers. For each test case, it calculates the sum of the list `a` and the maximum subarray sum that is non-negative. It then computes a final result using these values and the number of iterations `k`, applying a modulo operation to ensure the result is within a specified range. The function prints the final result for each test case. The state of the program after the function concludes includes the `T` variable being decremented by the number of test cases processed, and the variables `n`, `k`, `a`, `s`, `t`, `tmp`, and `ans` being updated for each test case. The `MOD` variable remains unchanged.

