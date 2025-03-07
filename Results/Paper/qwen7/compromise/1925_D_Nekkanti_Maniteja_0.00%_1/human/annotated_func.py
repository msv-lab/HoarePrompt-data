#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 ⋅ 10^5. Additionally, a_i, b_i, and f_i are integers such that a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. All pairs of friends are distinct, and the sum of n and m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: `i` is `100000 + 3 * m`, `k` is `3 * m`, `s` is `3 * m * c * i * c * m + 3 * m * c * a`.
    #
    #In natural language: After the loop executes all its iterations, the variable `i` will be `100000 + 3 * m` because the loop increments `i` by `m` for each iteration, and it runs `3 * m` times. The variable `k` will be `3 * m` since it represents the total number of iterations the loop executed. The variable `s` will be the cumulative sum of the expression `c * i * c * m + c * a` for each iteration, where `i` ranges from `100000 + m` to `100000 + 3 * m`. The variable `a` will hold the cumulative sum of all `f` values provided as input over the course of the loop's execution, and it is updated in each iteration of the inner loop.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( t \), \( n \), \( m \), and \( k \). For each test case, it calculates a value \( s \) based on given inputs and a modulus \( M \). Specifically, it computes \( s \) using the formula \( s = \sum_{i=100000+m}^{100000+3m} (c \cdot i \cdot c \cdot m + c \cdot a) \), where \( c \) is the modular inverse of \( \frac{n(n-1)}{2} \) modulo \( M \), and \( a \) is the sum of all \( f \) values provided for the test case. The function prints the result of \( s \mod M \) for each test case.

