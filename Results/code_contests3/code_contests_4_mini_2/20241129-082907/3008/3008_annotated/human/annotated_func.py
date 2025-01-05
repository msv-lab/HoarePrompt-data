#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^18.
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a string containing user input, and `s` is 0. If the last digit of `n` is not 0, then `s` is set to 1. If the last digit of `n` is 0, `s` remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function accepts a non-negative integer input `n` (via user input), checks if the last digit of `n` is not zero, and sets a variable `s` to 1 if it isn't. It then prints the result of the expression `2 * (n / 10) + s`. However, the function does not return a value, and since `n` is treated as a string, this may lead to issues when performing arithmetic operations; it should be converted to an integer first. Additionally, if `n` is 0, the output will just be `0`. The function lacks proper error handling for input conversion and assumes that the input will always be a valid non-negative integer string.

