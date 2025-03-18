#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3⋅10^5, and a list of integers a_1, a_2, ..., a_n where 0 ≤ a_i ≤ n. Additionally, the sum of all n values across all test cases does not exceed 3⋅10^5.
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
        
    #State: Output State: `buffer` is a list containing the results of the calculations for each iteration of the loop based on the input values of `t`, `n`, and `w`. Each result is calculated according to the provided logic and printed during the corresponding iteration. The `buffer` list will have exactly `t` elements, with each element representing the output of one iteration's calculation.
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it reads an integer `t` (1 ≤ t ≤ 10^4) and a list of integers `a_1, a_2, ..., a_n` (0 ≤ a_i ≤ n) with the condition that 1 ≤ n ≤ 3⋅10^5 and the sum of all n values across all test cases does not exceed 3⋅10^5. For each test case, it calculates and prints the number of ways to choose three distinct indices `i`, `j`, and `k` such that `a_i = a_j = a_k`. If `n < 3`, it prints 0. The function collects the results of these calculations in a list `buffer` and outputs them after processing all test cases.

