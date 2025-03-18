#State of the program right berfore the function call: a and b are positive integers.
def func_1(a, b):
    return a * b // gcd(a, b)
    #The program returns the least common multiple (LCM) of the positive integers a and b.
#Overall this is what the function does:The function `func_1` accepts two positive integers `a` and `b`, and returns their least common multiple (LCM). After the function concludes, the input variables `a` and `b` remain unchanged, and the program state is as it was before the function call, with the exception of the returned LCM value.

#State of the program right berfore the function call: N is a positive integer (1 ≤ N ≤ 50), and vals is a list of N integers where each integer k_i satisfies (2 ≤ k_i ≤ 20).
def func_2():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: `N` is an input integer (1 ≤ N ≤ 50), `vals` is a list of N integers where each integer `k_i` satisfies (2 ≤ `k_i` ≤ 20), `den` is the result of applying `func_1` to the initial `den` and all elements in `vals` sequentially, and `vals` has exactly N elements.
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns without any specific value.
    #State: `N` is an input integer (1 ≤ N ≤ 50), `vals` is a list of N integers where each integer `k_i` satisfies (2 ≤ `k_i` ≤ 20), `den` is the result of `den - sum(vprod)`, `vprod` is a list of N integers where each element is `(den // r)` for each `r` in `vals`, and `den` is greater than 0.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: - The `print` statement will output the elements of `vprod` as a space-separated string.
    #   - Each element in `vprod` is the integer division of `den` by the corresponding element in `vals`.
    #
    #Given the initial state and the code, the output will be a space-separated string of the integer divisions of `den` by each element in `vals`.
    #
    #Output:
#Overall this is what the function does:The function `func_2` takes an implied input of a positive integer `N` (1 ≤ N ≤ 50) and a list `vals` of `N` integers (2 ≤ k_i ≤ 20). It calculates a value `den` by applying a function `func_1` to the elements of `vals` sequentially. It then computes a list `vprod` where each element is the integer division of `den` by the corresponding element in `vals`. If the final value of `den` after subtracting the sum of `vprod` is less than or equal to 0, the function prints `-1` and returns without any specific value. Otherwise, it prints the elements of `vprod` as a space-separated string and returns without any specific value.

