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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer; `k` is `n`; `f` is factorial(0) which is 1; `d` is defined based on the last value of `i // f`; `p` is an empty list; `i` is the remainder after the last division, which is `i % 1`, resulting in `i` being 0.
#Overall this is what the function does:The function accepts no parameters directly but reads two positive integers from input: `n`, which indicates the length of permutations and must be between 1 and 50, and `i`, which specifies a position among the permutations. It then calculates and prints the `i-th` permutation of the sequence `[1, 2, ..., n]` in lexicographic order. The function does not handle cases where `i` exceeds the total number of permutations for the given `n`, which could lead to incorrect behavior or an index error.

