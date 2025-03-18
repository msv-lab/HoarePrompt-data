#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, each test case contains a positive integer n such that 1 ≤ n ≤ 50, and a list of n integers k_1, k_2, ..., k_n where 2 ≤ k_i ≤ 20 for all i. Additionally, the sum of n over all test cases does not exceed 2 × 10^5.
def func_1():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
        
    #State: `prod` is equal to the product of all elements in the original `vals` list, `t` remains a positive integer such that 1 ≤ t ≤ 10^4, `N` remains an input integer such that 1 ≤ N ≤ 50, `vals` is an empty list since all elements have been processed, and `r` is not applicable as the loop has completed.
    vprod = [(prod // r) for r in vals]
    den = prod - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program does not return any value since no return statement is provided.
    #State: `prod` is equal to the product of all elements in the original `vals` list, `t` remains a positive integer such that 1 ≤ t ≤ 10^4, `N` remains an input integer such that 1 ≤ N ≤ 50, `vals` is an empty list since all elements have been processed, `vprod` is a list containing the values of `prod // r` for each `r` in `vals`, `den` is greater than 0.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: []
#Overall this is what the function does:The function reads a positive integer `N` and a list of `N` integers `vals`. It calculates the product of all elements in `vals`, then computes a new list `vprod` where each element is the product of all elements in `vals` divided by the corresponding element in `vals`. It calculates `den` as the difference between the product and the sum of elements in `vprod`. If `den` is less than or equal to 0, it prints `-1`; otherwise, it prints the elements of `vprod` as a space-separated string. The function does not return any value.

