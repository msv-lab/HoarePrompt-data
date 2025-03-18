#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 5 · 10^4, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 10^5, m is an integer where 0 ≤ m ≤ min(10^5, n(n-1)/2), and k is an integer where 1 ≤ k ≤ 2 · 10^5, representing the number of children, pairs of friends, and excursions, respectively. The next m lines contain three integers each: a_i, b_i, and f_i, where 1 ≤ a_i, b_i ≤ n, a_i ≠ b_i, and 1 ≤ f_i ≤ 10^9, representing the indices of the pair of children who are friends and their initial friendship value. The sum of n and the sum of m over all test cases do not exceed 10^5, and the sum of k over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is an integer where 1 ≤ t ≤ 5 · 10^4, `i` is `k - 1`, `n`, `m`, and `k` are integers provided by the user, `M` is 1000000007, `c` is the modular multiplicative inverse of `n * (n - 1) // 1` modulo `M`, `s` is updated to `s + c * (0 * m + 1 * m + 2 * m + ... + (k-1) * m) + c * a * k`, `a` is the sum of all `f` values provided by the user over `m` iterations, `u`, `v`, and `f` are updated with the final values provided by the user in the last iteration, `m` must be greater than or equal to 0, and `k` must be greater than or equal to 3.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by the number of children `n`, the number of pairs of friends `m`, and the number of excursions `k`. For each test case, it reads `m` lines of input, each containing the indices of a pair of children who are friends and their initial friendship value. The function calculates a value `s` using modular arithmetic, where `s` is updated based on the sum of friendship values and the number of excursions. After processing all test cases, the function prints the final value of `s` for each test case, modulo `10^9 + 7`. The function does not return any value but prints the results directly.

