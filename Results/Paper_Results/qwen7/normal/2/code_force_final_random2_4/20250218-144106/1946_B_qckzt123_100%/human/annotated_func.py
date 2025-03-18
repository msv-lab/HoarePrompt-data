#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n, k ≤ 2 ⋅ 10^5, and the sum of the values of n and k for all test cases does not exceed 2 ⋅ 10^5. a is a list of n integers where each integer a_i satisfies -10^9 ≤ a_i ≤ 10^9.
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
        
    #State: After the loop executes all its iterations, `i` will be equal to `k-1`, `t` will be \(2^{k-1} \mod \text{MOD}\), and `ans` will be the sum of all `t` values from \(2^0 \mod \text{MOD}\) to \(2^{k-1} \mod \text{MOD}\) modulo `MOD`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers `a` and two positive integers `n` and `k`. For each test case, it calculates a value `t` which is the maximum subarray sum of `a` where negative sums are discarded. It then computes a result `ans` based on `s` (the sum of all elements in `a`), `t`, and `k`. Specifically, `ans` is the sum of `s + t` modulo `MOD`, plus the sum of powers of 2 up to `2^(k-1)` modulo `MOD`. Finally, it prints the computed `ans` for each test case.

