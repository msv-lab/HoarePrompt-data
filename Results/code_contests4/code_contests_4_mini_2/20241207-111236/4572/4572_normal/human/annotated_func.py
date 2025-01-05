#State of the program right berfore the function call: a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    a, b = map(float, raw_input().split())
    if (a < b) :
        print - 1
        exit(0)
    #State of the program after the if block has been executed: *`a` and `b` are floats. If `a` is less than `b`, the program terminates with exit code 0.
    print(a + b) / (2 * math.floor((a + b) / (2 * b)))
#Overall this is what the function does:The function reads two positive integers `a` and `b` from input. If `a` is less than `b`, it prints -1 and terminates the program. Otherwise, it calculates and prints the average of `a` and `b` divided by twice the largest integer less than or equal to the average divided by `b`. The function does not return any value, and its behavior is dependent on the input values.

