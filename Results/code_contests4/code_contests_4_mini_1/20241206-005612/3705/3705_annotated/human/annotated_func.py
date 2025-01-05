#State of the program right berfore the function call: l and r are integers such that 1 ≤ l ≤ r ≤ 10^18.
def func_1(n):
    f = 0
    s = 0
    p = 1
    if (n == 0) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *`l` and `r` are integers such that 1 ≤ `l` ≤ `r` ≤ 10^18; `f` is 0; `s` is 0; `p` is 1; `n` is not equal to 0
    for i in range(100):
        if i % 2:
            s += min(p, n)
        else:
            f += min(p, n)
        
        n -= p
        
        if n <= 0:
            break
        
        p *= 2
        
    #State of the program after the  for loop has been executed: `l` and `r` are integers such that 1 ≤ `l` ≤ `r` ≤ 10^18; `s` is the sum of contributions from odd indexed iterations, `f` is the sum of contributions from even indexed iterations, `n` is less than or equal to 0, `p` is 2 raised to the number of iterations executed (or at most 2^100 if no break occurs).
    return f * f + s * (s + 1)
    #The program returns the value calculated from the expression f * f + s * (s + 1), where 'f' is the sum of contributions from even indexed iterations and 's' is the sum of contributions from odd indexed iterations.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns 0 if `n` is 0. If `n` is greater than 0, it calculates the sums of contributions from even and odd indexed iterations of a loop, where the contributions are determined by the powers of 2, and returns the result of the expression `f * f + s * (s + 1)`, where `f` is the sum from even indexed iterations and `s` is the sum from odd indexed iterations. The loop runs at most 100 times or until `n` becomes non-positive.

