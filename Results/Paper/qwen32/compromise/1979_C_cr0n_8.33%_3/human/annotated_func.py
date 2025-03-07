#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, each test case consists of an integer n such that 1 <= n <= 50, and a list of n integers k_1, k_2, ..., k_n where 2 <= k_i <= 20 for each i. The sum of n over all test cases does not exceed 2 * 10^5.
def func_1():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
        
    #State: `t` is an integer such that 1 <= t <= 10^4, each test case consists of an integer n such that 1 <= n <= 50, and a list of n integers k_1, k_2, ..., k_n where 2 <= k_i <= 20 for each i. The sum of n over all test cases does not exceed 2 * 10^5. `N` is an integer read from the input. `vals` is a list of integers read from the input. `prod` is the product of all integers in `vals`.
    vprod = [(prod // r) for r in vals]
    den = prod - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns None
    #State: `t` is an integer such that 1 <= t <= 10^4, each test case consists of an integer n such that 1 <= n <= 50, and a list of n integers k_1, k_2, ..., k_n where 2 <= k_i <= 20 for each i. The sum of n over all test cases does not exceed 2 * 10^5. `N` is an integer read from the input. `vals` is a list of integers read from the input. `prod` is the product of all integers in `vals`. `vprod` is a list where each element is `prod` divided by the corresponding element in `vals`. `den` is `prod - sum(vprod)`, and `den` is greater than 0.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: [space-separated values of vprod where each value is prod divided by the corresponding element in vals]
#Overall this is what the function does:The function reads an integer `N` and a list of integers `vals` from the input, calculates the product of all integers in `vals`, and then computes a new list `vprod` where each element is the product divided by the corresponding element in `vals`. It then calculates a denominator `den` as the product minus the sum of `vprod`. If `den` is less than or equal to 0, it prints `-1`. Otherwise, it prints the elements of `vprod` as space-separated values. The function returns `None`.

