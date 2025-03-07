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
        
    #State: For each test case, the output state is the integer value of c, which represents the minimum total cost to buy k tickets, considering the constraints and the sorted list of ticket prices.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `n`, `m`, and `k`, and a list of `n` integers `a`. It calculates and prints the minimum total cost to buy exactly `k` tickets over `n` sale days, where the price per ticket on each day is given by the list `a`, and the maximum number of tickets that can be bought each day is `m`. The function does not return any value; it only prints the result for each test case.

