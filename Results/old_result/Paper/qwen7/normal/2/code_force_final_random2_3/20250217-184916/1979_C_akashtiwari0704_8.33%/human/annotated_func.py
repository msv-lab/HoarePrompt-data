#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 50. The list k contains n positive integers such that 2 ≤ k_i ≤ 20.
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
        
    #State: The output state after the loop executes all iterations is as follows:
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a positive integer `t` and a list `k` containing `n` positive integers. It calculates the product of the elements in `k`, then divides this product by each element in `k` to generate a new list. It sums the elements of this new list. If the sum is greater than or equal to the original product, it prints `-1`; otherwise, it prints the elements of the new list separated by spaces.

