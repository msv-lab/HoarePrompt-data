#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, each test case contains an integer n such that 1 ≤ n ≤ 50, and a list of n integers k_1, k_2, ..., k_n where 2 ≤ k_i ≤ 20 for all i. Additionally, the sum of n over all test cases does not exceed 2 × 10^5.
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
        
    #State: Output State: t is the number of test cases, and for each test case, bets is the number of integers in the list a, prod is the least common multiple (LCM) of the integers in a, sumo is the sum of the elements in a after dividing each element by prod, and ans is a string containing the elements of a separated by spaces. If sumo is greater than or equal to prod, -1 is printed instead.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `bets` and a list of `bets` integers `a`. It calculates the least common multiple (LCM) of the integers in the list and then divides each integer in the list by this LCM. It sums these divided values. If the sum is greater than or equal to the LCM, it prints `-1`; otherwise, it constructs a string containing the modified integers and prints this string. The function does not return any value but outputs the results for each test case.

