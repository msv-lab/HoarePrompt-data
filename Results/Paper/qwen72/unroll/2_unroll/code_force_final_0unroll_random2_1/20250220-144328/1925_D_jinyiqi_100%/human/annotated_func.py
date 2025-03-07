#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case includes three integers n, m, and k, where n is the number of children (2 ≤ n ≤ 10^5), m is the number of pairs of friends (0 ≤ m ≤ min(10^5, n(n-1)/2)), and k is the number of excursions (1 ≤ k ≤ 2 × 10^5). Additionally, m lines follow, each containing three integers a_i, b_i, and f_i, representing the indices of the pair of children who are friends (1 ≤ a_i, b_i ≤ n, a_i ≠ b_i) and their initial friendship value (1 ≤ f_i ≤ 10^9). The sum of n and the sum of m over all test cases do not exceed 10^5, and the sum of k over all test cases does not exceed 2 × 10^5. The function should return an integer for each test case, which is the answer to the problem modulo (10^9 + 7).
def func():
    t = int(input())
    M = 10 ** 9 + 7
    for i in range(t):
        n, m, k = map(int, input().split())
        
        sum_f = 0
        
        for j in range(m):
            a, b, f = map(int, input().split())
            sum_f += f
        
        cn2 = n * (n - 1) // 2
        
        p = 2 * k * cn2 * sum_f + m * k * (k - 1)
        
        q = 2 * cn2 ** 2
        
        gcd = math.gcd(p, q)
        
        p = p // gcd
        
        q = q // gcd
        
        print(int(p * pow(q, -1, M) % M))
        
    #State: The function `func` processes all test cases and prints the result for each test case. The variables `n`, `m`, `k`, `sum_f`, `cn2`, `p`, `q`, and `gcd` are updated and used within each iteration of the loop, but their values are reset for each new test case. Therefore, after all iterations of the loop, the state of these variables is not retained and is irrelevant. The only relevant state is the number of test cases `t`, which remains unchanged.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of three integers `n`, `m`, and `k`, and `m` lines of friendship data. It calculates and prints an integer result for each test case, which is the answer to a specific problem modulo (10^9 + 7). The function does not return any values; instead, it directly prints the results. After processing all test cases, the function does not retain any state from the processed test cases, and the only variable that remains unchanged is the number of test cases `t`.

