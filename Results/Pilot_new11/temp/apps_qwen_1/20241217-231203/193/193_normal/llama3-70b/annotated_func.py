#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100 000.
def func():
    x, y = map(int, input().split())
    print(abs(x - y))
#Overall this is what the function does:The function reads two integers `x` and `y` from standard input, where `3 ≤ y < x ≤ 100,000`. It then calculates the absolute difference between `x` and `y` and prints this value. The function does not return any value but modifies the output stream by printing the result. There are no parameters passed to the function.

