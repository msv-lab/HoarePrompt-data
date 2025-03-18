#State of the program right berfore the function call: The function `func` is expected to process multiple test cases. Each test case includes an integer n (1 ≤ n ≤ 50) representing the number of outcomes, and a list of n integers k_1, k_2, ..., k_n (2 ≤ k_i ≤ 20) representing the multipliers for the winning outcomes. The function should return a list of n integers x_1, x_2, ..., x_n (1 ≤ x_i ≤ 10^9) representing the bets on each outcome, such that the total bet is strictly less than the return for any winning outcome. If no such distribution exists, the function should return -1.
def func():
    t = int(input())
    for T in range(t):
        bets = int(input())
        
        a = [int(x) for x in input().split()]
        
        prod = 1
        
        for i in range(bets):
            prod *= a[i]
        
        sumo = 0
        
        for i in range(bets):
            a[i] = prod // a[i]
            sumo += int(a[i])
        
        if sumo >= prod:
            print(-1)
        else:
            ans = ''
            for i in range(bets):
                ans += str(a[i]) + ' '
            print(ans)
        
    #State: The function `func` processes `t` test cases, and for each test case, it prints a list of integers representing the bets on each outcome, or -1 if no such distribution exists. The variables `T`, `bets`, `a`, `prod`, `sumo`, and `ans` are updated and used within the loop, but their final values after the loop will depend on the last test case processed.
#Overall this is what the function does:The function `func` processes multiple test cases. Each test case involves an integer `n` (1 ≤ n ≤ 50) and a list of `n` integers `k_1, k_2, ..., k_n` (2 ≤ k_i ≤ 20). For each test case, the function calculates a list of `n` integers `x_1, x_2, ..., x_n` (1 ≤ x_i ≤ 10^9) such that the total sum of the bets is strictly less than the return for any winning outcome. If such a distribution is possible, the function prints the list of bets. If no such distribution exists, the function prints -1. The function does not return any value; it only prints the results.

