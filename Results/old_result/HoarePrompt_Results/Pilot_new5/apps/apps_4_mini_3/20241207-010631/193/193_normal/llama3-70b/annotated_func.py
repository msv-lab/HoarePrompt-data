#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100,000.
def func():
    x, y = map(int, input().split())
    print(abs(x - y))
#Overall this is what the function does:The function accepts two integers `x` and `y` through user input, where the constraints are that `3 ≤ y < x ≤ 100,000`. It calculates and prints the absolute difference between `x` and `y`. The function does not return any value.

