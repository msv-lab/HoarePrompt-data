#State of the program right berfore the function call: a and b are integers greater than or equal to 1.
def func_1(a, b):
    return a * b // gcd(a, b)
    #The program returns the least common multiple (LCM) of integers 'a' and 'b'
#Overall this is what the function does:The function accepts two integers `a` and `b`, both greater than or equal to 1, and returns their least common multiple (LCM).

#State of the program right berfore the function call: N is an integer representing the number of outcomes (1 <= N <= 50), vals is a list of integers representing the multipliers for each outcome (2 <= k_i <= 20 for each k_i in vals).
def func_2():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: N is the integer value provided by the input (1 <= N <= 50); vals is a list of integers obtained from the input where each integer is between 2 and 20 inclusive; den is the result of applying func_1 successively to all elements of vals in sequence.
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns None
    #State: `N` is the integer value provided by the input (1 <= N <= 50); `vals` is a list of integers obtained from the input where each integer is between 2 and 20 inclusive; `den` is the result of applying `func_1` successively to all elements of `vals` in sequence, minus the sum of `vprod`; `vprod` is a list of integers where each element is the result of `den` divided by the corresponding element in `vals`; `den` is greater than 0.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: [vprod[0] vprod[1] ... vprod[N-1]] (where vprod[i] is the integer division of den by vals[i])
#Overall this is what the function does:The function `func_2` reads an integer `N` and a list of integers `vals` from the input. It processes these inputs to compute a list `vprod` where each element is the result of dividing a computed denominator `den` by the corresponding element in `vals`. If the final `den` is less than or equal to zero, it prints `-1`. Otherwise, it prints the elements of `vprod` as a space-separated string. The function returns `None`.

