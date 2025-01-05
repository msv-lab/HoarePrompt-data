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
        
    #State of the program after the  for loop has been executed: `a` is the first part of input, `b` is the second part of input, `n` is the initial integer value, `k` is equal to `n`, `f` is 1, `d` is the last calculated index, `i` is 0, `p` is an empty list.
#Overall this is what the function does:The function reads two integers from input, computes the m-th permutation of the numbers from 1 to n, and prints the permutation. It does not handle cases where m exceeds the number of possible permutations of n.

