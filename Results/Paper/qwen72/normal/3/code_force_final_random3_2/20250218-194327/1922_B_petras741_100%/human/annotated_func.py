#State of the program right berfore the function call: The function is designed to handle multiple test cases. Each test case includes an integer n (1 ≤ n ≤ 3 · 10^5) representing the number of sticks, and a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n) where each a_i represents the exponent of the length of the i-th stick, 2^{a_i}. The input must be provided in the format described, and the sum of n over all test cases should not exceed 3 · 10^5.
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
        
    #State: `t` is 0, `i` is `t`, `n` is an input integer, and `w` is a list of integers input by the user. If `n` is less than 3, no additional changes are made. If `n` is at least 3, `q` is a list of length `n + 1` where each element `q[k]` (for `k` in the range of `w`) is the count of how many times `k` appears in `w`. `eta` is a list containing all integers `k` from 0 to `n` (inclusive) for which `q[k]` is greater than 0, and `eta_ln` is the length of `eta`. If `eta_ln` is 1, `rho` is the count of how many times `eta[0]` appears in `w`. If `eta_ln` is not 1, `rho` is the sum of the counts of how many times each integer in `eta` appears in `w`. `res` is the sum of `q[k] * (q[k] - 1) * (q[k] - 2) // 6` plus `q[k] * (q[k] - 1) // 2 * rho` for all `k` in `eta` if `eta_ln` is not 1.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. Each test case consists of an integer `n` and a list of `n` integers `w` representing the exponents of the lengths of sticks. The function calculates and prints the number of ways to choose three sticks such that the sum of the lengths of any two sticks is greater than the length of the third stick. If `n` is less than 3, the function prints 0 for that test case. After processing all test cases, the function terminates with no return value. The input variables `t`, `n`, and `w` are consumed and not modified.

