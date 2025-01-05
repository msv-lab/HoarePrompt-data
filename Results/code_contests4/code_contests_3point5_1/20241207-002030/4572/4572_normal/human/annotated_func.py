#State of the program right berfore the function call: a and b are positive integers such that 1 ≤ a, b ≤ 10^9.**
def func():
    a, b = map(float, raw_input().split())
    if (a < b) :
        print - 1
        exit(0)
    #State of the program after the if block has been executed: *`a` and `b` are positive floating-point numbers. If `a` is less than `b`, the program encounters a syntax error when executing the code snippet `print -1`. Otherwise, there is no change in the state of the variables after the execution of the if else block.
    print(a + b) / (2 * math.floor((a + b) / (2 * b)))
#Overall this is what the function does:The function `func` reads two positive floating-point numbers `a` and `b` as input. If `a` is less than `b`, it prints -1 and exits the program. Otherwise, it calculates (a + b) / (2 * floor((a + b) / (2 * b))) and prints the result. The function does not explicitly return any value. However, it misses importing the `math` module for the floor function, which may lead to a NameError during execution.

