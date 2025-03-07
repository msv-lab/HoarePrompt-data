#State of the program right berfore the function call: a and b are integers such that 2 <= b <= 20 and 1 <= a <= 10^9.
def func_1(a, b):
    return a * b // gcd(a, b)
    #The program returns the product of a and b divided by their greatest common divisor (gcd), where 2 <= b <= 20 and 1 <= a <= 10^9.
#Overall this is what the function does:The function accepts two parameters, `a` and `b`, where `a` is an integer between 1 and 10^9, and `b` is an integer between 2 and 20. It returns the result of the product of `a` and `b` divided by their greatest common divisor (gcd).

#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 50, and vals is a list of N integers where each integer k_i satisfies 2 ≤ k_i ≤ 20.
def func_2():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: Output State: `den` is equal to the result of applying the function `func_1` iteratively `N` times to the initial value `den`, with each application using the next element from the list `vals`.
    #
    #In simpler terms, after the loop has executed all its iterations, `den` will be the final result of successively applying the function `func_1` to `den` starting with the first element of `vals`, then the second, and so on, until all `N` elements of `vals` have been used.
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program does not return anything since there is no return statement in the code.
    #State: `den` is equal to `den - sum(vprod)`, and `den` is greater than 0
    print(' '.join([str(x) for x in vprod]))
    #This is printed: " ".join([str(x) for x in vprod]) (where vprod is a list of elements whose string representations are joined with spaces)
#Overall this is what the function does:The function reads an integer N and a list of N integers from the input. It then iteratively applies a function `func_1` to an initial value `den` using each element from the list `vals`. After the iterations, it calculates a new list `vprod` where each element is `den` divided by the corresponding element in `vals`. It subtracts the sum of `vprod` from `den`. If `den` is less than or equal to 0, it prints `-1` and does not return anything. Otherwise, it prints the elements of `vprod` separated by spaces.

