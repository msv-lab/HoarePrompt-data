#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, each test case contains a positive integer n such that 1 ≤ n ≤ 50, and a list of n integers k_1, k_2, ..., k_n where 2 ≤ k_i ≤ 20 for all 1 ≤ i ≤ n. Additionally, the sum of n over all test cases does not exceed 2 × 10^5.
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
        
    #State: Output State: After the loop executes all its iterations, `i` will be equal to `bets`, `sumo` will be the sum of `int(a[j])` for all `j` where `0 <= j < bets`, `bets` will be the number of bets entered, and `a[i]` will be updated to `prod // a[i]` for each `i` from 0 to `bets-1`. If `sumo` is greater than or equal to `prod`, then `sumo` remains unchanged. Otherwise, `ans` will contain the string representations of all elements in `a` separated by spaces, and `ans` will be printed. The variable `prod` will hold the product of the first `bets` elements in the list `a`.
    #
    #In simpler terms, after all iterations of the loop, `i` will be equal to the number of bets (`bets`), `sumo` will be the sum of the modified elements in the list `a` (each element divided by the product of all elements in the list), and `ans` will contain the final modified elements of `a` as a space-separated string. If the sum of these modified elements is greater than or equal to the initial product, `sumo` will retain its value; otherwise, `ans` will be printed.
#Overall this is what the function does:The function processes multiple test cases, each containing a positive integer `n` and a list of `n` integers `k_1, k_2, ..., k_n`. For each test case, it calculates the product of the first `n` integers, modifies each integer in the list by dividing the product by the respective integer, and computes the sum of these modified integers. If the sum is greater than or equal to the initial product, it prints `-1`; otherwise, it prints the modified integers as a space-separated string.

