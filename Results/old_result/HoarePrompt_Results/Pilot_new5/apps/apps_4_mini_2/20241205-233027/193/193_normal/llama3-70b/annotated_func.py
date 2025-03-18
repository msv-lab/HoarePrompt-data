#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100,000.
def func():
    x, y = map(int, input().split())
    print(abs(x - y))
#Overall this is what the function does:The function accepts two integers `x` and `y` from input, where it is assumed that 3 ≤ y < x ≤ 100,000, and it calculates and prints the absolute difference between `x` and `y`. There are no checks for the constraints, so if the input does not meet the conditions, the function may still operate but it could lead to unexpected results.

