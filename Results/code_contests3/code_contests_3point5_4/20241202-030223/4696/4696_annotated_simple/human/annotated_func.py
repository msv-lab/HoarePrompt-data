#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ m ≤ cntn, where cntn is the number of permutations of length n with maximum possible value of f(p).**
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
        
    #State of the program after the  for loop has been executed: n is a positive integer, m is a positive integer with 1 ≤ m ≤ cntn, cntn is a positive integer, a and b are assigned values obtained from splitting the raw input string, i is an integer value of `b` decremented by 1, p is an empty list, k is n for the loop to execute the final time, f is the factorial of 0, d is assigned the value of i, `i` is 0
#Overall this is what the function does:The function `func` reads two integers `n` and `m` from the user input, calculates the number of permutations of length `n`, and determines the maximum possible value of `f(p)`. It then performs a series of operations based on these values to manipulate a list `p`. The code does not explicitly return any value.

