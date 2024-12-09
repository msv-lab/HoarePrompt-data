#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100,000.
def func():
    x, y = map(int, input().split())
    print(abs(x - y))
#Overall this is what the function does:The function accepts two integers `x` and `y` from user input, where 3 ≤ y < x ≤ 100,000, and returns the absolute difference between `x` and `y`. It does not return any values but prints the result directly.

