#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3⋅10^5, and a list contains n integers a_1, a_2, ..., a_n where 0 ≤ a_i ≤ n. The sum of all n values across all test cases does not exceed 3⋅10^5.
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
        
    #State: After executing all iterations, the output state will consist of a series of integers printed as the result of the loop's operations. For each test case, if `n` is greater than or equal to 3, the program calculates a specific combinatorial value based on the frequency of unique elements in the list `w`. If `n` is less than 3, it prints 0. The final output state is a sequence of these calculated values for each test case.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer t and a list of n integers. For each test case, it calculates a combinatorial value based on the frequency of unique elements in the list if n is greater than or equal to 3, otherwise, it prints 0. The function outputs a sequence of these calculated values for each test case.

