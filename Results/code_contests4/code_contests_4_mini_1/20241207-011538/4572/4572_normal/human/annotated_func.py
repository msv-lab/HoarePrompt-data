#State of the program right berfore the function call: a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    a, b = map(float, raw_input().split())
    if (a < b) :
        print - 1
        exit(0)
    #State of the program after the if block has been executed: *`a` and `b` are floats derived from input; if `a` is less than `b`, the output is -1 and the program exits without further processing.
    print(a + b) / (2 * math.floor((a + b) / (2 * b)))
#Overall this is what the function does:The function accepts two positive integers `a` and `b` from user input. If `a` is less than `b`, it outputs `-1` and exits the program. Otherwise, it calculates and prints the result of the expression `(a + b) / (2 * floor((a + b) / (2 * b)))`. The function does not handle cases where the input might be non-integer or if the division results in errors, such as division by zero, since it relies on valid input as per the specified constraints.

