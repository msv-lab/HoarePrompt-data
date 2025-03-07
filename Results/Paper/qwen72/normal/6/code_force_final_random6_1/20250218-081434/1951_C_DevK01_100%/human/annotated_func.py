#State of the program right berfore the function call: t is an integer (1 ≤ t ≤ 10^4), n, m, and k are integers (1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, 1 ≤ k ≤ min(nm, 10^9)), and a is a list of n integers (1 ≤ a_i ≤ 10^9). The sum of n over all test cases does not exceed 3 · 10^5.
def func():
    t = int(input())
    for _ in range(t):
        L = list(map(int, input().split()))
        
        M = list(map(int, input().split()))
        
        n, m, k = L[0], L[1], L[2]
        
        m = min(m, k)
        
        M.sort()
        
        q = int(math.ceil(k / m))
        
        N = M[:q]
        
        n = len(N)
        
        if n * m == k:
            cost = m * sum(N) + m * m * ((n - 1) * n // 2)
        else:
            w = N.pop()
            mu = k - (n - 1) * m
            cost = mu * w
            n = len(N)
            cost += m * sum(N) + m * m * ((n - 1) * n // 2) + n * m * mu
        
        print(cost)
        
        continue
        
    #State: `t` is 0, `_` is `t - 1`, `L` is a list of integers provided by the user, `M` is a sorted list of integers converted from the input provided by the user, `n` is the number of elements in `N`, `m` is the minimum of the second integer in `L` and the third integer in `L`, `k` is the third integer in `L`, `q` is the ceiling of `k / m`. If `n * m == k`, `N` is a list containing the first `q` elements of `M`, `cost` is `m * sum(N) + m * m * ((n - 1) * n // 2)`, and `mu` is not defined. Otherwise, `N` is a list containing the first `q - 1` elements of `M`, `w` is the last element of the original `N`, `mu` is `k - (n - 1) * m`, and `cost` is updated to `mu * w + m * sum(N) + m * m * ((n - 1) * n // 2) + n * m * mu`. The `continue` statement does not change any variable values but continues to the next iteration of the loop.
#Overall this is what the function does:The function reads multiple test cases from the input, each consisting of a list `L` containing three integers `n`, `m`, and `k`, and a list `M` of integers. For each test case, it calculates a cost based on the sorted elements of `M` and the values of `n`, `m`, and `k`. The cost is computed differently depending on whether `n * m` equals `k` or not. The function prints the cost for each test case and continues to the next one until all test cases are processed. After the function concludes, `t` is 0, and the variables `L`, `M`, `n`, `m`, `k`, `q`, `N`, `w`, and `cost` are in the final state as described in the annotated code for the last test case.

