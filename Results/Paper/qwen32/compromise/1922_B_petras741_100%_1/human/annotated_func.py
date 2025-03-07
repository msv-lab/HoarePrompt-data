#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers where each integer a_i satisfies 0 <= a_i <= n. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is the input integer from the last test case; `a` is a list of `n` integers where each integer `a_i` satisfies 0 <= `a_i` <= `n`; `buffer` is an empty list; `w` is a list of integers from the last input; `i` is equal to `t` (the loop has finished all iterations). If `n` >= 3, `q` is a list of `n + 1` integers where `q[w[j]]` is incremented by 1 for each `j` from 0 to `n-1`; `eta` is a list containing all integers from 0 to `n` for which `q[j]` is greater than 0; `eta_ln` is the length of the list `eta`; `rho` is `q[eta[0]]` if `eta_ln == 1`, otherwise `rho` is the sum of `q[eta[j]]` for all `j` from 0 to `eta_ln - 1`. If `eta_ln` is greater than 1, `res` is the sum of `q[eta[j]] * (q[eta[j]] - 1) * (q[eta[j]] - 2) // 6` and `q[eta[j]] * (q[eta[j]] - 1) // 2 * rho` for all `j` from 1 to `eta_ln - 1`. If `n` < 3, the state of the variables remains unchanged as described in the precondition.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it calculates and prints the number of ways to choose three integers from the list such that at least two of them are the same. If `n` is less than 3, it prints 0.

