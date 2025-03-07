#State of the program right berfore the function call: a and b are positive integers.
def func_1(a, b):
    return a * b // gcd(a, b)
    #The program returns the least common multiple (LCM) of the positive integers 'a' and 'b'.
#Overall this is what the function does:The function `func_1` accepts two positive integers `a` and `b`, and returns their least common multiple (LCM). The input variables `a` and `b` are not modified by the function.

#State of the program right berfore the function call: N is an integer representing the number of outcomes, and vals is a list of integers where each element is a multiplier (k_i) for the i-th outcome, such that 1 <= N <= 50 and 2 <= vals[i] <= 20 for all 0 <= i < N.
def func_2():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
        
    #State: N is an input integer, `vals` is a list of integers where each element is a multiplier (k_i) for the i-th outcome, such that 1 <= N <= 50 and 2 <= vals[i] <= 20 for all 0 <= i < N, `den` is the result of applying `func_1` to the initial value of `den` and each element of `vals` in sequence.
    vprod = [(den // r) for r in vals]
    den = den - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns without any value, as the return statement is empty.
    #State: N is an input integer, `vals` is a list of integers where each element is a multiplier (k_i) for the i-th outcome, such that 1 <= N <= 50 and 2 <= vals[i] <= 20 for all 0 <= i < N, `den` is the result of applying `func_1` to the initial value of `den` and each element of `vals` in sequence, `vprod` is a list of integers where each element is the result of `den` divided by the corresponding element in `vals` (using integer division), `den` is now `den` minus the sum of all elements in `vprod`, and `den` is greater than 0.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: vprod (where vprod is a list of integers, each element being the result of den divided by the corresponding element in vals using integer division)
#Overall this is what the function does:The function `func_2` reads an integer `N` and a list of integers `vals` from user input. It then computes a value `den` by applying a function `func_1` to the initial value of `den` (which is the first element of `vals`) and each element of `vals` in sequence. It calculates a list `vprod` where each element is the result of `den` divided by the corresponding element in `vals` using integer division. The function then updates `den` by subtracting the sum of all elements in `vprod` from it. If the updated `den` is less than or equal to 0, the function prints `-1` and returns without any value. Otherwise, it prints the elements of `vprod` separated by spaces and returns without any value.

