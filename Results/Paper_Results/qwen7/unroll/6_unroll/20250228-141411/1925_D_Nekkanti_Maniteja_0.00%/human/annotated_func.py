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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 ⋅ 10^5. Additionally, c is the modular inverse of n * (n - 1) // 2 under modulo 10^9 + 7, a is the sum of f_i for all edges, s is calculated as (c * i * c * m + c * a) summed up to k, and the final result is taken modulo 10^9 + 7.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( n \), \( m \), and \( k \). For each test case, it calculates a value \( s \) based on the number of edges \( m \), the sum of edge weights \( a \), and a modular inverse \( c \). The final value of \( s \) is computed as the sum of \( c \cdot i \cdot c \cdot m + c \cdot a \) for \( i \) ranging from 0 to \( k-1 \), and then taken modulo \( 10^9 + 7 \). The function outputs the calculated value \( s \) for each test case.

