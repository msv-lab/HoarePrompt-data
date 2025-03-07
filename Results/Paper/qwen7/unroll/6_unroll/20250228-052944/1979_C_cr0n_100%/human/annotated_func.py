#State of the program right berfore the function call: a and b are positive integers such that 2 <= b <= 20 and 1 <= a <= 10^9.
def func_1(a, b):
    return a * b // gcd(a, b)
    #The program returns the product of a and b divided by their greatest common divisor (gcd), where 2 <= b <= 20 and 1 <= a <= 10^9.
#Overall this is what the function does:The function accepts two parameters, `a` and `b`, where both are positive integers with `2 <= b <= 20` and `1 <= a <= 10^9`. It calculates the greatest common divisor (gcd) of `a` and `b`, then returns the result of dividing the product of `a` and `b` by their gcd.

#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 50, and vals is a list of N integers where each integer k_i satisfies 2 ≤ k_i ≤ 20.
def func_2():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: Output State: `den` is the result of successively applying `func_1` to the first element of `vals` and each subsequent element in `vals`.
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns None
    #State: `vprod` is a list where each element is the result of `den` divided by each corresponding element in `vals`, and `den` is the result of successively applying `func_1` to the first element of `vals` and each subsequent element in `vals`; `den` is updated to `den - sum(vprod)`, and `den` is greater than 0
    print(' '.join([str(x) for x in vprod]))
    #This is printed: - The output will be a space-separated string of the elements in `vprod`, each converted to a string.
    #
    #Given the above analysis, the output will be a space-separated string of the elements in `vprod`.
    #
    #Output:
#Overall this is what the function does:The function reads two lines of input: the first line contains an integer \(N\) representing the number of elements in the list, and the second line contains \(N\) integers. It then calculates a value `den` by successively applying a function `func_1` to the first element of the list and each subsequent element. After that, it computes a list `vprod` where each element is the result of `den` divided by each corresponding element in the original list. It updates `den` by subtracting the sum of `vprod`. If `den` becomes less than or equal to zero, it prints `-1` and returns. Otherwise, it prints the elements of `vprod` as a space-separated string and returns `None`.

