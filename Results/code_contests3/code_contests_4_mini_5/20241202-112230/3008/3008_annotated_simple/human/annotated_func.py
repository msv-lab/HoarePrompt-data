#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^18.
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is an input string. If the last digit of `n` is not 0, then `s` is set to 1. Otherwise, `s` remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function accepts no parameters and reads a non-negative integer `n` from user input. If the last digit of `n` is not 0, it sets a variable `s` to 1; otherwise, `s` remains 0. The function then prints the result of the expression `2 * (n / 10) + s`. However, the input `n` is treated as a string, which may lead to a TypeError when attempting to perform arithmetic operations. Therefore, the functionality is to read an input value and print a calculation based on that value, but it may fail due to input type issues.

