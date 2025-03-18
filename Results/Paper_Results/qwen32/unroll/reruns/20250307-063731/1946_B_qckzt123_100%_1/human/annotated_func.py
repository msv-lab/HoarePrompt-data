#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and k are integers such that 1 <= n, k <= 2 * 10^5, and a is a list of n integers where each integer a_i satisfies -10^9 <= a_i <= 10^9. The sum of n and k across all test cases does not exceed 2 * 10^5.
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
        
    #State: - The variable `T` remains unchanged as it is the number of test cases.
    #   - The variable `t` is reset to 0 at the start of each iteration and is not retained across iterations.
    #   - The variables `n`, `k`, `a`, `s`, `tmp`, and `ans` hold the values from the last test case processed.
    #
    #Given the above analysis, the final state of the variables after all iterations is:
    #
    #- `T` remains the same as the initial state.
    #- `t` is 0 because it is reset at the start of each iteration.
    #- `n`, `k`, `a`, `s`, `tmp`, and `ans` hold the values from the last test case.
    #
    #Therefore, the output state is:
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases. For each test case, it calculates a result based on the sum of a list of integers and the maximum non-negative subarray sum, then applies a series of operations involving a multiplier `k` and a modulus `MOD`. The result for each test case is printed.

