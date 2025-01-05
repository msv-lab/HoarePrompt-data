#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 50, and m is a positive integer such that 1 ≤ m ≤ cntn, where cntn is the number of permutations of length n with maximum possible value of f(p).
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 50; `k` is `n + 1`; `p` is a list with an undefined number of elements removed; `i` is undefined; `f` is 1.
#Overall this is what the function does:The function accepts two implicit parameters, `n` (a positive integer between 1 and 50) and `m` (a positive integer that must be less than or equal to the number of permutations of length `n`). It computes and prints the `m`-th permutation of the numbers from 1 to `n`. The function does this by calculating factorial values and manipulating a list of numbers but does not return any value to the caller.

