#State of the program right berfore the function call: t is an integer (1 ≤ t ≤ 10^4), n is an integer (1 ≤ n ≤ 3 · 10^5), m is an integer (1 ≤ m ≤ 10^9), k is an integer (1 ≤ k ≤ min(nm, 10^9)), and a is a list of n integers (1 ≤ a_i ≤ 10^9). The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop iterates `t` times, and for each iteration, it reads two lines of input, processes the values of `n`, `m`, and `k`, and prints the calculated `cost`. The variables `L`, `M`, `n`, `m`, `k`, `N`, `q`, `w`, `mu`, and `cost` are updated and used within the loop, but their final values after the loop are not relevant to the initial state. The initial state variables `t`, `n`, `m`, `k`, and `a` remain unchanged outside the loop.
#Overall this is what the function does:The function reads multiple test cases from the input, where each test case consists of two lines: the first line contains three integers `n`, `m`, and `k`, and the second line contains a list of `n` integers. For each test case, it calculates a cost based on the values of `n`, `m`, `k`, and the sorted list of integers. The function then prints the calculated cost for each test case. The function does not return any value, but it processes and prints the cost for each of the `t` test cases. The initial state variables `t`, `n`, `m`, `k`, and `a` remain unchanged outside the loop.

