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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer based on user input, `k` is `n + 1`, `p` is an empty list, `i` is the final value after all updates, and `f` is `factorial(0)` which is 1.
#Overall this is what the function does:The function accepts user input for two positive integers, `n` (1 ≤ n ≤ 50) and `m`, and calculates the m-th permutation of the integers from 1 to n. It prints each element of the permutation in sequence. However, it does not handle cases where the input is invalid or when `m` exceeds the number of possible permutations (which is n!). The function does not return any value.

