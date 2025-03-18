#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5·10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2·10^5. Each of the next m lines contains three integers a_i, b_i, and f_i such that a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. It is guaranteed that all pairs of friends are distinct, and the sum of n and the sum of m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2·10^5.
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
        
    #State: After the loop executes all iterations, `i` is `k-1`, `k` must be greater than 0, `m` is the value it was initialized to, `a` is the sum of all integers `f` obtained from the input split operation over all iterations, and `s` is `k * c * (k-1) * c * m + k * c * a`.
#Overall this is what the function does:The function processes multiple test cases, where each test case involves integers n, m, and k, and a list of m tuples (a_i, b_i, f_i). It calculates and prints the value of `s`, which is computed using the formula `k * c * (k-1) * c * m + k * c * a`, where `c` is the modular inverse of `n * (n - 1) // 2` modulo `M`, and `a` is the sum of all `f_i` values from the input. The result is printed modulo `M`.

