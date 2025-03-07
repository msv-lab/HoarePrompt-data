#State of the program right berfore the function call: a and b are integers greater than or equal to 1.
def func_1(a, b):
    return a * b // gcd(a, b)
    #The program returns the least common multiple (LCM) of integers 'a' and 'b'.
#Overall this is what the function does:The function accepts two integer parameters `a` and `b`, both of which are greater than or equal to 1, and returns their least common multiple (LCM).

#State of the program right berfore the function call: N is an integer representing the number of outcomes such that 1 <= N <= 50, vals is a list of integers where each integer k_i represents the multiplier for the i-th outcome such that 2 <= k_i <= 20, and the length of vals is equal to N.
def func_2():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: N is the integer value provided by the user input, vals is a list of integers where each integer k_i represents the multiplier for the i-th outcome such that 2 <= k_i <= 20, and the length of vals is equal to N, with vals now holding the specific integers read from the input; den is the product of all elements in vals.
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns None
    #State: `N` is the integer value provided by the user input, `vals` is a list of integers where each integer \( k_i \) represents the multiplier for the i-th outcome such that \( 2 \leq k_i \leq 20 \), and the length of `vals` is equal to `N`, with `vals` now holding the specific integers read from the input; `den` is the product of all elements in `vals` minus the sum of `vprod`; `vprod` is a list where each element is `den // r` for each `r` in `vals`; `den` is greater than 0.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: vprod (where vprod is a list of integers calculated as den // r for each r in vals)
#Overall this is what the function does:The function `func_2` reads an integer `N` and a list `vals` of integers from the user, calculates a product of all elements in `vals`, then computes a list `vprod` where each element is the product divided by each respective element in `vals`. It then subtracts the sum of `vprod` from the product. If the result is less than or equal to zero, it prints `-1`. Otherwise, it prints the elements of `vprod` as a space-separated string. The function returns `None`.

