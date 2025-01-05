#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^18.
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a string representation of the user input value. If the last digit of the integer value of `n` is not 0, then `s` is set to 1. Otherwise, `s` remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function accepts no parameters, reads a non-negative integer `n` from user input, and prints the result of the expression `2 * (n / 10) + s`, where `s` is set to 1 if the last digit of `n` is not 0, or 0 if it is. However, since `n` is treated as a string and is used in a division operation, this may lead to a TypeError unless `n` is first converted to an integer. If the input is invalid (e.g., not a numeric string), it will raise an error. Additionally, the function does not handle inputs outside the specified range of 0 to 10^18.

