#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers where 0 <= a_i <= n. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: t is an input integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 3 * 10^5, a is a list of n integers where 0 <= a_i <= n, buffer is an empty list.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list `w` of `n` integers. If `n` is less than 3, the function prints 0. If `n` is 3 or greater, the function calculates and prints the number of unique combinations of three elements from the list `w` that are the same. The function does not return any value; it only prints the results to the console. After processing all test cases, the function leaves the program state with `t` and `n` as input integers, `w` as a list of integers, and `buffer` as an empty list.

