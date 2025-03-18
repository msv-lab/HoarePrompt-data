#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n, k ≤ 2 · 10^5, representing the length of the array a and the number of operations, respectively. a is a list of n integers where -10^9 ≤ a_i ≤ 10^9, representing the array a. The sum of the values of n and k over all test cases does not exceed 2 · 10^5.
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
        
    #State: `T` is an integer read from the standard input, 1 ≤ `T` ≤ 10^4; `_` is `T-1`; `n` and `k` are integers read from the last line of standard input with `k` > 0; `a` is a list of integers read from the last line of standard input and must have `n` elements; `s` is the sum of the elements in `a`; `t` is `((2 * (the maximum subarray sum of non-negative contiguous subarrays in `a`)) % MOD) * (2^(k-1)) % MOD`; `i` is `0`; `ans` is `(((s + t) % MOD + MOD) % MOD + (t * (2^(k-1) - 1)) % MOD) % MOD`.
#Overall this is what the function does:The function `func` reads from the standard input a series of test cases, each consisting of an integer `n` and an integer `k`, followed by a list of `n` integers `a`. For each test case, it calculates a value based on the sum of the elements in `a`, the maximum subarray sum of non-negative contiguous subarrays in `a`, and the number of operations `k`. The result for each test case is printed to the standard output, and the function does not return any value. After processing all test cases, the function completes its execution.

