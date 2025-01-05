#State of the program right berfore the function call: n and m are integers such that 1 <= m <= cntn, where cntn is the number of permutations of length n with maximum possible value of f(p).**
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= m <= cntn, `m` is an integer such that 1 <= m <= cntn, `a` and `b` are assigned values after splitting the input string, `i` is an integer value obtained from `b` decreased by 1, `p` is an empty range, `f` is the factorial of `n - n`, `d` is the result of `i // f`, and `i` is 0
#Overall this is what the function does:The function takes two integer inputs `n` and `m`, calculates the number of permutations of length `n`, and then iterates through these permutations to find the maximum possible value of `f(p)` based on the given constraints. It prints out the calculated values as it iterates through the permutations. There is a missing `factorial` function in the code that calculates the factorial of a number. The function does not return any value explicitly.

