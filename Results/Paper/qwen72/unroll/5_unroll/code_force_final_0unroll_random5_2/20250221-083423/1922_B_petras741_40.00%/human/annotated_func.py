#State of the program right berfore the function call: The function is expected to handle multiple test cases. Each test case includes an integer n (1 ≤ n ≤ 3 · 10^5) representing the number of sticks, and a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n) where each a_i represents the exponent of the length of the i-th stick (2^{a_i}). The sum of n over all test cases does not exceed 3 · 10^5.
def func():
    t = int(input())
    buffer = []
    for i in range(t):
        n = int(input())
        
        w = [int(k) for k in input().split()]
        
        if n >= 3:
            q = {}
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
                    if j > 1000:
                        break
                print(res)
        else:
            print(0)
        
    #State: The `buffer` remains an empty list, and the loop processes each test case as described, printing the number of ways to choose three sticks that can form a triangle for each test case. The variable `t` is decremented to 0 as the loop iterates `t` times.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. Each test case consists of an integer `n` and a list of `n` integers representing the exponents of the lengths of sticks (2^a_i). The function calculates and prints the number of ways to choose three sticks that can form a triangle for each test case. If `n` is less than 3, the function prints 0 for that test case. The `buffer` list remains empty throughout the execution, and the function does not return any value.

