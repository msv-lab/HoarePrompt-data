#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 50, and k_i is an integer such that 2 ≤ k_i ≤ 20 for all 1 ≤ i ≤ n.
def func_1():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
        
    #State: Output State: `t` is a positive integer such that \(1 \leq t \leq 10^4\), `N` is an input integer such that \(1 \leq N \leq 50\), `vals` is a list of integers obtained from the input split and converted to integers, `prod` is the product of all elements in `vals`, `r` is the last element of `vals`.
    #
    #In this final output state, `t` and `N` remain unchanged as they are not affected by the loop. The `vals` list contains all the original integers that were processed. The variable `prod` has been updated to hold the cumulative product of all elements in `vals`. The variable `r` holds the value of the last element in `vals` since it is reassigned in each iteration of the loop.
    vprod = [(prod // r) for r in vals]
    den = prod - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns None
    #State: `t` is a positive integer such that \(1 \leq t \leq 10^4\), `N` is an input integer such that \(1 \leq N \leq 50\), `vals` is a list of integers obtained from the input split and converted to integers, `prod` is the product of all elements in `vals`, `r` is the last element of `vals`, `vprod` is a list where each element is the product of `prod` divided by each element `r` in `vals` (excluding the last element), `den` is `prod - sum(vprod)`, and `den` is greater than 0
    print(' '.join([str(x) for x in vprod]))
    #This is printed: 
#Overall this is what the function does:The function reads two inputs: the number of test cases `N` and a list of integers `vals`. It calculates the product of all integers in `vals` and then computes a new list `vprod` where each element is the product of all elements in `vals` divided by the corresponding element in `vals` (excluding the last element). It also calculates `den` as the difference between the product and the sum of `vprod`. If `den` is less than or equal to zero, it prints `-1` and returns. Otherwise, it prints the elements of `vprod` separated by spaces. The function does not accept any parameters and does not return any value.

