#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 5 · 10^4; for each test case, n, m, and k are integers where 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 · 10^5; a_i, b_i, and f_i are integers where a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9; all pairs (a_i, b_i) are distinct; the sum of n and the sum of m over all test cases do not exceed 10^5, and the sum of k over all test cases does not exceed 2 · 10^5.
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
        
    #State: After the loop has executed all `t` iterations, `i` is `t-1`, `n` and `m` are the input integers for the last test case, `k` is the input integer for the last test case, `sum_f` is the sum of all `f` values read from the input over `m` iterations for the last test case, `j` is `m-1`, `a`, `b`, and `f` are the input integers read from the input during the last iteration of the last test case, `cn2` is `n * (n - 1) // 2` for the last test case, `p` is `(2 * k * cn2 * sum_f + m * k * (k - 1)) // gcd` for the last test case, `q` is `(2 * (n * (n - 1) // 2)) // gcd` for the last test case, `gcd` is the greatest common divisor of `p` and `q` for the last test case.
#Overall this is what the function does:The function reads multiple test cases, each consisting of integers `n`, `m`, and `k`, followed by `m` lines of integers `a_i`, `b_i`, and `f_i`. For each test case, it calculates a value based on the inputs and prints the result modulo \(10^9 + 7\). Specifically, it computes a fraction \( \frac{p}{q} \) where \( p = 2 \cdot k \cdot \binom{n}{2} \cdot \sum f_i + m \cdot k \cdot (k - 1) \) and \( q = 2 \cdot \binom{n}{2}^2 \), simplifies the fraction by dividing both numerator and denominator by their greatest common divisor, and then prints the modular inverse of the simplified fraction. After processing all test cases, the function terminates.

