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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 50; `k` is `n + 1`; `f` is 1; `d` is the final value of `i` after all iterations; `p` is an empty list; `i` has been modified through the loop.
#Overall this is what the function does:The function accepts two positive integers `n` (1 ≤ n ≤ 50) and `i` (1 ≤ i ≤ cntn, where cntn is the number of permutations of length `n`). It calculates and prints the `i`-th permutation of the sequence of integers from 1 to `n` in lexicographical order. The function does not return any value.

