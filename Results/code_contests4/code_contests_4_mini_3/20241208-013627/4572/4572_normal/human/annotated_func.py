#State of the program right berfore the function call: a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    a, b = map(float, raw_input().split())
    if (a < b) :
        print - 1
        exit(0)
    #State of the program after the if block has been executed: *`a` and `b` are floating-point numbers derived from the input values. If `a` is less than `b`, the program exits with status 0. Otherwise, the program does not execute any further actions.
    print(a + b) / (2 * math.floor((a + b) / (2 * b)))
#Overall this is what the function does:The function reads two floating-point numbers `a` and `b` from input. If `a` is less than `b`, it prints `-1` and exits. If `a` is greater than or equal to `b`, it calculates and prints the result of `(a + b) / (2 * math.floor((a + b) / (2 * b)))`. The function does not return a value but instead prints the result or exits early based on the condition.

