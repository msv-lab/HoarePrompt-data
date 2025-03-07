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
        
    #State: Output State: `T` is an integer read from stdin and stripped of whitespace, and 1 ≤ `T` ≤ 10^4; `MOD` is 1000000007; For each input pair `(n, k)` and list `a`, the variable `ans` is calculated based on the given operations and summed up modulo `MOD`; After all iterations, `ans` contains the final result for each input, summed up and taken modulo `MOD`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer \( T \) (1 ≤ \( T \) ≤ 10^4), two positive integers \( n \) and \( k \) (1 ≤ \( n \), \( k \) ≤ 2⋅10^5, and the sum of \( n \) and \( k \) for all test cases does not exceed 2⋅10^5), and a list \( a \) of \( n \) integers (each integer \( a_i \) satisfies -10^9 ≤ \( a_i \) ≤ 10^9). For each test case, it calculates a value \( ans \) based on the sum of \( a \), the maximum subarray sum starting from any point, and the value of \( k \), then prints the result modulo \( MOD \) (1000000007). The function reads inputs from standard input and outputs results to standard output.

