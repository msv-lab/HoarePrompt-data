#State of the program right berfore the function call: a, b, x, and y are positive integers such that 1 ≤ a, b, x, y ≤ 2·10^9.**
def func_1(be, en):
    while be < en:
        mid = (be + en + 1) // 2
        
        if x * mid <= a and y * mid <= b:
            be = mid
        else:
            en = mid - 1
        
    #State of the program after the loop has been executed: `a`, `b`, `x`, `y`, `be`, `en`, `mid` are positive integers such that 1 ≤ `a`, `b`, `x`, `y` ≤ 2·10^9. The loop finishes with `be` being the largest possible value such that `x * be` is less than or equal to `a` and `y * be` is less than or equal to `b`, `en` is equal to `be` or `be + 1` depending on the final iteration.
    print(be * x, be * y)
#Overall this is what the function does:The function `func_1` accepts two positive integer parameters `be` and `en` such that 1 ≤ `be`, `en` ≤ 2·10^9. Within the function, it iterates through a while loop to find the largest possible value of `be` where `x * be` is less than or equal to `a` and `y * be` is less than or equal to `b`. The loop updates `be` and `en` accordingly. At the end of the loop, it prints the values `be * x` and `be * y`. The function does not have a return value.

