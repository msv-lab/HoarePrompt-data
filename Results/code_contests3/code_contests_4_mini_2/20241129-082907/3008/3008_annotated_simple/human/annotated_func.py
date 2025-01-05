#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^18.
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a string representation of a non-negative integer within the range 0 ≤ n ≤ 10^18; if the last digit of `n` is not zero, then `s` is set to 1. If the last digit of `n` is zero, `s` remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function accepts no parameters, reads a non-negative integer `n` from input as a string, calculates whether the last digit of `n` is non-zero, and prints the result of `2 * (n / 10) + s`, where `s` is 1 if the last digit is non-zero and 0 if it is zero. However, since `n` is treated as a string, this will result in a TypeError during the division operation. The function does not handle this error, leading to a failure in execution.

