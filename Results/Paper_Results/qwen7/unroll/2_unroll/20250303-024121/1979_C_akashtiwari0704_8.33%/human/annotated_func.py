#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 50, and k is a list of n integers where 2 ≤ k_i ≤ 20 for all 1 ≤ i ≤ n.
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
        
    #State: After executing the loop, `t` will be decremented by 1 for each iteration, `bets` and `a` will be updated based on the calculations inside the loop, and `prod` and `sumo` will be recalculated for each test case. The final output will consist of either -1 or a space-separated list of integers for each test case, with `t` representing the number of such outputs.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads the number of bets (`bets`), a list of integers (`a`), calculates the product of the list elements (`prod`), and then updates each element in the list by dividing `prod` by the respective element and summing these updated values (`sumo`). If the sum of the updated list is greater than or equal to the original product, it prints `-1`; otherwise, it prints the updated list as a space-separated string. The function handles up to 10,000 test cases, with each test case containing up to 50 integers in the list, where each integer is between 2 and 20 inclusive.

