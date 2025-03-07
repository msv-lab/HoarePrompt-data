#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9). a is a list of n integers where each a_i is an integer such that 1 ≤ a_i ≤ 10^9.
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
        
    #State: Output State: After the loop executes all the iterations, `t` will be 0, indicating that there are no more inputs left to process. The state of `L` will be a list of integers where `L[0]` is the length of the final list `N`, `L[1]` is the minimum value between the original `m` and `k`, and `L[2]` is the third element of `L` from the last iteration. `M` will be a sorted list of integers converted from the last input string. `N` will be a list containing the first `q` elements of `M`, where `q` is the ceiling value of `k / m`. The variable `m` will be the smaller value between `L[1]` and `L[2]`, and `k` will be `L[2]` from the last iteration. The loop will have completed all its iterations, and the `continue` statement will not be executed since the condition `t > 0` will be false when `t` becomes 0.
    #
    #The `cost` calculation will depend on the specific values of `N`, `m`, and `k` from the last iteration, but it will be printed for the last iteration before the loop terminates.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers t, n, m, k, and a list a of n integers. For each test case, it sorts the list a, calculates a cost based on the sorted list and given parameters, and prints the cost. The function ensures that the cost calculation respects the constraints on n, m, and k. After processing all test cases, it outputs the total cost for the last test case.

