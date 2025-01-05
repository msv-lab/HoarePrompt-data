#State of the program right berfore the function call: T is an integer such that 1 <= T <= 100, and X is an integer such that 1 <= X <= 100.
def func():
    t, x = map(float, input().split())
    print(t / x)
#Overall this is what the function does:The function accepts no parameters, reads two float values from input, and prints the result of dividing the first value by the second. However, the function does not handle the scenario where the second value (X) is zero, which would result in a division by zero error. Additionally, the input values are expected to be integers within the range of 1 to 100, but the function does not enforce these constraints.

