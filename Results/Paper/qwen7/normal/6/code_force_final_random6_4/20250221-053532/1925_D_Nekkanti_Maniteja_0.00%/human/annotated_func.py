#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5·10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2·10^5. Additionally, a_i, b_i, and f_i are integers such that a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. All pairs of friends are distinct, and the sum of n and m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2·10^5.
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
        
    #State: i is less than m, k is greater than 0, s is the sum of c * i * c * m + c * a for all i from 0 to m-1, a is the sum of all f values provided as inputs during the loop executions.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( n \), \( m \), and \( k \). For each test case, it reads pairs of integers \( u \) and \( v \) along with an integer \( f \), sums up all \( f \) values, and calculates a value \( s \) based on these inputs and a constant \( c \). Finally, it prints \( s \mod M \) for each test case, where \( M = 10^9 + 7 \).

