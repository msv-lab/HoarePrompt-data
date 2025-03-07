#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 50, and k is a list of n integers where each element k_i satisfies 2 <= k_i <= 20. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is an integer such that 1 <= `t` <= 10^4; `n` is an integer such that 1 <= `n` <= 50; `k` is a list of `n` integers where each element `k_i` satisfies 2 <= `k_i` <= 20. The sum of `n` over all test cases does not exceed 2 * 10^5.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `n` and a list `k` of `n` integers. It calculates a product of the integers in `k`, then computes a new list where each element is the product divided by the corresponding element in `k`. It checks if the sum of this new list is greater than or equal to the product. If it is, the function outputs `-1`. Otherwise, it outputs the new list of computed values, separated by spaces.

