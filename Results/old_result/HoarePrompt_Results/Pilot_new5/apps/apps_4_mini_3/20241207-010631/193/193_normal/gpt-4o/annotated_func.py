#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100,000.
def func():
    x, y = map(int, input().split())
    print((x - y) // 2 + (x - y) % 2)
#Overall this is what the function does:The function accepts two integers `x` and `y` as input, where `3 ≤ y < x ≤ 100,000`, and calculates the result of the expression `(x - y) // 2 + (x - y) % 2`. It then prints the result, which effectively computes the ceiling of half of the difference between `x` and `y`. The function does not return any value.

