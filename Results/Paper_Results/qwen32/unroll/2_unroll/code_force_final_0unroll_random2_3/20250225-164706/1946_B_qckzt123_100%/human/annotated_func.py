#State of the program right berfore the function call: The input consists of several test cases. Each test case starts with two integers n and k (1 ≤ n, k ≤ 2 · 10^5) representing the length of the array and the number of operations, respectively. This is followed by a line containing n integers a_1, a_2, ..., a_n (-10^9 ≤ a_i ≤ 10^9) representing the array itself. The sum of n and k across all test cases does not exceed 2 · 10^5.
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
        
    #State: Variables `n`, `k`, `a`, `s`, `t`, `tmp`, and `ans` will hold the values from the last test case processed. `T` and `MOD` remain unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an array of integers and a number of operations. For each test case, it calculates a result based on the sum of the array, the maximum subarray sum, and a series of operations that involve doubling the maximum subarray sum a specified number of times. The result is then printed for each test case.

