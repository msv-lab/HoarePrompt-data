#State of the program right berfore the function call: **x and y are integers such that 3 ≤ y < x ≤ 100,000.**
def func():
    x, y = map(int, input().split())
    print((x - y) // 2 + (x - y) % 2)
#Overall this is what the function does:The function `func` reads two integer values `x` and `y` from the input, ensuring that 3 ≤ y < x ≤ 100,000. It then calculates the result of ((x - y) // 2) + ((x - y) % 2) and prints the output. The function does not return any value, but it performs the calculation based on the provided input constraints.

