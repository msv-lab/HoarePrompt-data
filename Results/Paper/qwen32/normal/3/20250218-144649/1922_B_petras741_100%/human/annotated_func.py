#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a_1, a_2, ..., a_n are integers such that 0 <= a_i <= n. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is the new input integer, `a_1, a_2, ..., a_n` are integers such that 0 <= a_i <= n, `buffer` is an empty list, `w` is a list of integers obtained by converting the space-separated input values to integers, `i` is `t` (indicating all iterations have been completed). If `n` >= 3 during any iteration, `q` is a list of `n + 1` integers where `q[w[j]]` is incremented by 1 for each `i` from 0 to `n-1`, `eta` is a list containing all the indices from 0 to n for which `q[j]` is greater than 0, `eta_ln` is the length of the list `eta`, `rho` is the sum of all `q[eta[j]]` for `j` from `0` to `eta_ln - 1`, and `res` is the computed sum of terms involving each `q[eta[j]]` and the cumulative `rho`. If `n` < 3 during any iteration, no further changes are made to the variables beyond the initial conditions.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it calculates and prints the number of ways to choose three distinct indices from a list of integers such that the integers at those indices are the same. If the list has fewer than three elements, it prints 0.

