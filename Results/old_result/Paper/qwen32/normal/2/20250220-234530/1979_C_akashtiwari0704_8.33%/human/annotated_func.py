#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 50, and k is a list of n integers where each element k_i satisfies 2 ≤ k_i ≤ 20. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The program outputs the results of all test cases one by one. For each test case, it either prints `-1` if the sum of the modified elements is greater than or equal to their product, or it prints the modified elements separated by spaces.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `k` of `n` integers. For each test case, it calculates a modified list where each element is the product of all elements in `k` divided by the element itself. It then checks if the sum of the modified list is greater than or equal to the product of the original list. If so, it outputs `-1`; otherwise, it outputs the modified list elements separated by spaces.

