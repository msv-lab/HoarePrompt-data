#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n, k ≤ 2 \cdot 10^5, and the sum of the values of n and k for all test cases does not exceed 2 \cdot 10^5. a is a list of n integers where -10^9 ≤ a_i ≤ 10^9.
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
        
    #State: Output State: `i` is equal to `k-1`, `t` is equal to `2^(k-1) % MOD`, and `ans` is equal to `(2^k - 1) % MOD`.
    #
    #Explanation: After the loop completes all its iterations, the value of `i` will be `k-1` because the loop runs `k-1` times. The variable `t` will hold the value `2^(k-1) % MOD` since it gets doubled in each iteration and takes modulo `MOD`. The variable `ans` will accumulate the sum of `t` values from `2^0 % MOD` to `2^(k-2) % MOD`, which simplifies to `(2^k - 1) % MOD` due to the properties of geometric series sums in modular arithmetic.
#Overall this is what the function does:The function processes a list of integers `a` and two positive integers `n` and `k`. It calculates a specific value based on the sum of the list and the maximum subarray sum (with zeros allowed), then performs a series of modular arithmetic operations involving powers of 2 up to `2^(k-1)`. Finally, it prints the computed result, which is `(2^k - 1) % MOD`.

