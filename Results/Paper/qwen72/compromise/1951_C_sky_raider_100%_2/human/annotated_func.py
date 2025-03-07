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
        
    #State: After the loop executes all iterations, `i` is `n-1`, `n` remains the same as the initial value for each test case, `m` remains the same as the second integer read from the input for each test case, `k` is 0 or a non-negative integer less than the initial `k` depending on how many tickets were bought, `l` is a sorted list of integers read from the input for each test case, `t` is the total number of tickets bought, which is equal to the initial `k` or the maximum possible tickets that can be bought within the constraints, `s` is 0 or a non-negative integer less than or equal to `m` depending on the remaining `k` at the last iteration, and `c` is the total cost of buying the tickets, calculated as the sum of `s * (l[j] + t)` for each `j` from 0 to `n-1`.
#Overall this is what the function does:The function processes multiple test cases, each defined by the number of sale days (`n`), the maximum number of tickets purchasable each day (`m`), the number of tickets to be bought (`k`), and a list of ticket prices for each day (`a`). It calculates and prints the minimum total cost required to buy exactly `k` tickets over the `n` days, considering the constraints on daily purchases and ticket prices. After processing all test cases, the function has no return value, but it prints the total cost for each test case. The final state includes `k` being reduced to 0 or a non-negative integer less than the initial `k`, `l` being a sorted list of ticket prices, and `c` holding the total cost of the tickets bought.

