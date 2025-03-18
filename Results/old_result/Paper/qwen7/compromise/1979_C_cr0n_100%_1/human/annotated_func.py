#State of the program right berfore the function call: a and b are positive integers such that 1 <= a, b <= 20.
def func_1(a, b):
    return a * b // gcd(a, b)
    #The program returns the product of a and b divided by their greatest common divisor (gcd), where both a and b are positive integers between 1 and 20 inclusive.
#Overall this is what the function does:The function accepts two positive integers `a` and `b` (both between 1 and 20 inclusive) and returns their product divided by their greatest common divisor (gcd).

#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 50, and vals is a list of N integers where each integer k_i satisfies 2 ≤ k_i ≤ 20.
def func_2():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: Output State: `den` is the result of successively applying `func_1` to the initial value `den` and each element in the list `vals`.
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program does not return any value since there is no return statement in the provided code.
    #State: `den` is the result of `den - sum(vprod)`, `vprod` remains unchanged, and `den` is greater than 0
    print(' '.join([str(x) for x in vprod]))
    #This is printed: what is printed (where the printed content is the elements of vprod joined by spaces)
#Overall this is what the function does:The function reads two lines of input: the first line contains an integer \(N\) representing the size of the list, and the second line contains \(N\) space-separated integers. It then calculates a value `den` by successively applying a function `func_1` to the initial value of the first list element and each subsequent element. Afterward, it computes a list `vprod` where each element is `den` divided by the corresponding element in the original list, truncating the division result. The function then subtracts the sum of `vprod` from `den`. If `den` is less than or equal to 0, it prints `-1` and terminates without returning any value. Otherwise, it prints the elements of `vprod` joined by spaces.

