#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3⋅10^5, and a is a list of non-negative integers such that 0 ≤ a_i ≤ n for all i where 1 ≤ i ≤ n. The sum of all n over all test cases does not exceed 3⋅10^5.
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
        
    #State: t is at least 1, n is an integer, w is a list of integers, i is 3, j is -1, eta is a list containing all indices j (from n-1 down to 0) for which q[j] was greater than 0 at any point during the loop's execution, eta_ln is the length of eta and is equal to 1, rho is the sum of all q[eta[j]] values encountered during the loop, and res is the sum of all the increments made to it during each iteration.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `t` (number of test cases), an integer `n`, and a list `w` of `n` non-negative integers. It then calculates and prints a specific value based on the distribution of elements in the list `w`. If `n` is less than 3, it prints 0. Otherwise, it computes a combinatorial value related to the frequency of unique elements in the list `w`.

