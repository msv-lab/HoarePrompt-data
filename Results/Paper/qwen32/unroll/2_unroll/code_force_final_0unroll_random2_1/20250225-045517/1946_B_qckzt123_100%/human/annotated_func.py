#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and k are integers such that 1 <= n, k <= 2 * 10^5. a is a list of n integers where each integer a_i satisfies -10^9 <= a_i <= 10^9. The sum of the values of n and k for all test cases does not exceed 2 * 10^5.
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
        
    #State: `n`, `k`, `a`, `s`, `t`, and `ans` are the values corresponding to the last test case processed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it computes a result based on the sum of a list of integers `a`, the maximum subarray sum within `a`, and a multiplier `k`. It outputs the result for each test case, ensuring the result is within a specified modulus.

