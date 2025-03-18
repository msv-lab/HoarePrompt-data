#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5 * 10^4. For each test case, n, m, and k are integers such that 2 <= n <= 10^5, 0 <= m <= min(10^5, n(n-1)/2), and 1 <= k <= 2 * 10^5. For each of the m lines in a test case, a_i, b_i, and f_i are integers such that a_i != b_i, 1 <= a_i, b_i <= n, and 1 <= f_i <= 10^9. All pairs (a_i, b_i) are distinct. The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5. The sum of k over all test cases does not exceed 2 * 10^5.
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
        
    #State: the final value of `s` modulo \(M\) after processing the last test case.
#Overall this is what the function does:The function processes multiple test cases, each involving a graph with `n` nodes and `m` edges, and an additional parameter `k`. For each test case, it calculates a specific value based on the edges' feature values and outputs the result modulo \(10^9 + 7\).

