#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4, for each test case, n, m, and k are integers where 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 · 10^5. Each of the next m lines contains three integers a_i, b_i, and f_i, where 1 ≤ a_i, b_i ≤ n, a_i ≠ b_i, and 1 ≤ f_i ≤ 10^9. The sum of n and the sum of m over all test cases do not exceed 10^5, and the sum of k over all test cases does not exceed 2 · 10^5.
def func():
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        M = 10 ** 9 + 7
        
        c = pow(n * (n - 1) // 1, -1, M)
        
        s = 0
        
        a = 0
        
        for i in range(m):
            u, v, f = map(int, input().split())
            a += f
        
        for i in range(k):
            s = s + c * i * c * m + c * a
        
        print(s % M)
        
    #State: The loop has completed all iterations, `i` is `t-1`, `t` is the total number of test cases, `n`, `m`, and `k` have been processed for each test case, `s` is the final accumulated value modulo `M` for each test case, `a` is the sum of all `f` values for each test case, `c` is the modular multiplicative inverse of `n * (n - 1) // 1` modulo `M`, `u`, `v`, and `f` are the last values read from the input for each test case, and `M` is 1000000007.
#Overall this is what the function does:The function `func` processes a series of test cases. It reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `n`, `m`, and `k` with specific constraints, and then reads `m` lines of input, each containing three integers `a_i`, `b_i`, and `f_i`. It calculates a final accumulated value `s` using modular arithmetic and prints `s` modulo `10^9 + 7` for each test case. The function does not return any value; it only prints the results.

