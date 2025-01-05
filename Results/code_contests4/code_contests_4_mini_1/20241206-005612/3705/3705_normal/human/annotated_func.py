#State of the program right berfore the function call: l and r are integers such that 1 ≤ l ≤ r ≤ 10^18.
def func_1(n):
    f = 0
    s = 0
    p = 1
    if (n == 0) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *`l` and `r` are integers such that 1 ≤ `l` ≤ `r` ≤ 10^18; `f` is 0; `s` is 0; `p` is 1; and `n` is not equal to 0
    for i in range(100):
        if i % 2:
            s += min(p, n)
        else:
            f += min(p, n)
        
        n -= p
        
        if n <= 0:
            break
        
        p *= 2
        
    #State of the program after the  for loop has been executed: `l` and `r` are integers such that 1 ≤ `l` ≤ `r` ≤ 10^18; `f` is equal to the sum of the minimum values of powers of 2 and `n` at each even iteration, `s` is equal to the sum of the minimum values of powers of 2 and `n` at each odd iteration, `n` is less than or equal to 0, and `p` is the smallest power of 2 that exceeds `n` when it becomes less than or equal to 0.
    return f * f + s * (s + 1)
    #The program returns the value of f squared plus s times (s plus 1), where f is the sum of the minimum values of powers of 2 and n at each even iteration, and s is the sum of the minimum values of powers of 2 and n at each odd iteration.
#Overall this is what the function does:The function accepts an integer `n` and returns 0 if `n` is 0. If `n` is positive, it computes two sums, `f` and `s`, based on the minimum values of powers of 2 (incremented in a loop) and the remaining value of `n` at each iteration. The function then returns the value of `f` squared plus `s` times `(s + 1)`. The loop runs a maximum of 100 times or until `n` becomes less than or equal to 0, effectively handling cases where `n` is large, up to \(10^{18}\).

