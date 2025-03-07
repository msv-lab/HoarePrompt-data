#State of the program right berfore the function call: a and b are integers greater than 0.
def func_1(a, b):
    return a * b // gcd(a, b)
    #The program returns the least common multiple (LCM) of integers a and b
#Overall this is what the function does:The function accepts two positive integers `a` and `b` and returns their least common multiple (LCM).

#State of the program right berfore the function call: N is an integer representing the number of outcomes (1 <= N <= 50), vals is a list of integers representing the multipliers for each outcome (2 <= k_i <= 20 for each k_i in vals).
def func_2():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: - `N` remains unchanged.
    #- `vals` remains unchanged.
    #- `den` is the product of all elements in `vals`.
    #
    #Output State:
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing.
    #State: `N` remains unchanged; `vals` remains unchanged; `den` is the product of all elements in `vals` minus the sum of `vprod`; `vprod` is a list where each element is `den // r` for the corresponding `r` in `vals`; `den` is greater than 0.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: [space-separated values of vprod] (where vprod is a list where each element is den // r for the corresponding r in vals)
#Overall this is what the function does:The function `func_2` reads an integer `N` and a list of integers `vals`. It calculates the product of all elements in `vals` and then computes a new list `vprod` where each element is the product divided by the corresponding element in `vals`. It subtracts the sum of `vprod` from the product. If the result is less than or equal to zero, it prints `-1`. Otherwise, it prints the elements of `vprod` as space-separated values. The function does not return any value.

