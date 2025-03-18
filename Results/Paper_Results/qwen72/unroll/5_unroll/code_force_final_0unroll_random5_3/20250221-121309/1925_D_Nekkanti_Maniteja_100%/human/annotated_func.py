#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5 * 10^4. For each test case, n, m, and k are integers where 2 <= n <= 10^5, 0 <= m <= min(10^5, n*(n-1)/2), and 1 <= k <= 2 * 10^5. Each of the m lines contains three integers a_i, b_i, and f_i, where 1 <= a_i, b_i <= n, a_i != b_i, and 1 <= f_i <= 10^9. The sum of n over all test cases does not exceed 10^5, the sum of m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2 * 10^5.
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
        
    #State: The value of `s` is calculated for each test case and printed modulo \(10^9 + 7\). The variables `t`, `n`, `m`, and `k` are unchanged, and the variables `M`, `c`, and `a` are reset for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by integers `n`, `m`, and `k`, and a list of `m` lines containing integers `a_i`, `b_i`, and `f_i`. For each test case, it calculates a value `s` based on the inputs and prints `s` modulo \(10^9 + 7\). The function does not return any value; it only prints the result for each test case. The variables `n`, `m`, and `k` are unchanged after each test case, and the internal variables `M`, `c`, and `a` are reset for each new test case.

