#State of the program right berfore the function call: T is an integer such that 1 <= T <= 100, and X is an integer such that 1 <= X <= 100.
def func():
    t, x = map(float, input().split())
    print(t / x)
#Overall this is what the function does:The function accepts two integers, T and X, through user input and prints the result of T divided by X. It does not validate the input for division by zero, which could lead to an error if X is 0. The expected behavior is to handle valid integers within the range of 1 to 100, but there is no explicit constraint in the code to enforce this.

