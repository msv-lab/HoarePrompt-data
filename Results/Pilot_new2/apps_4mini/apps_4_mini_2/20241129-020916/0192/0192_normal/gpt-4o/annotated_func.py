#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100,000.
def func():
    x, y = map(int, input().split())
    print((x - y) // 2 + (x - y) % 2)
#Overall this is what the function does:The function accepts two integers `x` and `y` (where \(3 \leq y < x \leq 100,000\)) and prints the ceiling of half the difference between `x` and `y`. It does not return a value and does not handle input errors or constraints directly.

