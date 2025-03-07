#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of n integers where 0 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `buffer` remains an empty list; all other variables (`t`, `n`, `a`, `w`, `q`, `eta`, `eta_ln`, `rho`, `res`) are in their final states after the last iteration of the loop, but since `buffer` is not modified within the loop, it stays empty.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` and a list `a` of `n` integers. For each test case, it calculates and prints the number of ways to choose three integers from the list such that at least two of them are the same. If `n` is less than 3, it prints 0.

