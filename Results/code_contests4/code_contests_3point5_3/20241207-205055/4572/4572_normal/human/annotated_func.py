#State of the program right berfore the function call: a and b are positive integers such that 1 <= a, b <= 10^9.**
def func():
    a, b = map(float, raw_input().split())
    if (a < b) :
        print - 1
        exit(0)
    #State of the program after the if block has been executed: *`a` and `b` are unknown float values obtained from the input. If `a` is less than `b`, the program exits with code 0.
    print(a + b) / (2 * math.floor((a + b) / (2 * b)))
#Overall this is what the function does:The function `func` reads two float values `a` and `b` from the input, compares them, and if `a` is less than `b`, it prints -1 and exits with code 0. Then, it calculates a mathematical expression involving `a` and `b` and prints the result. The function does not specify any return value. The code does not handle the case where the input values are not valid floats or if the input is not formatted correctly.

