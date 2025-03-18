#State of the program right berfore the function call: Each test case consists of three integers n, m, and k where 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9), representing the number of sale days, the maximum amount of tickets purchasable each day, and the number of tickets to be bought, respectively. The second line of each test case contains n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9, representing the price per ticket for each of the upcoming n days. The total number of n across all test cases does not exceed 3 · 10^5.
def func():
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        l.sort()
        
        s = 0
        
        c = k * k / 2
        
        for i in range(n):
            s = min(m, k)
            k -= s
            c += l[i] * s - s * s / 2
        
        print(int(c))
        
    #State: n, m, l unchanged; k is 0 or the remaining tickets that couldn't be bought; c is the total cost of buying the tickets.
#Overall this is what the function does:The function calculates and prints the minimum cost required to purchase `k` tickets over `n` days, given the daily ticket prices and the constraint that no more than `m` tickets can be bought in a single day.

