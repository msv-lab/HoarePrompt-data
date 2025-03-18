#State of the program right berfore the function call: x and y are integers such that 3 <= y < x <= 100,000.
def func():
    x, y = map(int, input().split())
    print((x - y) // 2 + (x - y) % 2)
#Overall this is what the function does:The function reads two integers `x` and `y` from standard input where `3 <= y < x <= 100,000`, and prints the floor of the average of `x` and `y`.

