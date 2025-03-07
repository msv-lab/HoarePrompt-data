#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4. For each test case, n, m, and k are integers where 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 · 10^5. Each of the m lines contains three integers a_i, b_i, and f_i, where 1 ≤ a_i, b_i ≤ n, a_i ≠ b_i, and 1 ≤ f_i ≤ 10^9. The sum of n and the sum of m over all test cases do not exceed 10^5, and the sum of k over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` must be greater than or equal to the number of iterations, `i` is `t - 1`, `n` is an input integer, `m` is an input integer, `k` is an input integer, `sum_f` is the sum of all `f` values input during the loop, `j` is `m - 1`, `a`, `b`, and `f` are the last set of input integers, `cn2` is `n * (n - 1) // 2`, `p` is `(2 * k * cn2 * sum_f + m * k * (k - 1)) // gcd`, `q` is `2 * cn2
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by the number of nodes (`n`), the number of edges (`m`), and the number of queries (`k`). For each test case, it reads a list of edges, where each edge is represented by two nodes (`a_i`, `b_i`) and a value (`f_i`). It calculates a result based on these inputs and prints the result modulo \(10^9 + 7\). The final state of the program includes the printed results for each test case, and the variables `t`, `i`, `n`, `m`, `k`, `sum_f`, `j`, `a`, `b`, `f`, `cn2`, `p`, `q`, and `gcd` are updated accordingly for each iteration.

