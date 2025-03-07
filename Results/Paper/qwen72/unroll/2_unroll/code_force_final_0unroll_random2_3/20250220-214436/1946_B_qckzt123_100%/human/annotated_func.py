#State of the program right berfore the function call: The function `func` is expected to take no input parameters, but based on the problem description, it should be defined to take input parameters `t`, `n`, `k`, and `a` where `t` is an integer representing the number of test cases (1 ≤ t ≤ 10^4), `n` and `k` are integers representing the length of the array and the number of operations (1 ≤ n, k ≤ 2 · 10^5), and `a` is a list of integers of length `n` (-10^9 ≤ a_i ≤ 10^9). The sum of the values of `n` and `k` for all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop has completed all iterations, and the final output state is that `T` is the initial integer value read from the standard input, `t` is the initial number of test cases, `n` and `k` are the last values read for the final test case, `a` is the last list of integers read for the final test case, and `ans` is the final computed answer for the last test case. The variables `s`, `tmp`, and `t` are no longer relevant after the loop completes.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an array `a` of length `n` and an integer `k` from the standard input. It computes a value `ans` based on the sum of the array and the maximum subarray sum that does not drop below zero, then applies `k` operations to this value. The result for each test case is printed to the standard output. After processing all test cases, the function completes without returning any value. The final state of the program is that all test cases have been processed and their results printed.

