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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `m` is defined, `a` and `b` are assigned values, `i` is 0, `p` is an empty list, `k` ranges from 1 to n, `f` is the factorial of n, and all elements of the original `p` list have been printed in order
#Overall this is what the function does:The function `func` reads two integers `a` and `b` from the input, where `a` represents the length of permutations and `b` is a value used in calculations. It then calculates the number of permutations of length `n` with the maximum possible value of f(p), removes elements from the list `p` based on calculations, and prints the result. The code does not explicitly return any value.

