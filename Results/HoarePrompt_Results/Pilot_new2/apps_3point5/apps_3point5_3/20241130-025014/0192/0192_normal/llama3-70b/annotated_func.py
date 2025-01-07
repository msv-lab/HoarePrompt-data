#State of the program right berfore the function call: **x and y are integers such that 3 <= y < x <= 100,000.**
def func():
    x, y = map(int, input().split())
    print(abs(x - y))
#Overall this is what the function does:The function `func` reads two integers `x` and `y` from the input, calculates the absolute difference between them, and prints the result. The function does not accept any parameters. The functionality of the function is to calculate and print the absolute difference between `x` and `y`. It assumes that `x` and `y` are integers such that 3 <= y < x <= 100,000.

