#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5·10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2·10^5. Each of the next m lines contains three integers a_i, b_i, and f_i such that a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. All pairs of friends are distinct, and the sum of n and m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2·10^5.
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
        
    #State: Output State: The output state will consist of a series of integers, each representing the result of the expression `(p * pow(q, -1, M) % M)` for each iteration of the loop. These results are calculated based on the values of `n`, `m`, `k`, and `sum_f` for each test case provided by the input. Each test case will produce one output value, and the final output state will be a list of these values.
#Overall this is what the function does:The function processes multiple test cases, where each test case includes integers t, n, m, and k, along with m lines of additional data. For each test case, it calculates and prints a value based on the given constraints and input data. Specifically, it computes an expression involving `p`, `q`, and `M`, and outputs the result modulo `M`. The final output consists of a series of integers, one for each test case.

