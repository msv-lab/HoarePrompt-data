#State of the program right berfore the function call: n is a non-negative integer.**
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a non-negative integer input by the user. If the remainder of `n` divided by 10 is not 0, then `s` is set to 1. Otherwise, there is no change in the values of `n` and `s`
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function prompts the user to input a value for `n`, calculates a value `s` based on whether the remainder of `n` divided by 10 is not 0, and then prints the result of the expression 2 * (n / 10) + s. The function does not accept any parameters and does not return any value.

