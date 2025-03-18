#State of the program right berfore the function call: a and b are integers such that 2 <= b <= 20 and 1 <= a <= 10^9.
def func_1(a, b):
    return a * b // gcd(a, b)
    #The program returns the product of a and b divided by their greatest common divisor (gcd), where 2 <= b <= 20 and 1 <= a <= 10^9.
#Overall this is what the function does:The function accepts two parameters, `a` and `b`, where `a` is an integer between 1 and 10^9 (inclusive) and `b` is an integer between 2 and 20 (inclusive). It returns the product of `a` and `b` divided by their greatest common divisor (gcd).

#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 50, and vals is a list of N integers where each integer k_i satisfies 2 ≤ k_i ≤ 20.
def func_2():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: den is equal to the result of applying func_1 successively to the first element of vals and each subsequent element in vals.
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program does not return any value since there is no return statement in the code.
    #State: `den` is equal to `den` - sum(`vprod`), `vprod` remains unchanged, and `den` is greater than 0
    print(' '.join([str(x) for x in vprod]))
    #This is printed: what is printed
#Overall this is what the function does:The function reads two lines of input: the first line contains an integer \(N\) representing the number of elements in the list, and the second line contains \(N\) space-separated integers. It then calculates a value `den` by successively applying a function `func_1` to the first element of the list and each subsequent element. After that, it computes a list `vprod` where each element is `den` divided by the corresponding element in the input list, performs a subtraction operation on `den`, and checks if the result is less than or equal to zero. If so, it prints `-1` and terminates without returning any value. Otherwise, it prints the elements of `vprod` as a space-separated string.

