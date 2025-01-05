#State of the program right berfore the function call: l and r are integers such that 1 ≤ l ≤ r ≤ 10^18.**
def func_1(n):
    f = 0
    s = 0
    p = 1
    if (n == 0) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *`f` is `0`, `s` is `0`, `p` is `1`, and `n` is not equal to 0
    for i in range(100):
        if i % 2:
            s += min(p, n)
        else:
            f += min(p, n)
        
        n -= p
        
        if n <= 0:
            break
        
        p *= 2
        
    #State of the program after the  for loop has been executed: `f`, `s`, `p` are integers with updated values, `n` will eventually reach 0 or less, and the loop will break.
    return f * f + s * (s + 1)
    #The program returns the result of f squared plus s multiplied by s plus 1
#Overall this is what the function does:The function `func_1` accepts an integer `n` within the range 1 ≤ l ≤ r ≤ 10^18. It calculates two values `f` and `s` based on the value of `n` in a loop. At the end, it returns the result of `f` squared plus `s` multiplied by `s` plus 1. In Case 1, if `n` is 0, the function returns 0.

