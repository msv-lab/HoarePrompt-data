#State of the program right berfore the function call: Each test case contains integers n, m, and k where 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 · 10^5. For each of the m pairs of friends, the input provides three integers a_i, b_i, and f_i where a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. All pairs of friends are distinct. The sum of n over all test cases does not exceed 10^5, the sum of m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2 · 10^5.
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
        
    #State: The printed results of the formula for each of the t iterations, each result being an integer between 0 and 1000000006.
#Overall this is what the function does:The function reads multiple test cases, each consisting of integers `n`, `m`, and `k`, representing the number of individuals, the number of friendship pairs, and an integer `k`, respectively. For each test case, it also reads `m` sets of integers `a_i`, `b_i`, and `f_i`, where `a_i` and `b_i` are distinct individuals and `f_i` is a value associated with their friendship. The function computes and prints an integer result for each test case based on these inputs, ensuring the result is within the range of 0 to 1000000006.

