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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` and `b` are strings obtained from splitting the input, `i` is not defined, `k` is 2
#Overall this is what the function does:The function `func` reads two integers `n` and `i` from the input, where `n` represents the length of permutations and `i` is a value to compute permutations. It then calculates permutations based on the factorial of `n - k`, where `k` ranges from 1 to `n`. The function prints the permutations and removes elements from the list accordingly. The function does not have a specified return value.

