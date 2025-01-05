#State of the program right berfore the function call: n is a non-negative integer.**
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a non-negative integer, `s` is 1. If the remainder of dividing `n` by 10 is not 0, then `s` is set to 1. Otherwise, `s` remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function `func` reads an input value `n`, checks if the remainder of dividing `n` by 10 is not 0, sets `s` to 1 in that case, and then prints the result of the expression `2 * (n / 10) + s`. It does not return any value. The code may have potential issues because `input()` returns a string, so the division operation might not work as intended, potentially causing a TypeError.

