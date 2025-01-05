#State of the program right berfore the function call: a, b, x, and y are positive integers such that 1 ≤ a, b, x, y ≤ 2·10^9.
def func_1(be, en):
    while be < en:
        mid = (be + en + 1) // 2
        
        if x * mid <= a and y * mid <= b:
            be = mid
        else:
            en = mid - 1
        
    #State of the program after the loop has been executed: `be` is equal to the maximum integer such that `x * be <= a` and `y * be <= b`, `en` is equal to `be` if the loop executes at least once, otherwise it is equal to the original value of `en`, `a` is a positive integer, `b` is a positive integer, `x` is a positive integer, and `y` is a positive integer.
    print(be * x, be * y)
#Overall this is what the function does:The function accepts two positive integer parameters `be` and `en`, and uses a binary search algorithm to find the maximum integer `be` such that `x * be` is less than or equal to `a` and `y * be` is less than or equal to `b`. It then prints the products `be * x` and `be * y`. If no suitable `be` can be found, it may print `0` for the products if the initial values of `be` and `en` do not allow for any valid integer to be found.

