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
        
    #State: After all iterations of the loop, `t` is 0, `i` is `n-1` for the last test case, `n`, `m`, and `k` are the final values from the last test case, `l` is a sorted list of integers from the last test case, `s` is the minimum of `m` and the remaining `k` from the last test case, and `c` is the total cost calculated as the sum of `k * k / 2` plus the sum of `l[j] * s - s * s / 2` for each day `j` in the last test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by the number of sale days (`n`), the maximum number of tickets purchasable each day (`m`), the total number of tickets to be bought (`k`), and a list of ticket prices for each day (`a`). It calculates and prints the minimum total cost required to buy exactly `k` tickets across the given `n` days, ensuring no more than `m` tickets are bought on any single day. After processing all test cases, the function completes without returning any value.

