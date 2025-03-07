#State of the program right berfore the function call: The function should accept two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists, where each inner list contains an integer n (1 ≤ n ≤ 3 · 10^5) followed by n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n). The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The function will print the number of ways to choose 3 distinct indices from the list `w` such that the values at these indices are the same. If `n` is less than 3, it will print 0. The variables `t` and `buffer` remain unchanged.
#Overall this is what the function does:The function reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers `w`. If `n` is less than 3, it prints 0. Otherwise, it calculates and prints the number of ways to choose 3 distinct indices from the list `w` such that the values at these indices are the same. The function does not return any value; it only prints the results. The variables `t` and `buffer` remain unchanged throughout the function's execution.

