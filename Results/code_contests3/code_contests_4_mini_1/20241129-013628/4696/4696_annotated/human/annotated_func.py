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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 50; `i` is the final value after all updates; `p` is an empty list.
#Overall this is what the function does:The function accepts two integers, `n` (ranging from 1 to 50) and `i` (adjusted to be zero-based), via input. It calculates the `i`-th permutation of the integers from 1 to `n` using factorial-based indexing. The function does not return a value; instead, it prints the elements of the permutation in order. If `i` exceeds the number of permutations for the given `n`, the function may lead to an index error when attempting to access `p[d]`. Therefore, users must ensure that `i` is within the valid range to avoid errors.

