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
        
    #State: After the loop executes all the iterations, `i` is `n-1`, `n` remains the same as provided by the user, `m` remains the same as provided by the user, `k` is 0 or a non-negative integer less than `m`, `s` is the minimum of `m` and the final value of `k` before each iteration, `c` is the total cost calculated as the sum of `s * (l[j] + t)` for each `j` from 0 to `n-1`, and `t` is the total number of tickets bought, which is equal to the initial `k` or the maximum possible tickets that can be bought within the constraints. The list `l` remains the same sorted list of integers provided by the user.
#Overall this is what the function does:The function processes multiple test cases, each defined by the number of sale days (`n`), the maximum number of tickets purchasable each day (`m`), the total number of tickets to buy (`k`), and a list of prices per ticket for each day (`a`). For each test case, it calculates and prints the minimum cost required to buy exactly `k` tickets, considering the daily purchase limit and the sorted ticket prices. After processing all test cases, the function concludes, and the final state includes the printed minimum costs for each test case. The input variables `n`, `m`, and `a` remain unchanged, while `k` is reduced to 0 or a non-negative integer less than `m`.

