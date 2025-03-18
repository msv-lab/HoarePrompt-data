#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5⋅10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2⋅10^5. Each of the next m lines contains three integers a_i, b_i, and f_i such that a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. It is guaranteed that all pairs of friends are distinct, and the sum of n and m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: All variables outside the loop remain unchanged, including `t`, `M`, `i`, `n`, `m`, `k`, `a`, `b`, `f`, `sum_f`, `cn2`, `p`, `q`, and `gcd`. After the loop completes all its iterations, `i` will be equal to `t-1`, and the final values of `p` and `q` will be simplified by their greatest common divisor (`gcd`). The expression `int(p * pow(q, -1, M) % M)` will be printed for each iteration, resulting in `t` outputs, each representing the simplified fraction \( \frac{p}{q} \) modulo \( M \).
    #
    #This means that after all iterations, the loop will have processed all inputs specified by `t`, and for each input set, it will compute and print the result of the expression \( \frac{p}{q} \mod M \), where `p` and `q` are the final values after all iterations, simplified by their greatest common divisor.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers t, n, m, and k, along with additional input data. For each test case, it calculates a value based on the given inputs and computes a simplified fraction \( \frac{p}{q} \) modulo \( M \). The function then prints this result for each test case. The final output consists of t results, one for each test case.

