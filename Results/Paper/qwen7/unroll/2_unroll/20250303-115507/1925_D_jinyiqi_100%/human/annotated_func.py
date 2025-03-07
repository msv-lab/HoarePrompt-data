#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5·10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2·10^5. Each of the next m lines contains three integers a_i, b_i, and f_i such that a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. It is guaranteed that all pairs of friends are distinct, and the sum of n and m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2·10^5.
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
        
    #State: Output State: The output state will consist of a series of integers, each representing the result of the expression `(p * pow(q, -1, M) % M)` for each iteration of the outer loop. Each result is calculated based on the values of `n`, `m`, and `k` for that specific iteration, along with the cumulative sum of `f` values from the inner loop, modulo `M` (1000000007).
#Overall this is what the function does:The function processes a series of test cases, each consisting of integers \( t \), \( n \), \( m \), and \( k \), along with additional pairs of integers \( a_i \), \( b_i \), and \( f_i \). For each test case, it calculates a value based on the sum of \( f_i \) values, the number of people \( n \), and the number of friendships \( m \), then computes and prints the result of a mathematical expression involving these values and a modulus operation. The final output consists of one integer per test case, representing the computed result for each case.

