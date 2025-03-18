#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4. For each test case, n, m, and k are integers with 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 · 10^5. Each of the m lines contains three integers a_i, b_i, and f_i, where 1 ≤ a_i, b_i ≤ n, a_i ≠ b_i, and 1 ≤ f_i ≤ 10^9. The sum of n and the sum of m over all test cases do not exceed 10^5, and the sum of k over all test cases does not exceed 2 · 10^5.
def func():
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        M = 10 ** 9 + 7
        
        c = pow(n * (n - 1) // 1, -1, M)
        
        s = 0
        
        a = 0
        
        for i in range(m):
            u, v, f = map(int, input().split())
            a += f
        
        for i in range(k):
            s = s + c * i * c * m + c * a
        
        print(s % M)
        
    #State: For each test case, the final value of `s` is calculated and printed as `s % M`, where `M` is \(10^9 + 7\). The value of `s` is the sum of `c * i * c * m + c * a` for `i` from 0 to `k-1`. The variables `n`, `m`, `k`, `c`, and `a` are reset for each test case, and the loop iterates `t` times.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads integers `n`, `m`, and `k`, and a list of `m` edges, each defined by three integers `a_i`, `b_i`, and `f_i`. It calculates a value `s` based on these inputs and prints `s % M`, where `M` is \(10^9 + 7\). The value of `s` is the sum of `c * i * c * m + c * a` for `i` from 0 to `k-1`, with `c` being the modular inverse of \( \frac{n(n-1)}{2} \) modulo \(10^9 + 7\). The function does not return any value; it only prints the result for each test case.

