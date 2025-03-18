#State of the program right berfore the function call: Each test case consists of three integers n, m, and k, where 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9), representing the number of days, the maximum tickets that can be purchased per day, and the total number of tickets to be bought, respectively. The second line of each test case contains n integers a_1, a_2, ..., a_n, where 1 ≤ a_i ≤ 10^9, representing the price per ticket for each of the upcoming n days. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: a series of integers, each representing the final value of `c` for each test case.
#Overall this is what the function does:The function calculates and prints the minimum cost to buy a specified number of tickets (`k`) over a given number of days (`n`), where the number of tickets that can be bought per day is limited (`m`). The cost is determined based on the prices of tickets for each day, which are provided as input.

