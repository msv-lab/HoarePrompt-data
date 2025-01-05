#State of the program right berfore the function call: l and r are positive integers such that 1 ≤ l ≤ r ≤ 10^18.
def func_1(n):
    f = 0
    s = 0
    p = 1
    if (n == 0) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *`l` is a positive integer such that 1 ≤ `l` ≤ `r` ≤ 10^18; `r` is a positive integer such that 1 ≤ `l` ≤ `r` ≤ 10^18; `f` is 0; `s` is 0; `p` is 1; `n` is a positive integer (since `n` is not equal to 0)
    for i in range(100):
        if i % 2:
            s += min(p, n)
        else:
            f += min(p, n)
        
        n -= p
        
        if n <= 0:
            break
        
        p *= 2
        
    #State of the program after the  for loop has been executed: `l` and `r` are positive integers such that 1 ≤ `l` ≤ `r` ≤ 10^18; `f` is the sum of the minimums added during even iterations, `s` is the sum of the minimums added during odd iterations; `n` is less than or equal to 0; `p` is 2^100.
    return f * f + s * (s + 1)
    #The program returns the value calculated from f squared plus s multiplied by (s + 1), where f is the sum of the minimums added during even iterations and s is the sum of the minimums added during odd iterations
#Overall this is what the function does:The function accepts a positive integer `n` and returns 0 if `n` is 0. If `n` is greater than 0, it computes two sums: `f`, which accumulates the minimum values during even iterations, and `s`, which accumulates during odd iterations, based on progressively doubling values. The function then returns the result of the calculation `f * f + s * (s + 1)`. The loop iterates a maximum of 100 times or until `n` becomes less than or equal to 0, which can lead to early termination.

