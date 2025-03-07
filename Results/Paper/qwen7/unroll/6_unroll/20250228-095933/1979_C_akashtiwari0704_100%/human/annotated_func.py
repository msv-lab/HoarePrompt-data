#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 50. The list k contains n positive integers such that 2 ≤ k_i ≤ 20 for all 1 ≤ i ≤ n.
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
        
    #State: The output state depends on the input values provided during each iteration of the loop. For each test case (value of `t`), the program calculates the least common multiple (LCM) of a list of integers (`a`), then computes a sum (`sumo`) based on the LCM and the elements of the list. If the sum is greater than or equal to the LCM, it prints `-1`. Otherwise, it prints a space-separated string of integers derived from the LCM and the original list elements. The process repeats for each test case.
#Overall this is what the function does:The function processes up to 10,000 test cases. For each test case, it reads an integer `bets`, a list of integers `a`, and calculates the least common multiple (LCM) of the list. It then computes a sum based on the LCM and the elements of the list. If the sum is greater than or equal to the LCM, it prints `-1`. Otherwise, it prints a space-separated string of integers derived from the LCM and the original list elements. This process is repeated for each test case.

