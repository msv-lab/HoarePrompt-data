#State of the program right berfore the function call: T is an integer such that 1 <= T <= 100, and X is an integer such that 1 <= X <= 100.
def func():
    t, x = map(float, input().split())
    print(t / x)
#Overall this is what the function does:The function accepts no parameters, reads two floating-point numbers from input, and prints the result of dividing the first number by the second. If the second number is zero, this will result in a division by zero error, which is not handled in the code. The function operates under the assumption that the inputs are constrained between 1 and 100, but this is not enforced in the code itself.

