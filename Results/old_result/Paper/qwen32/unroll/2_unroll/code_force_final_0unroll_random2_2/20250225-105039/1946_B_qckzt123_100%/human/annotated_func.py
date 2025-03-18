#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and k are integers such that 1 <= n, k <= 2 * 10^5. a is a list of n integers where each integer a_i satisfies -10^9 <= a_i <= 10^9. The sum of all n and k across all test cases does not exceed 2 * 10^5.
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
        
    #State: `T`, `n`, `k`, `a`, and `MOD` remain unchanged; `s`, `t`, `tmp`, and `ans` are the values calculated in the last iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `k`, and a list `a` of `n` integers. For each test case, it calculates a result based on the sum of the list, the maximum subarray sum, and the value of `k`. The result is printed for each test case.

