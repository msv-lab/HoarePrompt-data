#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100,000.
def func():
    x, y = map(int, input().split())
    print(abs(x - y))
#Overall this is what the function does:The function accepts two integers `x` and `y`, which are input by the user, and calculates the absolute difference between them. It prints the result to the console, but does not return any value. The function assumes that the input integers satisfy the constraints 3 ≤ y < x ≤ 100,000.

