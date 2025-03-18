#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 50, and k is a list of n integers where each k_i is an integer such that 2 <= k_i <= 20. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: t is an input integer, n is an integer such that 1 <= n <= 50, and k is a list of n integers where each k_i is an integer such that 2 <= k_i <= 20.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives an integer `bets` and a list `a` of `bets` integers. It calculates the least common multiple (LCM) of the integers in the list, then modifies each integer in the list to be the LCM divided by that integer. If the sum of these modified integers is greater than or equal to the LCM, it outputs `-1`. Otherwise, it outputs the modified list of integers.

