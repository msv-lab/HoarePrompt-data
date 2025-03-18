#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5 * 10^4. For each test case, n is an integer such that 2 <= n <= 10^5, m is an integer such that 0 <= m <= min(10^5, n(n-1)/2), and k is an integer such that 1 <= k <= 2 * 10^5. For each of the m lines in a test case, a_i, b_i, and f_i are integers where a_i != b_i, 1 <= a_i, b_i <= n, and 1 <= f_i <= 10^9. It is guaranteed that all pairs (a_i, b_i) are distinct. The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2 * 10^5.
def func():
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        M = 10 ** 9 + 7
        
        c = pow(n * (n - 1) // 2, -1, M)
        
        s = 0
        
        a = 0
        
        for i in range(m):
            u, v, f = map(int, input().split())
            a += f
        
        for i in range(k):
            s = s + c * i * c * m + c * a
        
        print(s % M)
        
    #State: For each test case, the output is \((c^2 \cdot m \cdot \frac{(k-1)k}{2} + c \cdot a \cdot k) \% M\).
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `m`, and `k`, and a list of `m` pairs of distinct nodes with associated values. For each test case, it calculates and prints a specific value based on these inputs, using modular arithmetic with a modulus of \(10^9 + 7\). The final output for each test case is determined by a formula involving the sum of the associated values and a series calculation.

