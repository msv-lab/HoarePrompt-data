#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5 * 10^4. For each test case, n is an integer such that 2 <= n <= 10^5, m is an integer such that 0 <= m <= min(10^5, n(n-1)/2), and k is an integer such that 1 <= k <= 2 * 10^5. Each of the m lines contains three integers a_i, b_i, and f_i where a_i != b_i, 1 <= a_i, b_i <= n, and 1 <= f_i <= 10^9. It is guaranteed that all pairs (a_i, b_i) are distinct. The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2 * 10^5.
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
        
    #State: the final value of s for each test case, modulo \(10^9 + 7\).
#Overall this is what the function does:The function processes multiple test cases, each defined by the number of nodes `n`, the number of edges `m`, and an integer `k`. For each test case, it also processes `m` lines of input, each representing an edge between two nodes with a feature value. The function calculates and prints a specific value `s` for each test case, which is derived from the provided inputs and is taken modulo \(10^9 + 7\).

