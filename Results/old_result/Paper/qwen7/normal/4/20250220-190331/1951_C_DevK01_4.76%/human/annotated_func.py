#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9). a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n.
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
            cost += m * sum(N) + m * m * ((n - 1) * (n - 2) // 2) + n * m * mu
        
        print(cost)
        
        continue
        
    #State: Output State: All the necessary lists and variables will retain their final values after the loop completes its execution. Specifically, `t` will be the total number of iterations the loop ran, which is provided initially. For each iteration `_` in the range of `t`, the following will hold true:
    #
    #- `L` will be a list of integers entered by the user for that specific iteration.
    #- `M` will be a sorted version of `L`.
    #- `n` will be the length of the list `N`.
    #- `m` will be the minimum value between the second and third elements of `L`.
    #- `k` will be the third element of `L`.
    #- `q` will be the ceiling value of `k / m`.
    #- `N` will be a sublist of `M` containing the first `q` elements of `M`.
    #- `cost` will be the calculated cost based on the conditions specified in the code, either as `m * sum(N) + m * m * ((n - 1) * n // 2)` or `cost + m * sum(N) + m * m * ((n - 1) * (n - 2) // 2) + n * m * mu`.
    #
    #After all iterations, the final values of `t`, `L`, `M`, `n`, `m`, `k`, `q`, `N`, and `cost` will reflect the results of the last iteration of the loop. The `continue` statement ensures that the loop proceeds to the next iteration without altering the current values of the variables. Thus, the output state will show the culmination of all individual iteration calculations, with `cost` being the sum of costs from all iterations.
#Overall this is what the function does:The function processes a series of test cases, each consisting of integers \( t \), \( n \), \( m \), and \( k \), and a list \( a \) of \( n \) integers. For each test case, it calculates a cost based on specific conditions involving the sorted list \( M \) derived from \( a \), and prints the cumulative cost after processing all test cases. The function does not return any value but modifies internal variables to store intermediate and final results for each test case.

