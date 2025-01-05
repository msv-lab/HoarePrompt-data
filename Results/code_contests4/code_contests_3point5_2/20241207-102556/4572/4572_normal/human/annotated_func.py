#State of the program right berfore the function call: a and b are positive integers such that 1 ≤ a, b ≤ 10^9.**
def func():
    a, b = map(float, raw_input().split())
    if (a < b) :
        print - 1
        exit(0)
    #State of the program after the if block has been executed: *`a` and `b` are positive float values. If `a` is less than `b`, the program exits with a status code of 0.
    print(a + b) / (2 * math.floor((a + b) / (2 * b)))
#Overall this is what the function does:The function `func` reads two float values `a` and `b` from the user input. If `a` is less than `b`, it prints -1 and exits the program. Otherwise, it calculates (a + b) / (2 * floor((a + b) / (2 * b))) and prints the result. The function does not accept any parameters and operates with predefined positive float variables `a` and `b` such that 1 ≤ a, b ≤ 10^9.

