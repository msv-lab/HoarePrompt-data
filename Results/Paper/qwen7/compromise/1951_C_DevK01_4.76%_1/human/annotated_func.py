#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n, m, and k are integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(n⋅m, 10^9); a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for all i in range n.
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
        
    #State: Output State: The final value of `t` will be the same as the initial value of `t`. For each iteration of the loop, the variables `n`, `m`, `k`, and `a` will be updated based on the input lists `L` and `M`. The variable `cost` will be calculated differently depending on the values of `n` and `m`, and printed at the end of each iteration. After all iterations, the final state of `t`, along with all the `cost` values printed during each iteration, will be the output state.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( t \), \( n \), \( m \), and \( k \), and a list \( a \) of \( n \) integers. For each test case, it calculates a cost based on the values of \( n \), \( m \), and \( k \), and prints the cost. The function updates the values of \( n \), \( m \), and \( k \) based on the input, sorts the list \( M \), and computes the cost using specific conditions. After processing all test cases, it outputs the final value of \( t \) and the costs calculated for each test case.

