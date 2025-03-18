#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, m, and k are integers where 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9), representing the number of sale days, the maximum number of tickets purchasable each day, and the total number of tickets to be bought, respectively. a is a list of n integers where 1 ≤ a_i ≤ 10^9, representing the price per ticket for each of the n days. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop has finished executing all iterations, and for each test case, the total cost of buying `k` tickets has been calculated and printed. The variables `t`, `n`, `m`, `k`, and `a` are not directly modified by the loop and retain their initial values or are re-initialized for each test case. The list `M` is sorted and potentially modified during each iteration, but its final state for each test case is not retained for the next iteration. The variables `L`, `N`, `q`, `w`, `mu`, and `cost` are local to each iteration and are re-initialized for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads the number of sale days `n`, the maximum number of tickets purchasable each day `m`, the total number of tickets to be bought `k`, and a list of ticket prices `a` for each day. It calculates and prints the minimum total cost required to buy `k` tickets over the `n` days. The function does not return any value; it only prints the cost for each test case. After processing all test cases, the function concludes.

