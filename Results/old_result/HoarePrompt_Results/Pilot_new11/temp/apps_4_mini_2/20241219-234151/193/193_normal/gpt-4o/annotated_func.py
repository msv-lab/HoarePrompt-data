#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100,000.
def func():
    x, y = map(int, input().split())
    print((x - y) // 2 + (x - y) % 2)
#Overall this is what the function does:The function reads two integers, x and y, from user input, where the constraints 3 ≤ y < x ≤ 100,000 must be satisfied. It computes and prints the result of the expression \((x - y) // 2 + (x - y) \% 2\), which effectively calculates the ceiling of the half of the difference between x and y. The function does not accept parameters and final output is based solely on the provided input values. Given that there are no checks for input validity within the function, it assumes that the input values will always conform to the specified constraints.

