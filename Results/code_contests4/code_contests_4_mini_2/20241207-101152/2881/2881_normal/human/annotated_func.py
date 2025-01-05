#State of the program right berfore the function call: be and en are integers representing the original screen dimensions (a, b) and the desired ratio (x, y) respectively, such that 1 ≤ a, b, x, y ≤ 2·10^9.
def func_1(be, en):
    while be < en:
        mid = (be + en + 1) // 2
        
        if x * mid <= a and y * mid <= b:
            be = mid
        else:
            en = mid - 1
        
    #State of the program after the loop has been executed: `be` is the largest integer such that `x * be <= a` and `y * be <= b`, `en` is equal to `be`, indicating that the loop has terminated when `be` equals `en`.
    print(be * x, be * y)
#Overall this is what the function does:The function accepts two integer parameters `be` and `en`, which represent the lower and upper bounds for scaling dimensions based on a desired ratio. It calculates the maximum scaling factor `mid` such that scaling the original dimensions `a` and `b` by `mid` results in dimensions that do not exceed the original screen size. The function prints the scaled dimensions. However, the code is missing the definitions for `a`, `b`, `x`, and `y`, which are necessary for the calculations to work correctly. Therefore, the function lacks completeness as it relies on undefined variables.

