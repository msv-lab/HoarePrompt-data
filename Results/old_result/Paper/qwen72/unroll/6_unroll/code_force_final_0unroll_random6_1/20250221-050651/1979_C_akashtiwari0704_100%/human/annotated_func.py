#State of the program right berfore the function call: The function is designed to handle multiple test cases, where each test case includes an integer n (1 ≤ n ≤ 50) representing the number of outcomes, and a list of n integers k_1, k_2, ..., k_n (2 ≤ k_i ≤ 20) representing the multipliers for the winning outcomes. The total number of test cases, t, is an integer (1 ≤ t ≤ 10^4). The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    t = int(input())
    for T in range(t):
        def lcm(l):
            g = 1
            for i in range(len(l)):
                g = g * l[i] // gcd(g, l[i])
            return g
        
        bets = int(input())
        
        a = [int(x) for x in input().split()]
        
        prod = lcm(a)
        
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
        
    #State: The loop has processed all test cases. For each test case, if the sum of the transformed multipliers (which are the result of dividing the least common multiple of the original multipliers by each multiplier) is greater than or equal to the least common multiple, the output is -1. Otherwise, the output is a space-separated list of the transformed multipliers. The variable `t` remains unchanged, and the loop has completed all iterations.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by an integer `n` and a list of `n` integers `k_1, k_2, ..., k_n`. For each test case, it calculates the least common multiple (LCM) of the integers in the list, transforms each integer by dividing the LCM by the integer, and sums these transformed values. If the sum of the transformed values is greater than or equal to the LCM, the function prints `-1`. Otherwise, it prints a space-separated list of the transformed values. The function does not return any value but prints the results directly. After processing all test cases, the variable `t` remains unchanged, and the loop has completed all iterations.

