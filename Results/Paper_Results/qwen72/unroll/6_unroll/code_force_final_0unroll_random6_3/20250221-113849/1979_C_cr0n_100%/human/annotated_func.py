#State of the program right berfore the function call: a and b are positive integers.
def func_1(a, b):
    return a * b // gcd(a, b)
    #The program returns the least common multiple (LCM) of the positive integers `a` and `b`.
#Overall this is what the function does:The function `func_1` accepts two positive integers `a` and `b`, and returns their least common multiple (LCM). The final state of the program after the function concludes is that the LCM of `a` and `b` is computed and returned.

#State of the program right berfore the function call: N is an integer such that 1 <= N <= 50, and vals is a list of N integers such that 2 <= vals[i] <= 20 for all 0 <= i < N.
def func_2():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: N remains the same, `vals` remains the same, and `den` is the greatest common divisor (GCD) of all the integers in the list `vals`.
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing.
    #State: N remains the same, `vals` remains the same, `den` is the greatest common divisor (GCD) of all the integers in the list `vals` minus the sum of `vprod`, `vprod` is a list where each element is the result of the original `den` divided by the corresponding element in `vals`, and `den` is greater than 0.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: " ".join([str(den // vals[i]) for i in range(len(vals))])
#Overall this is what the function does:The function `func_2` reads an integer `N` and a list of `N` integers from the user. It calculates the greatest common divisor (GCD) of the integers in the list. If the GCD minus the sum of the GCD divided by each integer in the list is less than or equal to zero, the function prints `-1`. Otherwise, it prints a space-separated string of the GCD divided by each integer in the list. The function does not accept any parameters and does not return any value.

