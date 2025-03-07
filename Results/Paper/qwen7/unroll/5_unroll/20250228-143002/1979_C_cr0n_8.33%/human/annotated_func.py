#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 50, and k is a list of n positive integers where 2 ≤ k_i ≤ 20.
def func_1():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
        
    #State: prod is the product of all elements in the list vals, t remains unchanged, N remains unchanged.
    vprod = [(prod // r) for r in vals]
    den = prod - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program does not return any value since there is no return statement in the provided code snippet.
    #State: `vprod` is a list where each element is the value of `prod` divided by each corresponding element in `vals`, `t` remains unchanged, `N` remains unchanged, `den` is `prod - sum(vprod)`, and `den` is greater than 0
    print(' '.join([str(x) for x in vprod]))
    #This is printed: [prod/vals[0]], [prod/vals[1]], [prod/vals[2]], ... (where each element in vprod is prod divided by the corresponding element in vals)
#Overall this is what the function does:The function reads a positive integer N and a list of N positive integers from input. It calculates the product of all elements in the list and then computes a new list where each element is the product of all elements divided by the corresponding element in the original list. If the denominator (product minus the sum of the new list) is less than or equal to zero, it prints -1 and stops. Otherwise, it prints the new list. The function does not return any value.

