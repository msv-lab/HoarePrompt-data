#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 50) and m is a positive integer (1 ≤ m ≤ cntn), where cntn is the number of permutations of length n with the maximum possible value of f(p).
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `p` is a range from 1 to `n` (inclusive), `i` is undefined.
#Overall this is what the function does:The function accepts two positive integers, `n` (1 ≤ n ≤ 50) and `m` (1 ≤ m ≤ cntn, where cntn is the number of permutations of length n). It computes and prints the m-th permutation of the sequence of integers from 1 to n, based on the factorial number system. However, the function does not return any value; it only prints the result. There are no checks for valid input beyond the assumed constraints, which could lead to issues if the input is outside these bounds.

