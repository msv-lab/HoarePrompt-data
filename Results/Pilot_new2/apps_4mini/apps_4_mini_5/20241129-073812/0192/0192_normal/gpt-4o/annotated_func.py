#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100,000.
def func():
    x, y = map(int, input().split())
    print((x - y) // 2 + (x - y) % 2)
#Overall this is what the function does:The function accepts two integers, `x` and `y`, such that 3 ≤ y < x ≤ 100,000, and calculates and prints the result of the expression `(x - y) // 2 + (x - y) % 2`. This effectively computes the ceiling of half the difference between `x` and `y`, but it does not return any value. Instead, it directly prints the result to the output.

