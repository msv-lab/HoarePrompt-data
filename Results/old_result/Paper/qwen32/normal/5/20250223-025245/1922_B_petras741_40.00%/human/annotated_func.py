#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, the first line contains an integer n (1 ≤ n ≤ 3 · 10^5) representing the number of sticks. The second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n) where each a_i represents the exponent of 2 for the length of the i-th stick. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `t` is 0, `i` is `t - 1` (the last iteration), `buffer` is an empty list.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of sticks and their respective lengths represented as exponents of 2. For each test case, it calculates and prints the number of ways to choose three sticks from the given set of sticks.

