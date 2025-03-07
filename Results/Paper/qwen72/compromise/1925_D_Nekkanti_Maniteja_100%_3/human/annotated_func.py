#State of the program right berfore the function call: Each test case contains integers n, m, and k where 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 × 10^5. The next m lines contain integers a_i, b_i, and f_i where 1 ≤ a_i, b_i ≤ n, a_i ≠ b_i, and 1 ≤ f_i ≤ 10^9. The sum of n and the sum of m over all test cases do not exceed 10^5, and the sum of k over all test cases does not exceed 2 × 10^5.
def func():
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        M = 10 ** 9 + 7
        
        c = pow(n * (n - 1) // 2, -1, M)
        
        s = 0
        
        a = 0
        
        for i in range(m):
            u, v, f = map(int, input().split())
            a += f
        
        for i in range(k):
            s = s + c * i * c * m + c * a
        
        print(s % M)
        
    #State: `i` is `k-1`, `n` is an input integer, `m` is an input integer, `k` is an input integer, `M` is 1000000007, `c` is the modular multiplicative inverse of `n * (n - 1) // 2` modulo `1000000007`, `a` is the sum of all `f` values from the `m` iterations, `s` is `c * a * k + c * m * c * (k * (k - 1) // 2) % M`.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by integers `n`, `m`, and `k`. For each test case, it reads `m` lines of input, each containing integers `a_i`, `b_i`, and `f_i`. The function calculates a value `s` based on the modular multiplicative inverse of `n * (n - 1) // 2` modulo `1000000007`, the sum of all `f_i` values, and the values of `k` and `m`. The final value of `s` is printed modulo `1000000007` for each test case.

