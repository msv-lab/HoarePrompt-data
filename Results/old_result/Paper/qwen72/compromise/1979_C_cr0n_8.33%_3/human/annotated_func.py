#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 50, and k is a list of n integers where each integer k_i satisfies 2 ≤ k_i ≤ 20.
def func_1():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 50, `k` is a list of n integers where each integer k_i satisfies 2 ≤ k_i ≤ 20, `N` is an input integer, `vals` is a list of integers read from the input, `prod` is the product of all integers in the list `vals`.
    vprod = [(prod // r) for r in vals]
    den = prod - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing, as the return statement is empty.
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 50, `k` is a list of n integers where each integer k_i satisfies 2 ≤ k_i ≤ 20, `N` is an input integer, `vals` is a list of integers read from the input, `prod` is the product of all integers in the list `vals`, `vprod` is a list of integers where each element is the result of `prod` divided by the corresponding element in `vals`, `den` is the result of `prod` minus the sum of all elements in `vprod`, and `den` is greater than 0.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: 12 8 6
#Overall this is what the function does:The function `func_1` reads an integer `N` and a list of integers `vals` from the user input. It calculates the product of all integers in `vals` and then computes a list `vprod` where each element is the product divided by the corresponding element in `vals`. It also calculates `den` as the product minus the sum of the elements in `vprod`. If `den` is less than or equal to 0, the function prints `-1` and returns. Otherwise, it prints the elements of `vprod` separated by spaces and returns without any value. The function does not accept any parameters and does not return any value.

