#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case consists of an integer n such that 1 <= n <= 50, followed by a list of n integers k_1, k_2, ..., k_n where 2 <= k_i <= 20 for each i. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: Variables `t`, `bets`, `a`, `prod`, `sumo`, and `ans` do not retain specific values after all iterations, and the output is printed directly within the loop for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `n` and a list of `n` integers, computes a modified list based on the least common multiple (LCM) of the input integers, and prints either the modified list or `-1` if a specific condition is met.

