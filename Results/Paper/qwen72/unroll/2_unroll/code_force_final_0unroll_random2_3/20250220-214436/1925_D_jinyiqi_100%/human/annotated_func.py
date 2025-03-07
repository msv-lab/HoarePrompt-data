#State of the program right berfore the function call: The function should take three parameters: n (the number of children), m (the number of pairs of friends), and k (the number of excursions). Each of these parameters is an integer, with constraints 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 × 10^5. Additionally, the function should take a list of m tuples, each containing three integers a_i, b_i, and f_i, representing the indices of the pair of children who are friends and their initial friendship value, with constraints 1 ≤ a_i, b_i ≤ n, a_i ≠ b_i, and 1 ≤ f_i ≤ 10^9. The sum of n and m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2 × 10^5.
def func():
    t = int(input())
    M = 10 ** 9 + 7
    for i in range(t):
        n, m, k = map(int, input().split())
        
        sum_f = 0
        
        for j in range(m):
            a, b, f = map(int, input().split())
            sum_f += f
        
        cn2 = n * (n - 1) // 2
        
        p = 2 * k * cn2 * sum_f + m * k * (k - 1)
        
        q = 2 * cn2 ** 2
        
        gcd = math.gcd(p, q)
        
        p = p // gcd
        
        q = q // gcd
        
        print(int(p * pow(q, -1, M) % M))
        
    #State: The loop executes `t` times, and for each iteration, it reads `n`, `m`, and `k` from the input, then reads `m` tuples of integers `a`, `b`, and `f` from the input. After processing these inputs, it calculates and prints the result of the formula `(2 * k * n * (n - 1) // 2 * sum_f + m * k * (k - 1)) // (2 * (n * (n - 1) // 2)
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `n`, `m`, and `k`, representing the number of children, the number of pairs of friends, and the number of excursions, respectively. It also reads `m` tuples, each containing three integers `a_i`, `b_i`, and `f_i`, representing the indices of a pair of friends and their initial friendship value. The function calculates a value based on these inputs and prints the result of a specific formula for each test case. The final state of the program after the function concludes is that `t` results have been printed, each corresponding to a test case.

