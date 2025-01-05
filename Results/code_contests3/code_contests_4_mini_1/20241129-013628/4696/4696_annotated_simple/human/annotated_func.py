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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `k` is `n`, `f` is `1`, `d` is equal to the final value of `i`, `p` is an empty list, and `i` is `0`.
#Overall this is what the function does:The function processes input values `n` and `m` to generate and print the `m`-th permutation of a sequence of integers from 1 to `n`. It does not return any value. The input `n` must be a positive integer between 1 and 50, and `m` must be a positive integer within the range of the total number of permutations of length `n`. The function does not handle cases where `m` exceeds the number of permutations, which could lead to an IndexError when trying to access an invalid index in the list.

