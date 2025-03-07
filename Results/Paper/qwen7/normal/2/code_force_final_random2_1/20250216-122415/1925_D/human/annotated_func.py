#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5⋅10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2⋅10^5. Each of the next m lines contains three integers a_i, b_i, and f_i such that a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. It is guaranteed that all pairs of friends are distinct, and the sum of n and the sum of m over all test cases do not exceed 10^5, and the sum of k over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The loop has executed all its iterations, so `i` will be equal to `t-1`. For each iteration `i`, the variables `m`, `a`, `b`, `f`, `sum_f`, `p`, `q`, `gcd`, `cn2`, and `n` will hold the values from the last iteration of the inner loop. Specifically, `sum_f` will be the total sum of all `f` values entered across all iterations, `p` and `q` will be reduced by their greatest common divisor, and `cn2` will be calculated as `n * (n - 1) // 2` based on the last `n` value from any iteration. The final output will be the result of the expression `int(p * pow(q, -1, M) % M)` computed with the values from the last iteration.
    #
    #In summary, after all iterations, `i` will be `t-1`, and all other variables will reflect the state of the last iteration of the inner loop.
#Overall this is what the function does:The function processes multiple test cases, each containing integers t, n, m, and k, along with m lines of additional data. For each test case, it calculates a mathematical expression involving the sum of f values, the number of pairs of friends, and the given integers n and k. After processing all test cases, it outputs the result of the expression for the last test case, ensuring all intermediate calculations are reduced modulo \(10^9 + 7\).

