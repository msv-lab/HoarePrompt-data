#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100000.
def func():
    x, y = map(int, input().split())
    print((x - y) // 2 + (x - y) % 2)
#Overall this is what the function does:The function accepts two integers, `x` and `y`, within the constraints 3 ≤ y < x ≤ 100000, and calculates and prints the result of the expression `(x - y) // 2 + (x - y) % 2`. However, it does not return any output or value to the caller.

