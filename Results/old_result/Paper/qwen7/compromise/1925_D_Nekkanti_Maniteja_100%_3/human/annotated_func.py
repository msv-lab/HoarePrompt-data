#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5⋅10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2⋅10^5. Each of the next m lines contains three integers a_i, b_i, and f_i such that a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. It is guaranteed that all pairs of friends are distinct, and the sum of n and the sum of m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The final value of `s` is calculated as the sum of `c * i * c * m + c * a` for all iterations from `i = 0` to `i = k-1`, plus additional terms for each subsequent iteration up to `i = k-1`. Specifically, for each iteration from `i = k` to `i = k-1`, the term `c * (i + m) * c * (i + m) * (m - (i - k + 1)) + c * a * m` is added to `s`. Here, `c` is the modular multiplicative inverse of `n * (n - 1) // 2` modulo `M`, `a` is the cumulative sum of `f` for all edges, `M` is \(10^9 + 7\), and `k` is the total number of iterations of the loop.
    #
    #In simpler terms, after all iterations of the loop, `s` accumulates the contributions from each edge `f` and the combinatorial terms based on the number of iterations and the modular multiplicative inverse `c`. The final value of `s` is then taken modulo \(10^9 + 7\).
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n, m, and k, along with m pairs of integers a_i and b_i, and an integer f_i. It calculates a value s based on the given inputs and a modular multiplicative inverse c, and prints the result of s modulo \(10^9 + 7\). The final value of s is derived from a combination of combinatorial terms and the cumulative sum of f_i values, ensuring all calculations are performed under modular arithmetic.

