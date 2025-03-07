#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, m, and k are integers where 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9), representing the number of sale days, the maximum amount of tickets purchasable each day, and the number of tickets to be bought, respectively. a is a list of n integers where 1 ≤ a_i ≤ 10^9, representing the price per ticket for each of the upcoming n days. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop has completed all iterations, and for each test case, the total cost of buying `k` tickets has been printed. The variables `t`, `n`, `m`, `k`, and `a` retain their initial values or are reset for each test case, while the variables `L`, `M`, `q`, `N`, `w`, `mu`, and `cost` are used and modified within the loop but do not persist outside of each test case iteration.
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases. For each test case, it reads two lines of input: the first line contains integers `n`, `m`, and `k`, representing the number of sale days, the maximum number of tickets purchasable each day, and the total number of tickets to be bought, respectively. The second line contains a list of `n` integers representing the ticket prices for each day. The function calculates and prints the minimum total cost to buy exactly `k` tickets over the `n` days, ensuring that no more than `m` tickets are bought on any single day. After processing all test cases, the function concludes, and the variables `t`, `n`, `m`, `k`, and `a` retain their initial values or are reset for each test case, while other variables used within the loop do not persist outside of each test case iteration.

