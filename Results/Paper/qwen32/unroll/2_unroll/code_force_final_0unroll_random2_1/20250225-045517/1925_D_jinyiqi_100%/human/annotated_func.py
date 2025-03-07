#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5 * 10^4. For each test case, n, m, and k are integers where 2 <= n <= 10^5, 0 <= m <= min(10^5, n*(n-1)/2), and 1 <= k <= 2 * 10^5. Each of the m lines contains three integers a_i, b_i, and f_i where a_i != b_i, 1 <= a_i, b_i <= n, and 1 <= f_i <= 10^9. All pairs of friends (a_i, b_i) are distinct. The sum of n and m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2 * 10^5.
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
        
    #State: The output state consists of `t` lines, each containing the result of the computation for each test case, formatted as `int(p * pow(q, -1, M) % M)`.
#Overall this is what the function does:The function processes `t` test cases, each defined by `n` people, `m` friendships, and a threshold `k`. For each friendship, it considers the friendship factor `f_i`. It computes and outputs a result for each test case based on these inputs, formatted as an integer. The result is derived from a specific mathematical computation involving the sum of friendship factors, combinations of people, and the threshold value, reduced modulo \(10^9 + 7\).

