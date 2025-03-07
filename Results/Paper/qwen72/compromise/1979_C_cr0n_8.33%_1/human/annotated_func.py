#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, n is a positive integer (1 ≤ n ≤ 50) representing the number of outcomes, and k is a list of n integers (2 ≤ k_i ≤ 20) representing the multipliers for the amount of coins if the i-th outcome turns out to be winning.
def func_1():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
        
    #State: `prod` is the product of all integers in the list `vals`. The values of `t`, `N`, `n`, and `k` remain unchanged.
    vprod = [(prod // r) for r in vals]
    den = prod - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing.
    #State: `prod` is the product of all integers in the list `vals`. `vprod` is a list where each element is the result of `prod` divided by the corresponding element in `vals`. `den` is `prod` minus the sum of all elements in `vprod`. The values of `t`, `N`, `n`, and `k` remain unchanged. Additionally, `den` is greater than 0.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: - The `print` statement will print the elements of the list `vprod` as strings, separated by spaces.
    #    - Based on the initial state, `vprod` is a list where each element is the result of `prod` divided by the corresponding element in `vals`.
    #    - The exact values of `vprod` depend on the values in `vals`, but the format of the output will be the elements of `vprod` as strings, separated by spaces.
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads an integer `N` from the input, followed by a list of `N` integers `vals`. It calculates the product of all integers in `vals` and then computes a list `vprod` where each element is the result of dividing the product by the corresponding element in `vals`. It also calculates a value `den` as the product minus the sum of the elements in `vprod`. If `den` is less than or equal to 0, the function prints `-1` and returns. Otherwise, it prints the elements of `vprod` as a space-separated string. The function does not accept any parameters and does not return any value. The values of `t`, `n`, and `k` remain unchanged.

