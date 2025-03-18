#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a list of n integers a_1, a_2, ..., a_n where 0 <= a_i <= n. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: `t` is an input integer such that 1 <= t <= 10^4, `i` is `t - 1`, `buffer` is an empty list. For each of the `t` test cases, the loop has processed an integer `n` and a list `w` of `n` integers. If `n` is greater than or equal to 3, the loop has computed and printed the number of ways to choose 3 elements from the list `w` such that at least two of them are the same, considering all possible values in `w`. If `n` is less than 3, the loop has printed 0.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers. If `n` is less than 3, it outputs 0. Otherwise, it calculates and outputs the number of ways to choose 3 elements from the list such that at least two of them are the same.

