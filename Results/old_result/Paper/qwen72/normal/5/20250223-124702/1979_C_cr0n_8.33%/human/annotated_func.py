#State of the program right berfore the function call: t is an integer (1 ≤ t ≤ 10^4) representing the number of test cases, n is an integer (1 ≤ n ≤ 50) representing the number of outcomes for each test case, and k is a list of n integers (2 ≤ k_i ≤ 20) representing the multipliers for each outcome.
def func_1():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
        
    #State: `t` is an integer (1 ≤ t ≤ 10^4), `n` is an integer (1 ≤ n ≤ 50), `k` is a list of n integers (2 ≤ k_i ≤ 20), `N` is an input integer, `vals` is a list of integers read from input, `prod` is the product of all integers in `vals`.
    vprod = [(prod // r) for r in vals]
    den = prod - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing.
    #State: `t` is an integer (1 ≤ t ≤ 10^4), `n` is an integer (1 ≤ n ≤ 50), `k` is a list of n integers (2 ≤ k_i ≤ 20), `N` is an input integer, `vals` is a list of integers read from input, `prod` is the product of all integers in `vals`, `vprod` is a list where each element is the product of all integers in `vals` except the corresponding integer in `vals`, `den` is the value of `prod - sum(vprod)`, and `den` is greater than 0.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: vprod (where vprod is a list of integers, each element being the product of all integers in vals except the corresponding integer in vals)
#Overall this is what the function does:The function reads an integer `N` and a list of integers `vals` from the user input. It calculates the product of all integers in `vals` and then computes a list `vprod` where each element is the product of all integers in `vals` except the corresponding integer. It also calculates `den` as the difference between the product of all integers in `vals` and the sum of the elements in `vprod`. If `den` is less than or equal to 0, the function prints `-1` and returns. Otherwise, it prints the elements of `vprod` separated by spaces. The function does not accept any parameters and returns nothing.

