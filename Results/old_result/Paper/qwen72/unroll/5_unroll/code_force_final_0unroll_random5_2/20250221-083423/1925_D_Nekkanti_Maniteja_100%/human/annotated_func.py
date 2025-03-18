#State of the program right berfore the function call: The function `func` is expected to take input parameters that are not provided in the function definition. Based on the problem description, the function should take three parameters: n (number of children), m (number of pairs of friends), and k (number of excursions). Additionally, it should take a list of m tuples, each containing three integers (a_i, b_i, f_i) representing the indices of the pair of children who are friends and their initial friendship value. The constraints are: 1 ≤ t ≤ 5 · 10^4 (number of test cases), 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), 1 ≤ k ≤ 2 · 10^5, 1 ≤ a_i, b_i ≤ n, a_i ≠ b_i, and 1 ≤ f_i ≤ 10^9. The sum of n and m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2 · 10^5.
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
        
    #State: After the loop executes all iterations, the variable `s` will contain the final computed value of the sum modulo \(10^9 + 7\). The variables `n`, `m`, `k`, `M`, and `c` will retain their initial values, and the variable `a` will be the sum of all initial friendship values `f_i` for the pairs of friends.
#Overall this is what the function does:The function `func` reads input from the user, processes multiple test cases, and for each test case, it calculates a specific sum based on the number of children (`n`), the number of pairs of friends (`m`), and the number of excursions (`k`). It then prints the result of this sum modulo \(10^9 + 7\). The function does not return any value; instead, it prints the result for each test case. After the function concludes, the variables `n`, `m`, `k`, `M`, and `c` retain their values, and the variable `a` holds the sum of all initial friendship values `f_i` for the pairs of friends.

