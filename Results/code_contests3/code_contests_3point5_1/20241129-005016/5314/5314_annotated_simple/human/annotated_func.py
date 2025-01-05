#State of the program right berfore the function call: **
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `n` is an input integer, `t` is either 0 or negative based on the calculations, `a` is a list of strings from the input, `i` is the total number of iterations performed
    print(i)
#Overall this is what the function does:The function `func` reads an integer `n` and a list of strings `a` as inputs, calculates the total number of iterations `i` based on the values in `a`, and decrements the value of `t` by the result of a specific calculation in each iteration. The function then prints the final value of `i`. There are potential edge cases where the loop might not iterate if `t` is initially 0 or negative, and the code does not handle any errors that might arise from invalid inputs or calculations.

