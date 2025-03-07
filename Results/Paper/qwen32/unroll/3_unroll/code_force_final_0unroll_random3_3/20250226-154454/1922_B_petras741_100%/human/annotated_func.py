#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, the first line contains an integer n (1 ≤ n ≤ 3 · 10^5) representing the number of sticks, and the second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n) representing the exponents for the lengths of the sticks, where the length of the i-th stick is 2^{a_i}. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `t` is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4; `buffer` is an empty list.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a number of sticks and their corresponding exponents. It calculates and prints the number of ways to choose three sticks such that their lengths are the same, considering the lengths as powers of 2 based on the exponents. If there are fewer than three sticks, it outputs 0.

