#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 50, and k is a list of n integers such that 2 ≤ k_i ≤ 20 for each i. The sum of n over all test cases does not exceed 2 * 10^5.
def func_1():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is an integer such that 1 ≤ n ≤ 50; `k` is a list of `n` integers such that 2 ≤ k_i ≤ 20 for each i; `N` is an input integer; `vals` is a list of integers derived from the input; `prod` is the product of all elements in `vals`.
    vprod = [(prod // r) for r in vals]
    den = prod - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing (None)
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is an integer such that 1 ≤ n ≤ 50; `k` is a list of `n` integers such that 2 ≤ k_i ≤ 20 for each i; `N` is an input integer; `vals` is a list of integers derived from the input; `prod` is the product of all elements in `vals`; `vprod` is a list where each element is `prod // vals[i]` for each index `i` in `vals`; `den` is `prod - sum(vprod)`; and `den` is greater than 0.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: [vprod[0] vprod[1] ... vprod[m-1]] (where each vprod[i] is the product of all elements in vals except vals[i])
#Overall this is what the function does:The function reads an integer `N` and a list of integers `vals` from the input, calculates the product of all elements in `vals`, and then computes a new list `vprod` where each element is the product of all elements in `vals` except the corresponding element. It then calculates `den` as the difference between the product and the sum of `vprod`. If `den` is less than or equal to zero, it prints `-1`. Otherwise, it prints the elements of `vprod` as a space-separated string. The function returns nothing (None).

