#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 ⋅ 10^5. Additionally, for each of the m lines describing pairs of friends, a_i, b_i, and f_i are integers such that a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9.
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
        
    #State: Output State: The loop has executed all its iterations, meaning `i` ranges from `0` to `t-1`. For each iteration, `n`, `m`, and `k` are integers entered by the user, and `sum_f` is the sum of all `f` values entered over the range of `m`. After processing all iterations, `cn2` remains `n * (n - 1) // 2`, `p` is `2 * k * cn2 * sum_f + m * k * (k - 1)` divided by the greatest common divisor of `p` and `q`, and `q` is `2 * cn2 // gcd`. The final output is the result of `int(p * pow(q, -1, M) % M)`.
    #
    #In simpler terms, after all iterations of the loop, the output state will reflect the cumulative effect of all inputs processed within the loop. The variables `cn2`, `p`, and `q` will be updated based on the total sums and counts from all iterations, and the final printed value will be the result of the modular multiplicative inverse calculation applied to the simplified fraction `p/q` modulo `M`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of integers \( t \), \( n \), \( m \), and \( k \). For each test case, it further processes \( m \) pairs of integers \( a_i \) and \( b_i \) along with an integer \( f_i \). It calculates a specific mathematical expression involving these inputs, simplifies the result using the greatest common divisor, and finally outputs the modular multiplicative inverse of the simplified fraction modulo \( M \).

