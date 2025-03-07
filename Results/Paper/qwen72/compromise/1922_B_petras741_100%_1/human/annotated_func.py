#State of the program right berfore the function call: The function is expected to handle multiple test cases. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of n integers where 0 ≤ a_i ≤ n. The total sum of n across all test cases does not exceed 3 · 10^5.
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
        
    #State: `i` is `t`, `buffer` is an empty list. For each test case, if `n` is less than 3, the variables `q`, `eta`, `eta_ln`, `rho`, and `res` remain undefined. If `n` is greater than or equal to 3, `q` is a list of length `n + 1` where each element `q[k]` (for `k` in `w`) is the count of how many times `k` appears in `w`, `eta` is a list containing all the integers `k` from 0 to `n` for which `q[k]` is greater than 0, `eta_ln` is the length of `eta`, `rho` is the sum of the counts of all elements in `eta` that appear in `w`, and `res` is the sum of the combinations of 3 elements from each `q[eta[j]]` plus the sum of the combinations of 2 elements from each `q[eta[j]]` multiplied by the total count of elements in `eta` that appear in `w` before the current element.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads an integer `n` and a list of `n` integers `w`. If `n` is less than 3, the function prints 0. If `n` is 3 or greater, the function calculates and prints the number of unique combinations of three elements from the list `w` that are all the same, plus the number of unique combinations of two elements from the list `w` that are the same, multiplied by the count of the first unique element. After processing all test cases, the function terminates.

