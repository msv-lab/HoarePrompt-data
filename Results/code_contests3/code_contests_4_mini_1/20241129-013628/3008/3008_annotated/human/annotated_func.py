#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^18.
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a non-negative integer such that 0 ≤ `n` ≤ 10^18. If `n` is not divisible by 10, then `s` is set to 1.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function accepts no parameters and reads a non-negative integer `n` from input. It calculates and prints the result of the expression `2 * (n / 10) + s`, where `s` is set to 1 if `n` is not divisible by 10, otherwise `s` is 0. If `n` is 0, the output will be 0. However, the function does not handle invalid input (e.g., non-integer inputs) and relies on `input()` which returns a string, potentially leading to a TypeError when performing arithmetic operations.

