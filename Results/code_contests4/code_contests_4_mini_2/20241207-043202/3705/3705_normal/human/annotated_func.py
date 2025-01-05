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
        
    #State of the program after the  for loop has been executed: `l` and `r` are positive integers; `f` is equal to the sum of the minimum of `p` and the values of `n` chosen in the even iterations of the loop; `s` is equal to the sum of the minimum of `p` and the values of `n` chosen in the odd iterations of the loop; `p` is equal to the last value multiplied by 2; `n` is less than or equal to 0.
    return f * f + s * (s + 1)
    #The program returns the value of f squared plus s multiplied by (s plus 1), where f is the sum of the minimum of p and the values of n chosen in the even iterations of the loop, and s is the sum of the minimum of p and the values of n chosen in the odd iterations of the loop.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns 0 if `n` is 0. If `n` is greater than 0, it calculates two sums: `f`, which is the sum of the minimum of `p` (which doubles each iteration) and `n` during even iterations, and `s`, which is the sum during odd iterations. The function then returns the result of the calculation `f * f + s * (s + 1)` based on these sums. The loop continues until `n` is decremented to 0 or below, ensuring that the calculations do not exceed the initial value of `n`.

