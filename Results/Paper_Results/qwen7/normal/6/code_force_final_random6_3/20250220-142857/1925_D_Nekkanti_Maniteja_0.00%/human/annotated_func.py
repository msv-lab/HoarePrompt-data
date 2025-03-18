#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5·10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2·10^5. Each of the next m lines contains three integers a_i, b_i, and f_i such that a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. All pairs of friends are distinct, and the sum of n and the sum of m over all test cases do not exceed 10^5, and the sum of k over all test cases does not exceed 2·10^5.
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
        
    #State: Output State: The output state after the loop executes all the iterations is \( s \) equals \( c \times \frac{k \times (k - 1)}{2} \times c \times m + k \times c \times a \). Here, \( c \) is the modular inverse of \( n \times (n - 1) \) modulo \( 10^9 + 7 \), \( a \) is the total sum of all \( f_i \) values provided as input over the course of the loop's execution, \( k \) is the number of iterations the outer loop runs, and \( m \) is the number of edges in the graph.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads integers n, m, and k. It then reads m lines of input, each containing three integers a_i, b_i, and f_i. The function calculates a value s based on the modular inverse of n*(n-1) modulo \(10^9 + 7\), the total sum of all f_i values, and the number of test cases and edges. Finally, it prints the result of s modulo \(10^9 + 7\) for each test case.

