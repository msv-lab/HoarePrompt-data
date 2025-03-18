#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and a is a list of non-negative integers such that 0 ≤ a_i ≤ n. The sum of all n over all test cases does not exceed 3 ⋅ 10^5.
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
        
    #State: Output State: `t` is a positive integer between 1 and 10^4, `n` is a series of integers where each integer is the value of `n` from each iteration of the loop, `a` remains unchanged, `buffer` is an empty list, and the loop has printed the calculated results for each value of `n`.
#Overall this is what the function does:The function processes a series of test cases, each containing a positive integer \( t \) (number of test cases), a positive integer \( n \) (size of the list), and a list of non-negative integers \( a \). For each test case, it calculates and prints a specific value based on the distribution of elements in the list \( a \). If \( n < 3 \), it prints 0. Otherwise, it computes a value related to combinations and sums of counts of distinct elements in \( a \).

