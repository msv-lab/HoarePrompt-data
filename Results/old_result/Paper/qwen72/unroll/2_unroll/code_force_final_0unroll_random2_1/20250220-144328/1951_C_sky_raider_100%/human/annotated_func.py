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
        
    #State: For each test case, the variable `c` will hold the minimum total cost to buy `k` tickets, and `k` will be 0 (indicating all tickets have been bought). The variables `n`, `m`, and `l` will retain their initial values for the next test case, and `t` will be equal to the total number of tickets bought in the current test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by the number of sale days `n`, the maximum number of tickets purchasable each day `m`, the total number of tickets to be bought `k`, and a list `a` of ticket prices for each day. For each test case, it calculates and prints the minimum total cost to buy exactly `k` tickets, ensuring that no more than `m` tickets are bought on any single day. After processing each test case, the function resets the state for the next test case, leaving the input variables `n`, `m`, and `a` unchanged, while `k` is reduced to 0 and `t` holds the total number of tickets bought in the current test case.

