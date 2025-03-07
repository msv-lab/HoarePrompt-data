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
        
    #State: After the loop executes all iterations, `t` remains an integer where 1 ≤ t ≤ 10^4, `i` is `t-1`, `n` is the same as the initial value of `n` for each test case, `m` is the same as the initial value of `m` for each test case, `k` is 0, `s` is the last computed value of `min(m, k)` before `k` becomes 0, `c` is the final computed cost which is the sum of the costs calculated for each test case, and the list `l` is a sorted list of integers from the input for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by the number of sale days (`n`), the maximum number of tickets that can be purchased each day (`m`), the total number of tickets to be bought (`k`), and a list of ticket prices for each day (`a`). For each test case, it calculates and prints the minimum total cost required to purchase exactly `k` tickets, adhering to the constraint of buying no more than `m` tickets on any single day. After processing all test cases, the function has printed the minimum total cost for each one, and the variables `t`, `n`, `m`, and `k` retain their values as described in the initial state, with `k` being reduced to 0 for each test case. The list `a` (renamed to `l` in the function) is sorted and retains its sorted state after processing.

