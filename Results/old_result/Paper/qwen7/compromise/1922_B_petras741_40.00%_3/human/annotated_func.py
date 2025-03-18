#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3⋅10^5, and a is a list of non-negative integers such that 0 ≤ a_i ≤ n for all 1 ≤ i ≤ n. The sum of all n over all test cases does not exceed 3⋅10^5.
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
        
    #State: All iterations of the loop have been executed. The variable `i` will have a value of `t-1` since it increments by 1 in each iteration of the loop. For each `i` from 0 to `t-1`, the following conditions hold: `n` is an integer input by the user, `w` is a list of integers converted from the input split by spaces. If `n` is greater than or equal to 3, `eta` is a list of unique integers from `w` that have a count greater than 0 in `q`, `eta_ln` is the length of `eta`, `rho` is the sum of `q[eta[j]]` for all `j` in `eta`, and `res` accumulates the contributions from each iteration of the loop as described. If `n` is less than 3, `res` is simply 0.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `t` representing the number of sub-cases, followed by an integer `n` and a list `a` of `n` non-negative integers. If `n` is greater than or equal to 3, it calculates a specific combinatorial result based on the frequency of unique integers in the list `a`. If `n` is less than 3, it returns 0. The function prints the calculated result for each valid sub-case and does not return any value explicitly.

