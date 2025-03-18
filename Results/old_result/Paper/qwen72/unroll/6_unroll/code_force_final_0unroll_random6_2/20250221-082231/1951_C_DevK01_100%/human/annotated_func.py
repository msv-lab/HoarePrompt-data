#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 3 · 10^5, m is an integer such that 1 ≤ m ≤ 10^9, k is an integer such that 1 ≤ k ≤ min(nm, 10^9), and a is a list of n integers such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop has finished executing all iterations, and for each iteration, the variable `cost` is calculated and printed. The variables `t`, `n`, `m`, `k`, and `a` remain unchanged as they are not modified within the loop. The list `M` is sorted and potentially modified by the `pop` operation, but its state is reset in each iteration. The variables `L`, `N`, `q`, `w`, and `mu` are local to the loop and do not persist between iterations.
#Overall this is what the function does:The function `func` processes multiple test cases defined by an integer `t`. For each test case, it reads two lines of input: the first line contains three integers `n`, `m`, and `k`, and the second line contains a list of `n` integers `M`. The function calculates a cost based on the values of `n`, `m`, `k`, and the elements of `M`. The cost is determined by sorting the list `M`, selecting a subset of its elements, and performing arithmetic operations. The calculated cost is printed for each test case. The function does not return any value, and the input variables `t`, `n`, `m`, `k`, and `a` (if present) remain unchanged. The list `M` is sorted and potentially modified by the `pop` operation, but its state is reset in each iteration.

