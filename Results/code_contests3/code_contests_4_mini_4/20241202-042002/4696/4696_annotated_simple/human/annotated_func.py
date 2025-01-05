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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer based on input `a`; `i` is the final updated value after all modulus operations; `p` is an empty list.
#Overall this is what the function does:The function reads two integers from input, `n` and `i`, where `n` represents the length of permutations of the numbers from 1 to `n`, and `i` is an index that is used to determine a specific permutation. The function then calculates and prints the `i`-th permutation of the numbers [1, 2, ..., n] in lexicographic order. It does not return any value. However, it does not handle invalid input scenarios (e.g., `i` being larger than the total number of permutations).

