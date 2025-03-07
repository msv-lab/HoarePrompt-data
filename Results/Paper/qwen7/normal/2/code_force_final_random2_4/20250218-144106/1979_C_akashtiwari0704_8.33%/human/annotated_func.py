#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 50, and k is a list of n positive integers where 2 ≤ k_i ≤ 20 for all 1 ≤ i ≤ n.
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
        
    #State: After all iterations, `bets` is equal to the total number of iterations in the loop, `prod` is the product of all elements in the list `a` from index 0 to `bets-1`, `sumo` is the sum of the integer division of `prod` by each element in `a` for all iterations, and `ans` is a string containing the final values of `a[i]` for each `i` from 0 to `bets-1`, separated by spaces.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a positive integer `t` representing the number of cases, then for each case, it reads another positive integer `bets` and a list of `bets` positive integers. It calculates the product of all elements in the list, divides this product by each element in the list, sums these divisions, and checks if the sum is greater than or equal to the original product. If true, it prints `-1`; otherwise, it constructs a string of the modified list elements separated by spaces and prints this string.

