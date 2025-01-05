#State of the program right berfore the function call: be and en are four integers a, b, x, and y such that 1 ≤ a, b, x, y ≤ 2·10^9.
def func_1(be, en):
    while be < en:
        mid = (be + en + 1) // 2
        
        if x * mid <= a and y * mid <= b:
            be = mid
        else:
            en = mid - 1
        
    #State of the program after the loop has been executed: `be` is equal to `en`, which is the maximum integer such that `x * be <= a` and `y * be <= b`.
    print(be * x, be * y)
#Overall this is what the function does:The function accepts two integers `be` and `en` and performs a binary search to find the maximum integer `mid` such that `x * mid` is less than or equal to `a` and `y * mid` is less than or equal to `b`. After determining this maximum value, it prints the products `be * x` and `be * y`. The function does not return any values but outputs the results directly.

