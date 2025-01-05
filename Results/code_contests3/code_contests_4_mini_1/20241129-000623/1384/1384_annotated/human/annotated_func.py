#State of the program right berfore the function call: T is an integer such that 1 <= T <= 100, and X is an integer such that 1 <= X <= 100.
def func():
    t, x = map(float, input().split())
    print(t / x)
#Overall this is what the function does:The function does not accept parameters and reads two floating-point numbers from user input. It then calculates and prints the result of dividing the first number by the second. If the second number is zero, a division by zero error will occur, but the function does not handle this case. The function assumes that the inputs are constrained between 1 and 100, but it does not enforce these constraints.

