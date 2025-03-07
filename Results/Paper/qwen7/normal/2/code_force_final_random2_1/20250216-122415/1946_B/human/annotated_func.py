#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n, k ≤ 2 \cdot 10^5, and the sum of the values of n and k for all test cases does not exceed 2 \cdot 10^5. a is a list of n integers where each integer a_i satisfies -10^9 ≤ a_i ≤ 10^9.
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
        
    #State: Output State: `i` is `k-1`, `k` must be greater than 0, `ans` is ((((s + t) % MOD + MOD) % MOD + t % MOD) * (2^k - 1)) % MOD, `a` is an empty list, `tmp` is equal to `t`, `t` is `2^k * t % MOD`.
    #
    #In this final state, after the loop has executed all its iterations, the variable `i` will be `k-1` since the loop runs from `0` to `k-2`. The variable `t` will be updated to `2^k * t % MOD` because it gets multiplied by `2` in each iteration. The variable `ans` accumulates the value of `t` in each iteration, starting from `((s + t) % MOD + MOD) % MOD` and adding `t` for each iteration, resulting in `(((s + t) % MOD + MOD) % MOD + t % MOD) * (2^k - 1)`. The variable `a` remains an empty list as it is not affected by the loop, and `tmp` remains equal to `t` as it is not reassigned within the loop. Finally, `ans` is taken modulo `MOD` to ensure it stays within the required range.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a list of integers `a` with length `n`, and two positive integers `n` and `k`. It calculates a result based on the sum of the list `a`, the maximum subarray sum starting from any point, and the value of `2^k % MOD`. The final output is the accumulated value of `t` for `k` iterations, adjusted by the initial sum and maximum subarray sum, all taken modulo `1000000007`.

