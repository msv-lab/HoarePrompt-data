#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n, k ≤ 2 \cdot 10^5, and the sum of the values of n and k for all test cases does not exceed 2 \cdot 10^5. The array a is a list of n integers where -10^9 ≤ a_i ≤ 10^9 for each element a_i in the array.
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
        
    #State: Output State: `T` is an integer read from standard input and stripped of whitespace, and 1 ≤ `T` ≤ 10^4; `MOD` is 1000000007; Each `ans` calculated for each test case after executing the loop body is summed up and then taken modulo `MOD`.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer t (1 ≤ t ≤ 10^4), two integers n and k (1 ≤ n, k ≤ 2⋅10^5) such that the sum of n and k across all test cases does not exceed 2⋅10^5, and an array a of n integers (-10^9 ≤ a_i ≤ 10^9). For each test case, it calculates a value based on the sum of the array and a specific transformation of its elements, applies a series of modular arithmetic operations, and prints the result. After processing all test cases, it outputs the final results for each test case, each taken modulo 1000000007.

