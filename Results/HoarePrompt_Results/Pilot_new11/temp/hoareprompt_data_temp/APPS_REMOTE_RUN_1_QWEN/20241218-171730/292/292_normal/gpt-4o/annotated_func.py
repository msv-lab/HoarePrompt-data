#State of the program right berfore the function call: a and b are positive integers such that 1 <= a <= b <= 10.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is a_original * 3^years, `b` is b_original * 2^years, `years` is the number of times the loop executed.
    print(years)
#Overall this is what the function does:The function processes two positive integers `a` and `b` (where \(1 \leq a \leq b \leq 10\)) and calculates the minimum number of years required for `a` to become greater than `b` through repeated tripling of `a` and doubling of `b`. It then prints this number of years. If `a` is already greater than `b` at the start, the function will still execute the loop once to update `a` and `b`, but the number of years will be reported as 1. There are no explicit return parameters; the function directly outputs the result.

