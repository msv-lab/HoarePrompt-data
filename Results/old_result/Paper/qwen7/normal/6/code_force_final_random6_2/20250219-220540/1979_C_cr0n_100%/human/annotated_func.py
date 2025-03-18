#State of the program right berfore the function call: a and b are integers such that 2 <= b <= 20 and 1 <= a <= 10^9.
def func_1(a, b):
    return a * b // gcd(a, b)
    #The program returns the product of a and b divided by their greatest common divisor (gcd), where 2 <= b <= 20 and 1 <= a <= 10^9.
#Overall this is what the function does:The function accepts two parameters, `a` and `b`, where `a` is an integer between 1 and 10^9, and `b` is an integer between 2 and 20. It returns the product of `a` and `b` divided by their greatest common divisor (gcd).

#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 50, and vals is a list of N integers where each integer k_i satisfies 2 ≤ k_i ≤ 20.
def func_2():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: N is an input integer, `vals` is a list of N integers, and `den` is the result of applying `func_1` successively to the elements of `vals` starting with the first element and using each subsequent element as the argument for `func_1`.
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns None
    #State: `N` is an input integer, `vals` is a list of N integers, `den` is the result of applying `func_1` successively to the elements of `vals` starting with the first element and using each subsequent element as the argument for `func_1`, `vprod` is a list of integers where each element is the result of `den` divided by the corresponding element in `vals` using integer division, `den` is updated to `den + sum(vprod)`
    print(' '.join([str(x) for x in vprod]))
    #This is printed: 2 2 1
#Overall this is what the function does:The function reads an integer N and a list of N integers from input. It then calculates a value `den` by successively applying a function `func_1` to the elements of the list. After computing a list `vprod` of integer divisions of `den` by each element in the list, it updates `den` by subtracting the sum of `vprod`. If `den` becomes non-positive, it prints `-1` and returns. Otherwise, it prints the elements of `vprod` separated by spaces and returns `None`.

