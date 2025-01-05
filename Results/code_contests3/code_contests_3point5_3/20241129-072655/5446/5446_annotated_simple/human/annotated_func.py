#State of the program right berfore the function call: **
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function `func` reads three integer inputs, calculates a value based on these inputs, and prints the result. However, the function does not accept any parameters and does not return any value. It performs a calculation and prints the result without taking any input.

