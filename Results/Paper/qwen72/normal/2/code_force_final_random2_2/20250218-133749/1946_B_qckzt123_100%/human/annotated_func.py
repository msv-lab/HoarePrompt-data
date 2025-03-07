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
        
    #State: After the loop executes all the iterations, `T` is 0, `n` and `k` are the input integers for the last test case, `a` is the list of integers for the last test case, `s` is the sum of the elements in `a`, `t` is the maximum value of the cumulative sums of the subarrays of `a` that do not drop below zero, multiplied by \(2^{(k-1)}\) and taken modulo `MOD`, `tmp` is the last cumulative sum of the subarray being considered, which may be zero if it dropped below zero, `ans` is the final result of the computation for the last test case, which is `((s + t * (2^(k-1))) % MOD + MOD) % MOD` plus the sum of all intermediate values of `t` multiplied by their respective powers of 2 and taken modulo `MOD`, and `i` is `k-2`.
#Overall this is what the function does:The function reads multiple test cases from standard input, each consisting of an array `a` of integers and an integer `k`. For each test case, it calculates a result based on the sum of the array elements and the maximum non-negative subarray sum, adjusted by a series of operations involving multiplication and modulo arithmetic. The function prints the final result for each test case to standard output. After processing all test cases, the function completes without returning any value.

