#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5⋅10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2⋅10^5. Each of the next m lines contains three integers a_i, b_i, and f_i such that a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. It is guaranteed that all pairs of friends are distinct, and the sum of n and the sum of m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 5⋅10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2⋅10^5. The value of `s` is calculated as \( s = \sum_{i=0}^{k-1} \left(c \cdot i \cdot c \cdot m + c \cdot a\right) \mod M \), where \( c = \left(\frac{n \cdot (n - 1)}{2}\right)^{-1} \mod M \), and `a` is the sum of `f_i` values from the edges. The final output is the value of `s` modulo \( M \).
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads integers n, m, and k, followed by m lines of integers a_i, b_i, and f_i. It calculates the value of `s` using the formula \( s = \sum_{i=0}^{k-1} \left(c \cdot i \cdot c \cdot m + c \cdot a\right) \mod M \), where \( c = \left(\frac{n \cdot (n - 1)}{2}\right)^{-1} \mod M \) and `a` is the sum of `f_i` values. Finally, it prints the value of `s` modulo \( M \) for each test case.

