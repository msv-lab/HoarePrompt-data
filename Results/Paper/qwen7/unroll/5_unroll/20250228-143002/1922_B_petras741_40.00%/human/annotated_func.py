#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3⋅10^5, and a list of integers a_1, a_2, ..., a_n where 0 ≤ a_i ≤ n. Additionally, the sum of all n values across all test cases does not exceed 3⋅10^5.
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
        
    #State: Output State: `buffer` contains a series of integers representing the results of each iteration of the loop, with each result calculated based on the input values of `n` and `w` for each test case. Each result is printed according to the conditions specified within the loop body. If `n < 3`, the output is `0`. Otherwise, the output is calculated using combinations and sums based on the frequency of elements in the list `w`.
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it accepts an integer `t` (1 ≤ t ≤ 10^4) representing the number of test cases, followed by `t` groups of inputs. Each group contains an integer `n` (1 ≤ n ≤ 3⋅10^5) and a list of `n` integers `a_1, a_2, ..., a_n` (0 ≤ a_i ≤ n). For each test case, it calculates and prints a result based on the frequency of elements in the list `w`. If `n < 3`, the output is `0`. Otherwise, the output is calculated using combinations and sums based on the frequency of elements in the list `w`. The function does not return any value but prints the results for each test case.

