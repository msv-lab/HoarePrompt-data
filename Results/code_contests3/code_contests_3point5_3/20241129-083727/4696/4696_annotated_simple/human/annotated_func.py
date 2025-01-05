#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ m ≤ cntn, where cntn is the number of permutations of length n with maximum possible value of f(p).**
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
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `i` is the remainder of `i` divided by the factorial of `n - 1`, `p` is an empty list, `k` is equal to `n`, `f` is the factorial of 0, `d` is the result of `i` divided by the factorial of `n - 1` after the last iteration
#Overall this is what the function does:The function takes two inputs, n and m, where n is the length of permutations and m is a positive integer less than or equal to the total number of permutations of length n. It then calculates and prints the m-th permutation based on the factorial calculations and removes elements from the permutation list accordingly. Finally, it prints the result.

