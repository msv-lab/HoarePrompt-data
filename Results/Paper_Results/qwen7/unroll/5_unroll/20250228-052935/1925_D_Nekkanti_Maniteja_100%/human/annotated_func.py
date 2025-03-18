#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5·10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2·10^5. Additionally, a_i, b_i, and f_i are integers such that a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. All pairs of friends are distinct, and the sum of n and m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2·10^5.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 5·10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2·10^5. Additionally, a is an integer, s is an integer calculated as \(s = \sum_{i=0}^{k-1} (c \cdot i \cdot c \cdot m + c \cdot a)\) where \(c = (n \cdot (n - 1) // 2)^{-1} \mod M\) and M is \(10^9 + 7\). The sum of n and m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2·10^5.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers n, m, and k, along with additional integers a, u, v, and f. It calculates a value s based on the formula \(s = \sum_{i=0}^{k-1} (c \cdot i \cdot c \cdot m + c \cdot a)\), where \(c = (n \cdot (n - 1) // 2)^{-1} \mod M\) and M is \(10^9 + 7\). After processing all test cases, it prints the final value of s modulo M for each test case.

