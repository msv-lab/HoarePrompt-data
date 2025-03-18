#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100,000.
def func():
    x, y = map(int, input().split())
    print((x - y) // 2 + (x - y) % 2)
#Overall this is what the function does:The function accepts two integers `x` and `y`, which are read from standard input with the constraints 3 ≤ y < x ≤ 100,000. It calculates and prints the result of the expression ((x - y) // 2) + ((x - y) % 2), which effectively computes the number of ways to distribute the difference between `x` and `y` into pairs, considering any remaining single unit when the difference is odd.

