#State of the program right berfore the function call: n is a non-negative integer.**
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`s` is 0 or 1, `n` is an integer. If `n` % 10 is not equal to 0, `s` is updated to 1. Otherwise, `s` remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function `func` reads an input `n`, checks if `n` is not divisible by 10, updates the value of `s` accordingly, and then prints the result of the expression 2 * (n / 10) + s. However, there is a missing logic where the input `n` needs to be converted to an integer type before performing mathematical operations. This missing conversion might lead to unexpected results or errors.

