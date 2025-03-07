#State of the program right berfore the function call: Each test case contains integers n (2 ≤ n ≤ 10^5), m (0 ≤ m ≤ min(10^5, n(n-1)/2)), and k (1 ≤ k ≤ 2·10^5) representing the number of children, pairs of friends, and excursions respectively. The next m lines contain three integers each: a_i, b_i (1 ≤ a_i, b_i ≤ n, a_i ≠ b_i) representing a pair of friends and f_i (1 ≤ f_i ≤ 10^9) representing their initial friendship value. All pairs of friends are distinct. The sum of n and m over all test cases does not exceed 10^5 and the sum of k over all test cases does not exceed 2·10^5.
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
        
    #State: the final value of `s % M` after the loop executes all iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of children, pairs of friends with their initial friendship values, and a number of excursions. It calculates and prints a result based on these inputs, specifically the value of `s % M` after performing certain computations involving the number of children, pairs of friends, their friendship values, and the number of excursions.

