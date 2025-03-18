#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 50, and k_1, k_2, ..., k_n are integers such that 2 ≤ k_i ≤ 20. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` remains an integer such that 1 ≤ t ≤ 10^4. For each of the `t` iterations, `bets` is an integer, and `a` is a list of integers where each element `a[i]` is the product of all other elements in the original list `a`. `prod` is the product of the transformed list `a`. `sumo` is the sum of the elements in the transformed list `a`. If `sumo` is greater than or equal to `prod`, the output for that iteration is `-1`. Otherwise, the output is a string of the elements in `a` each followed by a space.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `n` and a list of `n` integers. It calculates a new list where each element is the product of all other elements in the original list. If the sum of the new list is greater than or equal to the product of the original list, it outputs `-1`. Otherwise, it outputs the new list as a space-separated string.

