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
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 0, `i` is the remainder of `i` divided by `f`, `p` is an empty range as all elements have been removed, `k` is n+1, `f` is the factorial of 0 which is 1, `d` is the floor division of `i` by `f`
#Overall this is what the function does:The function takes input for two positive integers n and m, where m is between 1 and the number of permutations of length n with the maximum possible value of f(p). It then performs a series of calculations to find a positive integer m based on the constraints provided. The function calculates the number of permutations of length n and finds the maximum possible value of f(p).

