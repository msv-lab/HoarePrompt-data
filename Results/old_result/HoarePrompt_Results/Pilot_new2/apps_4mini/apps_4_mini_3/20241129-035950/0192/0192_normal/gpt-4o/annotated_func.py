#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100000.
def func():
    x, y = map(int, input().split())
    print((x - y) // 2 + (x - y) % 2)
#Overall this is what the function does:The function accepts no direct parameters and reads two integers `x` and `y` from input, where `3 ≤ y < x ≤ 100000`. It computes and prints the result of the expression `(x - y) // 2 + (x - y) % 2`, which effectively calculates the ceiling value of `(x - y) / 2`. This may produce unexpected results if the constraints on `x` and `y` are not strictly adhered to.

