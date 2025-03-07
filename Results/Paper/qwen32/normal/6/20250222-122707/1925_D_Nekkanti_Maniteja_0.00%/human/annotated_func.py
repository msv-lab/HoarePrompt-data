#State of the program right berfore the function call: Each test case consists of integers n, m, and k where 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2⋅10^5. For each of the m pairs of friends, the input specifies two distinct children a_i and b_i (1 ≤ a_i, b_i ≤ n) and their initial friendship value f_i (1 ≤ f_i ≤ 10^9). The sum of n and m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2⋅10^5.
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
        
    #State: s = (c^2 * m * (k-1) * k // 2 + c * a * k) % M
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `m`, and `k`, and `m` friendship pairs with associated friendship values. For each test case, it computes and prints a result based on these inputs, specifically a value derived from the sum of friendship values and the threshold `k`, modulo \(10^9 + 7\).

