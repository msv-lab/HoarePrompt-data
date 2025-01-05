#State of the program right berfore the function call: n and m are integers such that 1 <= m <= cntn, where cntn is the number of permutations of length n with the maximum possible value of f(p).**
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= n <= cntn, `a` and `b` are the input values after splitting, `i` is an updated integer based on the input value of b - 1, `p` is an empty list, `k` is equal to n + 1, `f` is the factorial of 0, `d` is the result of the floor division of `i` by `f` (which is 0), and all values have been processed and removed from `p`.
#Overall this is what the function does:The function takes user input for integers `a` and `b`, where `a` represents the length of permutations and `b` is modified by subtracting 1. It then calculates the maximum possible value of f(p) for permutations of length `n` based on certain constraints. The function iterates through a loop to compute values and remove processed elements from a list `p`.

