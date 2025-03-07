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
        
    #State: All iterations of the loop have completed, with `t` being the initial input integer where 1 ≤ t ≤ 10^4, `buffer` containing all input integers from all iterations, `i` being t-1 (indicating the loop has run t times), `n` being the last input integer from the final iteration, `w` being a list of integers from the last input split by spaces, `eta` being an empty list, `j` being greater than 1000, `rho` being the sum of `q[0]` and the first 1001 elements of `q` (i.e., `sum(q[1:1002])`), and `res` being the cumulative sum of the expressions evaluated for each `j` from 1 to 1001 if `n` is greater than or equal to 3.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of a positive integer \( t \) (1 ≤ \( t \) ≤ 10^4), a positive integer \( n \) (1 ≤ \( n \) ≤ 3 ⋅ 10^5), and a list of non-negative integers \( a \) (0 ≤ \( a_i \) ≤ \( n \)). For each test case, it calculates and prints a value based on the distribution of the integers in \( a \). If \( n \) is less than 3, it prints 0. Otherwise, it computes a specific combinatorial expression involving the counts of distinct integers in \( a \) and prints the result.

