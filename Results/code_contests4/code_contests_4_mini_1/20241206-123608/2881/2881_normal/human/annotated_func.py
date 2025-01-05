#State of the program right berfore the function call: be and en are four integers a, b, x, and y such that 1 ≤ a, b, x, y ≤ 2·10^9.
def func_1(be, en):
    while be < en:
        mid = (be + en + 1) // 2
        
        if x * mid <= a and y * mid <= b:
            be = mid
        else:
            en = mid - 1
        
    #State of the program after the loop has been executed: `be` is equal to `en`, and `x * be` is less than or equal to `a` and `y * be` is less than or equal to `b`.
    print(be * x, be * y)
#Overall this is what the function does:The function accepts two integer parameters, `be` and `en`, and uses a binary search approach to determine the maximum integer `mid` such that `x * mid` is less than or equal to `a` and `y * mid` is less than or equal to `b`. It then prints the results of `be * x` and `be * y`, which represent the maximum possible quantities based on the constraints given by `a`, `b`, `x`, and `y`. The function does not return any value; instead, it prints the results directly.

