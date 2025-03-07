#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5 * 10^4. For each test case, n is an integer such that 2 <= n <= 10^5, m is an integer such that 0 <= m <= min(10^5, n*(n-1)/2), and k is an integer such that 1 <= k <= 2 * 10^5. Each of the m lines contains three integers a_i, b_i, and f_i where a_i != b_i, 1 <= a_i, b_i <= n, and 1 <= f_i <= 10^9. The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5. The sum of k over all test cases does not exceed 2 * 10^5. All pairs (a_i, b_i) are distinct.
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
        
    #State: t is an integer such that 1 <= t <= 5 * 10^4; for each of the t test cases, n, m, and k are integers read from the input; M is 1000000007; c is the modular multiplicative inverse of n * (n - 1) // 2 modulo M; a is the sum of all f values read from the input for each test case; s is the final sum calculated as c * a * k + c^2 * m * (k * (k - 1)) // 2, taken modulo M; the loop has executed t times, processing each test case as described.
#Overall this is what the function does:The function processes `t` test cases, each defined by integers `n`, `m`, and `k`, and `m` lines of edge values `a_i`, `b_i`, and `f_i`. For each test case, it calculates and prints a specific sum `s` modulo `10^9 + 7`, which is derived from the input values and the defined operations.

