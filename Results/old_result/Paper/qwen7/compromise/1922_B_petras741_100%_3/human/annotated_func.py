#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3⋅10^5, and the list a contains n non-negative integers such that 0 ≤ a_i ≤ n. The sum of all n values across all test cases does not exceed 3⋅10^5.
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
        
    #State: Output State: `t` is a positive integer such that \(1 \leq t \leq 10^4\), `buffer` is a list containing integers from the input for all iterations, `i` is 9999 (since the loop runs `t` times), `n` is the last input integer processed, `w` is the last list of integers obtained from splitting the input and converting each element to an integer, and if `n` is greater than or equal to 3, `res` is the final cumulative sum of the terms calculated in the loop, which can be expressed as \(\sum_{j=1}^{n} q[eta[j]] * (q[eta[j]] - 1) * (q[eta[j]] - 2) // 6 + \sum_{j=1}^{n} q[eta[j]] * (q[eta[j]] - 1) // 2 * rho\). If `n` is less than 3, `res` remains unchanged.
    #
    #This means that after all iterations of the loop have finished, the variable `t` will still hold its initial value, but `buffer` will contain all the integers provided as input across all iterations. The variable `i` will be `t-1` because the loop increments `i` from `0` to `t-1`. The variable `n` will be the last input integer processed, and `w` will be the last list of integers split from the input. The variable `res` will hold the final result calculated based on the last iteration's inputs if `n` was greater than or equal to 3; otherwise, it will retain its value from the last valid iteration.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer \( t \) (1 ≤ \( t \) ≤ 10^4) followed by \( n \) (1 ≤ \( n \) ≤ 3⋅10^5) non-negative integers in a list \( a \) (0 ≤ \( a_i \) ≤ \( n \)). For each test case, it calculates and prints a specific value based on the distribution of integers in the list \( a \). If \( n \) is less than 3, it prints 0. Otherwise, it computes a cumulative sum involving the counts of distinct integers in the list and prints the result. After processing all test cases, the function outputs the results for each test case.

