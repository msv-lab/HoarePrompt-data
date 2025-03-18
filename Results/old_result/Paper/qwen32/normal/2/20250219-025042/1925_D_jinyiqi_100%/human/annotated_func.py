#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, m is an integer such that 0 ≤ m ≤ min(10^5, n(n-1)/2), and k is an integer such that 1 ≤ k ≤ 2 · 10^5. Each of the m lines contains three integers a_i, b_i, and f_i where a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. All pairs (a_i, b_i) are distinct. The sum of n across all test cases does not exceed 10^5, and the sum of m across all test cases does not exceed 10^5. The sum of k across all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop has executed `t` times, with `i` ranging from 0 to `t-1`. For each iteration `i`, `n`, `m`, and `k` are read as inputs. `sum_f` is the cumulative sum of `f` values for the `m` edges provided in that iteration. `cn2` is calculated as `n * (n - 1) // 2`. `p` is computed as `(2 * k * cn2 * sum_f + m * k * (k - 1)) // gcd`, and `q` is computed as `2 * cn2 // gcd`, where `gcd` is the greatest common divisor of `p` and `q`. The final output for each iteration is `int(p * pow(q, -1, M) % M)`, which is printed.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `m`, and `k`, along with `m` edges specified by pairs of nodes and a feature value. For each test case, it calculates and prints a specific integer result based on these inputs.

