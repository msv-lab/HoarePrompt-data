#State of the program right berfore the function call: Each test case consists of three integers n, m, and k, where 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 · 10^5. The next m lines contain three integers a_i, b_i, and f_i, where a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. All pairs (a_i, b_i) are distinct. The sum of n and m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2 · 10^5.
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
        
    #State: result1 result2 ... resultt
#Overall this is what the function does:The function reads multiple test cases, each consisting of three integers `n`, `m`, and `k`, and `m` lines of three integers representing edges and their associated values. It computes a specific mathematical result based on these inputs and prints the result for each test case. The result is a modular inverse calculation involving sums and combinations derived from the input values.

