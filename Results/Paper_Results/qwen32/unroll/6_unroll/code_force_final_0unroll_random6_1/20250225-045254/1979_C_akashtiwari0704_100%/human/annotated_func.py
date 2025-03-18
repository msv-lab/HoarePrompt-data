#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 50, and k is a list of n integers where each k_i is an integer such that 2 ≤ k_i ≤ 20. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: - Since the variables `bets`, `a`, `prod`, `sumo`, and `ans` are local to each iteration, their final values are not stored or reflected in the global state after all iterations are complete.
    #   - The only variables that remain unchanged throughout the loop executions are `t`, `n`, and `k`.
    #
    #Given this understanding, the output state after all iterations of the loop is:
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of integers. For each test case, it calculates a value based on the least common multiple (LCM) of the integers and their relationships. It then outputs either a list of derived values or -1, depending on a specific condition involving the sum of these derived values relative to the LCM.

