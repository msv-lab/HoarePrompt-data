#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case contains three integers n, m, and k, where 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 * 10^5. Additionally, m lines follow, each containing three integers a_i, b_i, and f_i, where 1 ≤ a_i, b_i ≤ n, a_i ≠ b_i, and 1 ≤ f_i ≤ 10^9, representing the indices of the pair of children who are friends and their initial friendship value. The sum of n and the sum of m over all test cases do not exceed 10^5, and the sum of k over all test cases does not exceed 2 * 10^5.
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
        
    #State: `i` is `k-1`, `s` is `s + c * (0 + 1 + 2 + ... + (k-1)) * c * m + c * a * k`.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by three integers `n`, `m`, and `k`. For each test case, it reads `m` lines of friendship data, where each line contains three integers representing a pair of children who are friends and their initial friendship value. The function calculates a value `s` based on the friendship values and the number of children, and prints the result modulo \(10^9 + 7\). The final state of the program after the function concludes is that the value `s` has been computed and printed for each test case, and the input has been fully processed.

