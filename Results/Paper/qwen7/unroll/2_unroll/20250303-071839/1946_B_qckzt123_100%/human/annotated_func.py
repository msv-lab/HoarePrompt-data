#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n, k ≤ 2 ⋅ 10^5, and the sum of the values of n and k for all test cases does not exceed 2 ⋅ 10^5. The array a is a list of n integers where each integer a_i satisfies -10^9 ≤ a_i ≤ 10^9.
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
        
    #State: The output state will consist of multiple lines, each corresponding to the output of one iteration of the loop. For each line, the value printed will be the result of the calculation based on the given inputs n, k, and array a, modulo 1000000007. The specific values depend on the input provided through standard input during each iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer \( t \), two positive integers \( n \) and \( k \), and an array \( a \) of \( n \) integers. For each test case, it calculates a value based on the sum of the array \( a \) and a modified version of the maximum subarray sum, then applies a series of modular arithmetic operations. Finally, it prints the result for each test case, which is the calculated value modulo \( 1000000007 \).

