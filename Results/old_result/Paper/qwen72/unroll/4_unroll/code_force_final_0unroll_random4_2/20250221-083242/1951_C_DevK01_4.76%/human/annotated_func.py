#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, m, and k are integers where 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, 1 ≤ k ≤ min(nm, 10^9), representing the number of sale days, the maximum amount of tickets purchasable each day, and the number of tickets to be bought, respectively. a is a list of n integers where 1 ≤ a_i ≤ 10^9, representing the price per ticket for each of the upcoming n days. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: After the loop executes all iterations, the variable `t` will be 0, as the loop has iterated `t` times. The variables `L`, `M`, `n`, `m`, `k`, `q`, `N`, `w`, `mu`, and `cost` will have their final values based on the last test case processed, but these values are not guaranteed to be consistent across different test cases. The list `M` will be sorted and potentially modified by the `.pop()` operation. The variable `cost` will hold the total cost calculated for the last test case. The sum of `n` over all test cases will still not exceed 3 · 10^5.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by the number of sale days `n`, the maximum number of tickets purchasable each day `m`, the total number of tickets to be bought `k`, and a list `a` of ticket prices for each day. For each test case, it calculates and prints the minimum cost required to buy exactly `k` tickets over the `n` sale days. After processing all test cases, the function does not return any value, but the variable `t` will be 0, and the list `a` will be sorted and potentially modified. The final state of other variables (`L`, `M`, `n`, `m`, `k`, `q`, `N`, `w`, `mu`, and `cost`) will be based on the last test case processed.

