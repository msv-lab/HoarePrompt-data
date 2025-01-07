#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100,000.
def func():
    x, y = map(int, input().split())
    print((x - y) // 2 + (x - y) % 2)
#Overall this is what the function does:The function accepts two integers `x` and `y` from user input, constrained such that 3 ≤ y < x ≤ 100,000. It calculates and prints the value of `(x - y) // 2 + (x - y) % 2`, which effectively computes the ceiling of half the difference between `x` and `y`. The function does not return a value but prints the computed result directly.

