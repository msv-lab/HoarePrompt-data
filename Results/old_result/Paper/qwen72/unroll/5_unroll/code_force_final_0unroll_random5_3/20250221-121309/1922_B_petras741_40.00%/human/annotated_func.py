#State of the program right berfore the function call: The function `func` is expected to be called with no arguments, but it should internally handle multiple test cases. Each test case consists of an integer n (1 ≤ n ≤ 3 · 10^5) followed by a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n). The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The list `buffer` remains empty, and the loop has processed all `t` test cases, printing the result for each test case. For each test case, if `n` is less than 3, the output is 0. If `n` is 3 or greater, the output is the number of ways to choose 3 elements from the list `w` such that all three elements are the same or all three elements are distinct.
#Overall this is what the function does:The function `func` accepts no parameters and processes multiple test cases. Each test case involves an integer `n` and a list of `n` integers. For each test case, if `n` is less than 3, the function prints 0. If `n` is 3 or greater, the function prints the number of ways to choose 3 elements from the list such that all three elements are the same or all three elements are distinct. The list `buffer` remains empty throughout the function's execution.

