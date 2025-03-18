#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n and k are integers such that 1 <= n, k <= 2 \cdot 10^5, and a is a list of n integers where -10^9 <= a_i <= 10^9. The sum of the values of n and k for all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` and `k` are integers such that 1 <= n, k <= 2 \cdot 10^5, and `a` is a list of n integers where -10^9 <= a_i <= 10^9. The sum of the values of `n` and `k` for all test cases does not exceed 2 \cdot 10^5. `MOD` is 1000000007, `T` is an integer read from the input and stripped of any leading or trailing whitespace. After the loop, `ans` is the final computed value for each test case, and `t` is the maximum subarray sum found in the last iteration of the inner loop for each test case, modulo `MOD`.
#Overall this is what the function does:The function reads a series of test cases from standard input. For each test case, it takes the number of elements `n` and a multiplier `k`, followed by a list of `n` integers `a`. It computes a value `ans` based on the sum of the elements in `a` and the maximum subarray sum found in `a`, then applies a series of transformations involving the multiplier `k` and a modulus operation. Finally, it prints the computed value `ans` for each test case. The function does not return any value.

