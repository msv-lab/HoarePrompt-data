#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 50, and k_1, k_2, ..., k_n are integers such that 2 ≤ k_i ≤ 20 for each i. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: All test cases have been processed, and the corresponding results (either `-1` or the modified list `a` as a space-separated string) have been printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers. For each test case, it calculates a modified list where each element is the product of all other elements divided by the current element. If the sum of the modified list is greater than or equal to the original product, it outputs `-1`. Otherwise, it outputs the modified list as a space-separated string.

