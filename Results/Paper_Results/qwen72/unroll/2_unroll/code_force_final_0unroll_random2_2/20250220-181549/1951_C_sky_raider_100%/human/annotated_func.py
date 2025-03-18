#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9), representing the number of sale days, the maximum number of tickets purchasable each day, and the number of tickets to be bought, respectively. a is a list of n integers such that 1 ≤ a_i ≤ 10^9, representing the price per ticket for each of the upcoming n days. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: For each test case, the variable `c` will hold the minimum total cost to buy `k` tickets, and `k` will be 0 (indicating all tickets have been bought). The variables `n`, `m`, and the list `l` will retain their initial values, and `t` will be equal to the total number of tickets bought, which is `k` from the initial state.
#Overall this is what the function does:The function `func` processes multiple test cases, where each test case involves buying a specified number of tickets `k` over a given number of days `n`, with a maximum of `m` tickets purchasable each day. The function reads the number of test cases and the details of each test case from the standard input. For each test case, it calculates and prints the minimum total cost to buy `k` tickets by purchasing the cheapest available tickets first, up to the daily limit `m`. After processing each test case, the function ensures that `k` tickets have been bought, and the total cost `c` is printed. The variables `n`, `m`, and the list of ticket prices `l` retain their initial values after each test case.

