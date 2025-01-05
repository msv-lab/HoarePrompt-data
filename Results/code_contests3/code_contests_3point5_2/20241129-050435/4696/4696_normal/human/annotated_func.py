#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ m ≤ cntn, where cntn is the number of permutations of length n with the maximum possible value of f(p).**
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` and `b` are assigned values from user input, `i` is the remainder of the previous value of `i` divided by `f`, list `p` is empty
#Overall this is what the function does:The function takes user input for integers `n` and `m`, performs calculations on permutations based on the values of `n` and `m`, and outputs the results. It calculates the value of `f(p)` for each permutation `p` and prints the corresponding values based on the given constraints. The function handles permutations, factorials, and index calculations to determine the output.

