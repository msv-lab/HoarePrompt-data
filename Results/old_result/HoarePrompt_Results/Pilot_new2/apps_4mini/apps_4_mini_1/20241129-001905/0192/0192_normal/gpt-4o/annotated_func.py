#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100000.
def func():
    x, y = map(int, input().split())
    print((x - y) // 2 + (x - y) % 2)
#Overall this is what the function does:The function accepts two integers `x` and `y` within the constraints \(3 \leq y < x \leq 100000\). It calculates and prints the result of the expression \((x - y) // 2 + (x - y) \% 2\), which effectively computes the ceiling of half the difference between `x` and `y`. There are no parameters passed to the function directly, and it relies on user input for `x` and `y`. The function does not handle invalid inputs or provide output if the input constraints are violated.

