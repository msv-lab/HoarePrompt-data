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
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is an integer such that 1 <= n <= 3 * 10^5, and `a_1, a_2, ..., a_n` are integers such that 0 <= a_i <= n. The sum of `n` over all test cases does not exceed 3 * 10^5; `buffer` is an empty list. The loop has finished executing, and for each test case, the number of ways to choose three indices i, j, k such that a_i = a_j = a_k has been printed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it calculates and prints the number of ways to choose three indices \(i\), \(j\), and \(k\) such that the elements at these indices in the list are equal. The function accepts an integer `t` representing the number of test cases, and for each test case, it accepts an integer `n` and a list of `n` integers. The result for each test case is printed directly.

