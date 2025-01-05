#State of the program right berfore the function call: n and m are integers such that 1 ≤ m ≤ cntn, where cntn is the number of permutations of length n with maximum possible value of f(p).**
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
        
    #State of the program after the  for loop has been executed: `a` holds the value entered by the user, `b` holds the value entered by the user decremented by 1, `n` is an integer value of `a`, `i` is 0, `k` is equal to `n`, `f` is the factorial of `a - n`, `d` is the result of `i` divided by `f` for the last iteration, the loop has printed and removed all values in list `p` in the order determined by the calculations, `p` is now an empty list.
#Overall this is what the function does:The function accepts user input values for `n` and `m`, where `m` is decremented by 1. It then calculates the number of permutations of length `n` with a maximum possible value of f(p). The function iterates through a loop, performing factorial calculations, division, printing values, and removing elements from a list `p`. At the end of the loop, `p` becomes an empty list.

