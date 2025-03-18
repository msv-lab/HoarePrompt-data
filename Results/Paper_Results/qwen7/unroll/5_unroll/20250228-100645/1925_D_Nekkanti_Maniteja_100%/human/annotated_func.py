#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 ⋅ 10^5. Additionally, a_i, b_i, and f_i are integers such that a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. All pairs (a_i, b_i) are distinct.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 ⋅ 10^5. Additionally, c is an integer calculated as the modular inverse of \( \frac{n(n-1)}{2} \) modulo \( 10^9 + 7 \), s is an integer initially set to 0, and a is an integer initially set to 0. After the loop executes all the iterations, s is updated based on the formula \( s = s + c \cdot i \cdot c \cdot m + c \cdot a \) for each iteration from 0 to k-1, and then printed as \( s \mod (10^9 + 7) \).
#Overall this is what the function does:The function processes multiple test cases, each defined by integers n, m, and k, along with additional integers a_i, b_i, and f_i. For each test case, it calculates a value s based on the number of edges (m), the modular inverse of half the number of possible edges (c), and a sum (a) of f_i values. The final value of s is computed using a specific formula and printed modulo \(10^9 + 7\).

