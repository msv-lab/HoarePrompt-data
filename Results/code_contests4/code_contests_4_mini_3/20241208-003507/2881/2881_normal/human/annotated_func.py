#State of the program right berfore the function call: be and en are integers representing the original screen dimensions (a and b) and the desired aspect ratio dimensions (x and y), respectively, where 1 ≤ a, b, x, y ≤ 2·10^9.
def func_1(be, en):
    while be < en:
        mid = (be + en + 1) // 2
        
        if x * mid <= a and y * mid <= b:
            be = mid
        else:
            en = mid - 1
        
    #State of the program after the loop has been executed: `be` is the largest integer such that `x * be <= a` and `y * be <= b`, `en` is equal to `be`, indicating that the loop has terminated with `be` equal to `en`.
    print(be * x, be * y)
#Overall this is what the function does:The function accepts two integers `be` and `en`, which represent the minimum and maximum scaling factors for adjusting screen dimensions based on a specified aspect ratio. It calculates the largest integer scaling factor such that the adjusted dimensions do not exceed the original dimensions (represented by `a` and `b`). The function then prints the adjusted dimensions resulting from this scaling factor. However, it does not return any value; it only prints the results.

