#State of the program right berfore the function call: n is a non-negative integer.**
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a non-negative integer inputted by the user. If the last digit of `n` is not 0, then `s` is updated to 1. Otherwise, `s` remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function prompts the user to input a non-negative integer `n`, checks if the last digit of `n` is not 0, updates `s` to 1 in that case, and then prints the result of the mathematical expression 2 * (n / 10) + s. The function does not accept any parameters and does not return any output.

