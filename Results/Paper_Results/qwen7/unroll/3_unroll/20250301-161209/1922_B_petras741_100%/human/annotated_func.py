#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and the list a contains n non-negative integers such that 0 ≤ a_i ≤ n. The sum of all n values over all test cases does not exceed 3 ⋅ 10^5.
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
        
    #State: Output State: `buffer` is a list containing integers calculated from the given logic for each iteration of the loop based on the input values of `t`, `n`, and `w`. Each element in the list corresponds to the result printed for each respective input set within the loop.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes an integer t (number of cases), an integer n (size of the list), and a list a of n non-negative integers. It calculates and prints the number of specific triplets that can be formed based on the frequency of elements in the list. If n is less than 3, it prints 0. The function does not return any value but outputs the results for each test case.

