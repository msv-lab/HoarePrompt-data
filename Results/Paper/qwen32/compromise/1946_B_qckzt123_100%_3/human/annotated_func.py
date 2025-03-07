#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n, k ≤ 2 · 10^5, and a is a list of n integers where each element a_i satisfies -10^9 ≤ a_i ≤ 10^9. The sum of all n and k across all test cases does not exceed 2 · 10^5.
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
        
    #State: T is 0; n, k, a, s, t, tmp, ans are the values from the last test case.
#Overall this is what the function does:The function reads multiple test cases from standard input. For each test case, it calculates a result based on the sum of a list of integers and the maximum subarray sum, then prints this result modulo \(10^9 + 7\). The calculation involves doubling the maximum subarray sum up to \(k-1\) times and adding these values to the total sum of the list, all while taking care to handle large numbers using modulo operations.

