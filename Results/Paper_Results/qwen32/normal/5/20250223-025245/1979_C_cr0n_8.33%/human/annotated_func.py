#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 50, and k is a list of n integers where each k_i satisfies 2 ≤ k_i ≤ 20. The sum of n over all test cases does not exceed 2 * 10^5.
def func_1():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; for each test case, `n` is an integer such that 1 ≤ n ≤ 50, and `k` is a list of `n` integers where each `k_i` satisfies 2 ≤ `k_i` ≤ 20; `N` is an input integer; `vals` is a list of integers derived from the input and must have at least `N` elements; `prod` is the product of all elements in `vals`.
    vprod = [(prod // r) for r in vals]
    den = prod - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing (None)
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; for each test case, `n` is an integer such that 1 ≤ n ≤ 50, and `k` is a list of `n` integers where each `k_i` satisfies 2 ≤ `k_i` ≤ 20; `N` is an input integer; `vals` is a list of integers derived from the input and must have at least `N` elements; `prod` is the product of all elements in `vals`; `vprod` is a list where each element is the integer division of `prod` by the corresponding element in `vals`; `den` is `prod - sum(vprod)`, and `den` is greater than 0
    print(' '.join([str(x) for x in vprod]))
    #This is printed: vprod (where vprod is a list of integers where each element is the integer division of prod by the corresponding element in vals)
#Overall this is what the function does:The function `func_1` reads an integer `N` and a list of `N` integers from the input. It calculates the product of these integers and then computes a new list where each element is the result of dividing the product by the corresponding integer in the input list. It then calculates a denominator as the difference between the product and the sum of the new list. If the denominator is less than or equal to zero, it prints `-1`. Otherwise, it prints the new list of integers. The function does not return any value.

