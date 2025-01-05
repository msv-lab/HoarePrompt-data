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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 50; `p` is an empty list; `i` is the final updated value after all iterations.
#Overall this is what the function does:The function accepts two implicit parameters `n` and `m`, calculates the `m`-th permutation of the sequence from 1 to `n`, and prints the elements of the permutation. It does not return a value or validate the input against the number of possible permutations.

