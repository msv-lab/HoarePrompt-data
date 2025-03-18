#State of the program right berfore the function call: t is an integer such that 1 \le t \le 10^4, representing the number of test cases. For each test case, n, m, and k are integers such that 1 \le n \le 3 \cdot 10^5, 1 \le m \le 10^9, and 1 \le k \le \min(nm, 10^9), representing the number of sale days, the maximum amount of tickets purchasable each day, and the number of tickets to be bought, respectively. a is a list of n integers such that 1 \le a_i \le 10^9, representing the price per ticket for each of the upcoming n days. The sum of n over all test cases does not exceed 3 \cdot 10^5.
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
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `_` is `t`, the loop has completed all iterations. For each of the `t` test cases, the variables `L`, `M`, `n`, `m`, `k`, `q`, `N`, `w`, `mu`, and `cost` have been updated and printed according to the logic of the loop. The final `cost` for each test case has been calculated and printed.
#Overall this is what the function does:The function `func` processes a series of test cases, where each test case involves buying a specified number of tickets `k` over a series of sale days `n`, with a maximum number of tickets purchasable each day `m`. For each test case, the function reads the number of sale days, the maximum tickets per day, the total tickets to buy, and a list of ticket prices for each day. It calculates and prints the minimum total cost to buy the required number of tickets, considering the constraints and the sorted ticket prices. After processing all test cases, the function completes, and the final state is that the minimum total cost for each test case has been printed.

