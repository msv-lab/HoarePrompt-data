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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `p` is an empty list, `i` is updated based on the last iteration's computation, `d` is the last computed value of `i // f`.
#Overall this is what the function does:The function accepts no parameters and reads two integers from input, `n` (where 1 ≤ n ≤ 50) and `i` (where 1 ≤ i ≤ cntn, with cntn being the total number of permutations of length `n`). It calculates the `i`-th permutation of the numbers from 1 to `n` using factorial calculations to determine the correct indices for selection and prints the permutation. The function does not handle invalid input cases or errors related to input parsing.

