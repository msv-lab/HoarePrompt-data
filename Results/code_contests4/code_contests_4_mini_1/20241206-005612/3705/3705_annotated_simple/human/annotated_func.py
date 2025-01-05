#State of the program right berfore the function call: l and r are positive integers such that 1 ≤ l ≤ r ≤ 10^18.
def func_1(n):
    f = 0
    s = 0
    p = 1
    if (n == 0) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *`l` is a positive integer, `r` is a positive integer, `f` is 0, `s` is 0, `p` is 1, and `n` is not equal to 0
    for i in range(100):
        if i % 2:
            s += min(p, n)
        else:
            f += min(p, n)
        
        n -= p
        
        if n <= 0:
            break
        
        p *= 2
        
    #State of the program after the  for loop has been executed: `l` and `r` are positive integers; `p` is 2 raised to the number of iterations executed; `n` is less than or equal to 0; `f` is the sum of contributions for even `i`; `s` is the sum of contributions for odd `i`.
    return f * f + s * (s + 1)
    #The program returns the result of f squared plus s multiplied by (s plus 1), where f is the sum of contributions for even i and s is the sum of contributions for odd i
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns 0 if `n` is 0. For positive values of `n`, it computes two sums: `f`, which is the sum of contributions for even indices, and `s`, which is the sum of contributions for odd indices, based on the powers of 2. Finally, it returns the value of `f` squared plus `s` multiplied by `(s + 1)`. The loop iterates at most 100 times, and it breaks early if `n` becomes non-positive.

