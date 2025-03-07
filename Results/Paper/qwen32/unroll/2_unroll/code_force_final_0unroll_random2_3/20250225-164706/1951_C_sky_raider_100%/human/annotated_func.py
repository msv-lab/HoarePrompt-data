#State of the program right berfore the function call: Each test case consists of three integers n, m, and k, where 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9), representing the number of sale days, the maximum amount of tickets purchasable each day, and the number of tickets to be bought, respectively. The second line of each test case contains n integers a_1, a_2, ..., a_n, where 1 ≤ a_i ≤ 10^9, representing the price per ticket for each of the upcoming n days. The sum of n over all test cases does not exceed 3 · 10^5.
def func():
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        l.sort()
        
        t = 0
        
        s = 0
        
        c = 0
        
        for i in range(n):
            s = min(m, k)
            c += s * (l[i] + t)
            t += s
            k -= s
        
        print(int(c))
        
    #State: the total cost `c` for the last test case.
#Overall this is what the function does:The function calculates and prints the minimum cost required to buy `k` tickets over `n` sale days, given that up to `m` tickets can be purchased each day and each day has a specific price per ticket.

