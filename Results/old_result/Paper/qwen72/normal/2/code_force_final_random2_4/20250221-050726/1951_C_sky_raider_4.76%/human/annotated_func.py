#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, m, and k are integers where 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9), representing the number of sale days, the maximum amount of tickets purchasable each day, and the number of tickets to be bought, respectively. a is a list of n integers where 1 ≤ a_i ≤ 10^9, representing the price per ticket for each of the upcoming n days. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: After the loop has executed all iterations, `i` is `n-1`, `n` remains the same as the input integer, `m` remains the same as the input integer, `k` is reduced to 0 or a non-positive value (since all tickets have been bought), `l` remains the sorted list of integers provided by the user, `s` is the last computed minimum value between `m` and the remaining `k`, and `c` is the final accumulated value calculated as the initial value `k * k / 2` plus the sum of `l[j] * s - s * s / 2` for each iteration from `i = 0` to `i = n-1`.
#Overall this is what the function does:The function reads multiple sets of inputs, each set containing the number of sale days (`n`), the maximum number of tickets purchasable each day (`m`), the number of tickets to be bought (`k`), and a list of ticket prices for each day (`a`). It calculates and prints the minimum total cost required to buy exactly `k` tickets over `n` days, considering the constraints on the number of tickets that can be bought each day and the varying prices. After processing all test cases, the function completes without returning any value, but it prints the calculated minimum cost for each test case.

