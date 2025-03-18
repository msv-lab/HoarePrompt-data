#State of the program right berfore the function call: a and b are integers greater than 0.
def func_1(a, b):
    return a * b // gcd(a, b)
    #The program returns the least common multiple (LCM) of integers 'a' and 'b'
#Overall this is what the function does:The function accepts two positive integers `a` and `b` and returns their least common multiple (LCM).

#State of the program right berfore the function call: N is an integer representing the number of outcomes, and vals is a list of integers representing the multipliers for the amount of coins if the corresponding outcome turns out to be winning. Each element in vals is an integer such that 2 <= vals[i] <= 20.
def func_2():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: N is an integer representing the number of outcomes, vals is a list of integers where each integer is a multiplier for the amount of coins if the corresponding outcome turns out to be winning, and den is the value returned by applying func_1 iteratively to the initial den (which is vals[0]) and each subsequent element in vals.
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns None.
    #State: N is an integer representing the number of outcomes, vals is a list of integers where each integer is a multiplier for the amount of coins if the corresponding outcome turns out to be winning, den is the value returned by applying func_1 iteratively to the initial den (which is vals[0]) and each subsequent element in vals minus the sum of vprod, vprod is a list of integers where each element is the result of den // r for r in vals, and den is greater than 0.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: [space-separated values of vprod] (where each value is the result of den // r for r in vals)
#Overall this is what the function does:The function `func_2` reads an integer `N` and a list of integers `vals`. It calculates a value `den` by iteratively applying `func_1` to the elements of `vals`. It then computes a list `vprod` where each element is the integer division of `den` by the corresponding element in `vals`. It subtracts the sum of `vprod` from `den`. If `den` is less than or equal to zero, it prints `-1`. Otherwise, it prints the elements of `vprod` as space-separated values. The function does not accept any parameters and always returns `None`.

