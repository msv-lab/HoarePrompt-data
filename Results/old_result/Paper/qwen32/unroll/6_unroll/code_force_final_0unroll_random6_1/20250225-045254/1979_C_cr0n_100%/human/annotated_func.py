#State of the program right berfore the function call: a and b are integers greater than or equal to 1.
def func_1(a, b):
    return a * b // gcd(a, b)
    #The program returns the least common multiple of `a` and `b`
#Overall this is what the function does:The function takes two integer parameters `a` and `b`, both greater than or equal to 1, and returns their least common multiple.

#State of the program right berfore the function call: N is an integer representing the number of outcomes, and vals is a list of integers where each element is a multiplier (k_i) for the corresponding outcome such that 2 <= k_i <= 20.
def func_2():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: N is the integer value input by the user, vals is a list of integers, den is the product of all elements in vals.
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns None.
    #State: `N` is the integer value input by the user, `vals` is a list of integers, `den` is the product of all elements in `vals` minus the sum of `vprod`, `vprod` is a list where each element is `den` divided by the corresponding element in `vals`. `den` is greater than 0.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: [den/v1] [den/v2] ... [den/vk] (where den = prod_vals / (1 + (1/v1 + 1/v2 + ... + 1/vk)) and vprod[i] = den / vals[i])
#Overall this is what the function does:The function `func_2` reads an integer `N` and a list of integers `vals` from the user input. It calculates a value `den` as the product of all elements in `vals`, then computes a list `vprod` where each element is `den` divided by the corresponding element in `vals`. It adjusts `den` by subtracting the sum of `vprod`. If the adjusted `den` is less than or equal to zero, it prints `-1`. Otherwise, it prints the elements of `vprod` as a space-separated string. The function returns `None`.

