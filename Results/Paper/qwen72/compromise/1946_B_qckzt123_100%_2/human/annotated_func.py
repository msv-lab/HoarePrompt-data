#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n, k ≤ 2 · 10^5, representing the length of the array a and the number of operations, respectively. a is a list of n integers where -10^9 ≤ a_i ≤ 10^9, representing the array a. The sum of the values of n and k for all test cases does not exceed 2 · 10^5.
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
        
    #State: After the loop has executed all iterations, `i` is `k-1`, `k` is greater than or equal to the number of iterations, `t` is `(2^(k-1) * initial_t) % MOD`, and `ans` is the remainder of (`initial_ans` + `sum of (2^j * initial_t) % MOD` for `j` from 1 to `k-1`) divided by `MOD`. The values of `tmp`, `_`, `T`, `n`, `a`, and `s` remain unchanged.
#Overall this is what the function does:The function reads multiple test cases from standard input, each consisting of the number of elements `n`, the number of operations `k`, and an array `a` of integers. For each test case, it calculates a value `ans` based on the sum of the array `a` and the maximum subarray sum that is non-negative. This value is then adjusted through a series of operations defined by `k`, and the final result is printed modulo `1000000007`. The function does not return any value; instead, it prints the result for each test case. After processing all test cases, the function completes without modifying the input parameters.

