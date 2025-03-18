#State of the program right berfore the function call: a and b are positive integers.
def func_1(a, b):
    return a * b // gcd(a, b)
    #The program returns the least common multiple (LCM) of the positive integers 'a' and 'b'.
#Overall this is what the function does:The function `func_1` accepts two positive integers `a` and `b` and returns their least common multiple (LCM). The LCM is the smallest positive integer that is divisible by both `a` and `b`. After the function concludes, the input variables `a` and `b` remain unchanged, and the function returns the LCM of `a` and `b`.

#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 50, and vals is a list of N integers such that 2 ≤ vals[i] ≤ 20 for all 0 ≤ i < N.
def func_2():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: `N` is an input integer such that 1 ≤ N ≤ 50, `vals` is a list of N integers such that 2 ≤ `vals[i]` ≤ 20 for all 0 ≤ i < N, `den` is the result of applying `func_1` to all elements of `vals` sequentially, starting with `vals[0]` as the initial value.
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing.
    #State: `N` is an input integer such that 1 ≤ N ≤ 50, `vals` is a list of N integers such that 2 ≤ `vals[i]` ≤ 20 for all 0 ≤ i < N, `den` is the result of applying `func_1` to all elements of `vals` sequentially, starting with `vals[0]` as the initial value, `vprod` is a list of N integers where each element is `den` divided by the corresponding element in `vals` (using integer division), `den` is now `den` minus the sum of `vprod`, and `den` is greater than 0.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: - The `print` statement will print the elements of `vprod` separated by spaces.
    #   - The elements of `vprod` are the integer divisions of `den` by each element in `vals`.
    #
    #Given the precondition and the steps above, the output will be the elements of `vprod` separated by spaces. Since the exact values of `vals` are not provided, we can describe the output in terms of the elements of `vprod`.
    #
    #Output:
#Overall this is what the function does:The function `func_2` reads an integer `N` and a list of `N` integers `vals` from the user input. It then applies a function `func_1` to all elements of `vals` sequentially, starting with `vals[0]` as the initial value, and stores the result in `den`. It computes a list `vprod` where each element is the integer division of `den` by the corresponding element in `vals`. The function then subtracts the sum of `vprod` from `den`. If the resulting `den` is less than or equal to 0, the function prints `-1` and returns. Otherwise, it prints the elements of `vprod` separated by spaces. The function does not accept any parameters and returns nothing.

