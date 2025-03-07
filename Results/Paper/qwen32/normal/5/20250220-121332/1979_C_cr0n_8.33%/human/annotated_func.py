#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 50, and k is a list of n integers where each k_i satisfies 2 <= k_i <= 20. The sum of n over all test cases does not exceed 2 * 10^5.
def func_1():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
        
    #State: - `prod` is the product of all elements in `vals`.
    #
    #The other variables (`t`, `n`, `k`, `N`, and `vals`) remain unchanged.
    #
    #Output State:
    vprod = [(prod // r) for r in vals]
    den = prod - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing (None)
    #State: `prod` is the product of all elements in `vals`; `vprod` is a list where each element is the result of `prod` divided by the corresponding element in `vals`; `t`, `n`, `k`, `N`, and `vals` remain unchanged; `den` is `prod - sum(vprod)` and `den` is greater than 0.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: vprod[0] vprod[1] ... vprod[len(vals)-1] (where each vprod[i] is prod / vals[i])
#Overall this is what the function does:The function `func_1` reads an integer `N` and a list of integers `vals` from the input. It calculates the product of all elements in `vals` and then computes a new list `vprod` where each element is the product divided by the corresponding element in `vals`. It also calculates `den` as the difference between the product and the sum of `vprod`. If `den` is less than or equal to zero, it prints `-1`. Otherwise, it prints the elements of `vprod` as a space-separated string. The function does not return any value.

