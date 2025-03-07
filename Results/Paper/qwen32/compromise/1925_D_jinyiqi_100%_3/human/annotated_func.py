#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, m is an integer such that 0 ≤ m ≤ min(10^5, n(n-1)/2), and k is an integer such that 1 ≤ k ≤ 2 · 10^5. Each of the next m lines contains three integers a_i, b_i, and f_i, where a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. All pairs (a_i, b_i) are distinct. The sum of n across all test cases does not exceed 10^5, and the sum of m across all test cases does not exceed 10^5. The sum of k across all test cases does not exceed 2 · 10^5.
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
        
    #State: `i` is `t`, `n`, `m`, `k`, `sum_f`, `cn2`, `p`, `q`, `gcd` are from the last iteration, and the output is the final result printed for the last test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `m`, and `k`, along with `m` edges connecting `n` nodes and associated values. For each test case, it computes and prints a specific result based on these inputs.

