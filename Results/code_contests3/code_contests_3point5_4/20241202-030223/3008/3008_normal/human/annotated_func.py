#State of the program right berfore the function call: **Precondition**: **n is a non-negative integer.**
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is the user input value and `s` is 0. If the remainder of `n` divided by 10 is not equal to 0, `s` is updated to 1.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function prompts the user to input a value for `n`, then checks if the remainder of `n` divided by 10 is not 0. If the condition is met, it updates the variable `s` to 1. Finally, it calculates and prints the result of the expression 2 * (n / 10) + s. The function does not accept any parameters and does not return any value. It does not cover the case where the user enters a non-integer value or handles potential errors related to input validation.

