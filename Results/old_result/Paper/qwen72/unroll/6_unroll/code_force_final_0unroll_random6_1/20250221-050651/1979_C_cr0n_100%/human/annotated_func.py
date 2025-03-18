#State of the program right berfore the function call: a and b are positive integers.
def func_1(a, b):
    return a * b // gcd(a, b)
    #The program returns the least common multiple (LCM) of the positive integers 'a' and 'b'.
#Overall this is what the function does:The function `func_1` accepts two positive integers `a` and `b`, and returns their least common multiple (LCM). The input variables `a` and `b` remain unchanged after the function call.

#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 50, and vals is a list of N integers such that 2 ≤ vals[i] ≤ 20 for all 0 ≤ i < N.
def func_2():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: `den` is the GCD of all integers in `vals`, `vals` remains unchanged, `N` remains unchanged.
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing.
    #State: *`den` is updated to `den - sum(vprod)`, `vals` remains unchanged, `N` remains unchanged, `vprod` is a list where each element is the result of `den` (before the update) divided by the corresponding element in `vals`. Additionally, `den` is greater than 0 after the update.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: `den_initial / vals[0] den_initial / vals[1] ... den_initial / vals[N-1]` (where `den_initial` is the initial value of `den` and `vals` is the list of values)
#Overall this is what the function does:The function `func_2` reads an integer `N` and a list of `N` integers `vals` from the user. It calculates the greatest common divisor (GCD) of all integers in `vals` and stores it in `den`. It then computes a list `vprod` where each element is the result of `den` divided by the corresponding element in `vals`. The function updates `den` to `den - sum(vprod)`. If the updated `den` is less than or equal to 0, the function prints `-1` and returns. Otherwise, it prints the elements of `vprod` separated by spaces. The function does not return any value. The final state of the program is that `den` is updated, `vals` remains unchanged, and `N` remains unchanged.

