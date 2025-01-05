#State of the program right berfore the function call: a, b, x, and y are positive integers such that 1 ≤ a, b, x, y ≤ 2·10^9.**
def func_1(be, en):
    while be < en:
        mid = (be + en + 1) // 2
        
        if x * mid <= a and y * mid <= b:
            be = mid
        else:
            en = mid - 1
        
    #State of the program after the loop has been executed: `mid` is a positive integer, `a`, `b`, `x`, `y`, `be`, `en` are positive integers. After the loop finishes executing, `be` will be equal to the maximum value of `mid` such that `x * mid <= a` and `y * mid <= b`, while `en` will be equal to the maximum value of `mid` minus 1.
    print(be * x, be * y)
#Overall this is what the function does:The function `func_1` calculates the maximum value of `mid` such that `x * mid <= a` and `y * mid <= b` within the range of `be` and `en`. The function does not return any specific output but prints the product of the maximum valid `mid` values with `x` and `y` respectively. The function takes two positive integer parameters `be` and `en` where 1 ≤ be, en ≤ 2·10^9.

