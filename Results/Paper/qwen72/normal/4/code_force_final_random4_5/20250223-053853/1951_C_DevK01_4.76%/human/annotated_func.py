#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9), representing the number of sale days, the maximum amount of tickets purchasable each day, and the number of tickets to be bought, respectively. a is a list of n integers such that 1 ≤ a_i ≤ 10^9, representing the price per ticket for each of the upcoming n days. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop has finished executing for all test cases. For each test case, the variable `cost` has been calculated and printed, representing the minimum cost to buy `k` tickets over `n` days, with the maximum of `m` tickets purchasable each day. The variables `t`, `n`, `m`, `k`, and `a` (the list of prices) retain their initial values as they are not modified within the loop. The intermediate variables `L`, `M`, `q`, `N`, `w`, and `mu` are recalculated for each test case and do not persist outside the loop.
#Overall this is what the function does:The function `func` reads the number of test cases `t` and, for each test case, reads the number of sale days `n`, the maximum number of tickets purchasable each day `m`, the total number of tickets to be bought `k`, and a list of ticket prices `a` for each day. It calculates and prints the minimum cost to buy `k` tickets over `n` days, considering the constraint that no more than `m` tickets can be bought on any single day. The function does not return any value; it only prints the result for each test case. After all test cases are processed, the function terminates.

