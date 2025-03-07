#State of the program right berfore the function call: a and b are positive integers.
def func_1(a, b):
    return a * b // gcd(a, b)
    #The program returns the result of the integer division of the product of `a` and `b` by their greatest common divisor (gcd). Since `a` and `b` are positive integers, the returned value is the least common multiple (LCM) of `a` and `b`.
#Overall this is what the function does:The function `func_1` accepts two positive integers `a` and `b`, and returns their least common multiple (LCM). The LCM is calculated by performing integer division of the product of `a` and `b` by their greatest common divisor (gcd). After the function concludes, the final state of the program includes the returned LCM value.

#State of the program right berfore the function call: N is an integer such that 1 <= N <= 50, vals is a list of integers of length N where each element k_i satisfies 2 <= k_i <= 20.
def func_2():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: `den` is the greatest common divisor (GCD) of all the elements in the list `vals`. The list `vals` remains unchanged.
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: - Since the `print` statement is printing a constant value `-1`, the output will be `-1`.
        #
        #Output:
        return
        #The program returns `None`.
    #State: `den` is the greatest common divisor (GCD) of all the elements in the list `vals` minus the sum of the elements in `vprod`, `vals` remains unchanged, `vprod` is a list where each element is the result of the original `den` divided by the corresponding element in `vals`, and `den` is greater than 0.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: - The elements in `vprod` are calculated as `den / vals[i]` for each `i` in the range of `vals`.
    #   - Since `den` is the GCD of `vals`, each element in `vprod` will be an integer.
    #
    #Output:
#Overall this is what the function does:The function `func_2` reads an integer `N` and a list of `N` integers `vals` from user input. It calculates the greatest common divisor (GCD) of the elements in `vals` and then computes a list `vprod` where each element is the GCD divided by the corresponding element in `vals`. If the GCD minus the sum of the elements in `vprod` is less than or equal to zero, the function prints `-1`. Otherwise, it prints the elements of `vprod` separated by spaces. The function does not accept any parameters and always returns `None`. The list `vals` remains unchanged throughout the function's execution.

