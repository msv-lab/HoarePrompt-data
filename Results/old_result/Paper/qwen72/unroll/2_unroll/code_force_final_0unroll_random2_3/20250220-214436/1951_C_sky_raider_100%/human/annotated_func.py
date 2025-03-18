#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, m, and k are integers where 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9), representing the number of sale days, the maximum amount of tickets purchasable each day, and the number of tickets to be bought, respectively. a is a list of n integers where 1 ≤ a_i ≤ 10^9, representing the price per ticket for each of the upcoming n days. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: For each test case, the variable `c` will contain the minimum total cost to buy `k` tickets, and `k` will be 0 after the loop has executed all iterations. The values of `n`, `m`, and `l` will remain unchanged.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case involves buying a specified number of tickets (`k`) over a given number of days (`n`), with a limit on the number of tickets that can be bought each day (`m`). The function reads the number of test cases (`t`), and for each test case, it reads `n`, `m`, `k`, and a list of ticket prices for each day (`a`). It calculates and prints the minimum total cost to buy `k` tickets by sorting the ticket prices and buying the cheapest available tickets first, up to the daily limit. After processing all test cases, the function does not return any value, but it prints the minimum total cost for each test case. The input variables `n`, `m`, and `a` remain unchanged after each test case.

