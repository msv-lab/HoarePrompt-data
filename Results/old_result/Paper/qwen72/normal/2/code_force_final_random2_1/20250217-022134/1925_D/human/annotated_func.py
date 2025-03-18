#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4; for each test case, n, m, and k are integers where 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 · 10^5; for each of the m pairs, a_i, b_i, and f_i are integers where a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9; the sum of n and m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is 0, `i` is `t`, `n` is the last input integer for `n`, `m` is the last input integer for `m`, `k` is the last input integer for `k`, `sum_f` is the sum of all `f` values input during the loop, `j` is `m - 1`, `a` is the last input integer for `a`, `b` is the last input integer for `b`, `f` is the last input integer for `f`, `cn2` is `n * (n - 1) // 2`, `p` is `(2 * k * cn2 * sum_f + m * k * (k - 1)) // gcd`, `q` is `2 * (n * (n - 1) // 2) // gcd`, `gcd` is the greatest common divisor of `p` and `q`.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by integers `n`, `m`, and `k`, and a list of `m` pairs `(a_i, b_i, f_i)`. For each test case, it calculates a value based on these inputs and prints the result modulo \(10^9 + 7\). The function reads the number of test cases `t` and then iterates through each test case, reading the values of `n`, `m`, and `k`, followed by the pairs `(a_i, b_i, f_i)`. It computes a result using these values and prints the result for each test case. After processing all test cases, the function terminates.

