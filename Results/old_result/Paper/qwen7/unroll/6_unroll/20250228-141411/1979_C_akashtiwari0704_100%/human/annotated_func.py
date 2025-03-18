#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 50, and k is a list of n integers where 2 ≤ k_i ≤ 20 for all 1 ≤ i ≤ n.
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
        
    #State: The output state depends on the input values of `t`, `bets`, and the list `a`. For each iteration of the outer loop (controlled by `T`), the program calculates the least common multiple (LCM) of the elements in list `a`, then modifies the list by dividing the LCM by each element. It sums these modified values. If the sum is greater than or equal to the LCM, it prints `-1`. Otherwise, it prints the modified list elements separated by spaces. This process repeats `t` times. The final output will be the result of the last iteration of the outer loop.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `t` indicating the number of test cases, an integer `bets` indicating the number of elements in the list `a`, and a list `a` of integers. It calculates the least common multiple (LCM) of the elements in `a`, then modifies each element in `a` by dividing the LCM by itself. It sums these modified values. If the sum is greater than or equal to the LCM, it prints `-1`. Otherwise, it prints the modified list elements separated by spaces. This process repeats `t` times. The final output is the result of the last iteration of the outer loop.

