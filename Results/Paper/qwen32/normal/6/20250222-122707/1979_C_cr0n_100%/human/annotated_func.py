#State of the program right berfore the function call: a and b are integers greater than or equal to 1.
def func_1(a, b):
    return a * b // gcd(a, b)
    #The program returns the least common multiple (LCM) of integers `a` and `b`
#Overall this is what the function does:The function accepts two integers `a` and `b`, both greater than or equal to 1, and returns their least common multiple (LCM).

#State of the program right berfore the function call: N is an integer representing the number of outcomes, and vals is a list of integers representing the multipliers for each outcome, where 1 <= N <= 50 and 2 <= k_i <= 20 for each k_i in vals.
def func_2():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: N is an integer representing the number of outcomes, vals is a list of integers, and den is the value returned by applying func_1 cumulatively to all elements in vals starting with den = vals[0].
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing.
    #State: `N` is an integer representing the number of outcomes, `vals` is a list of integers, `den` is the value returned by applying `func_1` cumulatively to all elements in `vals` starting with `den = vals[0]` minus the sum of `vprod`, and `vprod` is a list where each element is `den // r` for each `r` in `vals`. Additionally, `den` is greater than 0.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: den // vals[0] den // vals[1] den // vals[2] ... den // vals[N-1] (where den is the cumulative result of applying func_1 to all elements in vals starting with den = vals[0] and then subtracting the sum of vprod, and vprod is a list of den // r for each r in vals)
#Overall this is what the function does:The function `func_2` reads an integer `N` and a list of integers `vals` from the input. It calculates a cumulative value `den` by applying a function `func_1` cumulatively to the elements of `vals`. It then computes a list `vprod` where each element is the integer division of `den` by each element in `vals`. The function subtracts the sum of `vprod` from `den`. If the resulting `den` is less than or equal to 0, it prints `-1`. Otherwise, it prints the elements of `vprod` separated by spaces. The function does not return any value.

