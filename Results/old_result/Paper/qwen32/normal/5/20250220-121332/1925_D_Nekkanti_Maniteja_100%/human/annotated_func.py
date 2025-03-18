#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5 * 10^4. For each test case, n is an integer such that 2 <= n <= 10^5, m is an integer such that 0 <= m <= min(10^5, n(n-1)/2), and k is an integer such that 1 <= k <= 2 * 10^5. For each of the m lines in a test case, a_i and b_i are integers such that a_i != b_i, 1 <= a_i, b_i <= n, and f_i is an integer such that 1 <= f_i <= 10^9. The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2 * 10^5. All pairs (a_i, b_i) are distinct within a test case.
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
        
    #State: t remains the same as the initial value, n remains the same as the value for the last test case, m remains the same as the value for the last test case, k remains the same as the value for the last test case, M remains 1000000007, c remains the modular multiplicative inverse of n * (n - 1) // 2 modulo 1000000007 for the last test case, a is the sum of all f values for the last test case, s is the final value computed for the last test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `m`, and `k`, along with `m` pairs of integers `(a_i, b_i)` and associated values `f_i`. For each test case, it computes and prints a specific value `s` modulo \(10^9 + 7\), which is derived from the inputs provided.

