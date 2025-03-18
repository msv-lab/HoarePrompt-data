#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of n, an integer such that 1 ≤ n ≤ 3 · 10^5, and a list of n integers a_1, a_2, ..., a_n, where 0 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5.
def func():
    t = int(input())
    buffer = []
    for i in range(t):
        n = int(input())
        
        w = [int(k) for k in input().split()]
        
        if n >= 3:
            q = [(0) for j in range(n + 1)]
            for j in range(n):
                q[w[j]] += 1
            eta = []
            for j in range(n + 1):
                if q[j] > 0:
                    eta.append(j)
            eta_ln = len(eta)
            rho = q[eta[0]]
            if eta_ln == 1:
                print(n * (n - 1) * (n - 2) // 6)
            else:
                res = q[eta[0]] * (q[eta[0]] - 1) * (q[eta[0]] - 2) // 6
                for j in range(1, eta_ln):
                    res += q[eta[j]] * (q[eta[j]] - 1) * (q[eta[j]] - 2) // 6
                    res += q[eta[j]] * (q[eta[j]] - 1) // 2 * rho
                    rho += q[eta[j]]
                print(res)
        else:
            print(0)
        
    #State: The variable `t` is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. The variable `buffer` remains an empty list. For each test case, the loop has processed the input values `n` and the list of integers `a_1, a_2, ..., a_n`, and has printed the number of ways to choose 3 distinct indices i, j, k such that a_i = a_j = a_k. If n < 3, the loop prints 0 for that test case.
#Overall this is what the function does:The function `func` processes a series of test cases. It accepts an integer `t` (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, it reads an integer `n` (1 ≤ n ≤ 3 · 10^5) and a list of `n` integers `a_1, a_2, ..., a_n` (0 ≤ a_i ≤ n). The function calculates and prints the number of ways to choose 3 distinct indices i, j, k such that a_i = a_j = a_k. If `n` is less than 3, it prints 0 for that test case. The function does not return any value; it only prints the results. After processing all test cases, the function concludes, and the variable `buffer` remains an empty list.

