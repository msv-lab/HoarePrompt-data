#State of the program right berfore the function call: n and m are integers such that 1 <= m <= cntn, where cntn is the number of permutations of length n with maximum possible value of f(p).**
def func():
    a, b = raw_input().split()
    n = int(a)
    i = int(b)
    i = i - 1
    p = range(1, n + 1)
    for k in range(1, n + 1):
        f = factorial(n - k)
        
        d = i // f
        
        print(p[d]),
        
        p.remove(p[d])
        
        i = i % f
        
    #State of the program after the  for loop has been executed: Output State: `i` is updated to the remainder of the division of `i` by `f`, `p` is an empty list, `k` is equal to `n + 1`, `f` is the factorial of 0, `d` is the result of `i` divided by `f` for the last value of `i`.
#Overall this is what the function does:The function `func` reads two integers `n` and `m` from the user input. It then calculates the number of permutations of length `n` and determines the maximum possible value of `f(p)`, denoted as `cntn`. The function iterates through a loop to calculate and print values based on certain calculations. However, the function does not accept any parameters as mentioned in the annotations, which contradicts the initial statement. The functionality is focused on permutation calculation and value determination based on constraints, but the absence of parameter passing needs to be addressed.

