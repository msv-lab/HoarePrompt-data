#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^18.
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a string that represents the user input. If the last digit of `n` is not 0, `s` is set to 1. If the last digit of `n` is 0, then `s` remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function accepts no parameters and prompts the user for input, reading it as a string `n`. It checks if the last digit of `n` is not zero; if so, it sets `s` to 1, otherwise `s` remains 0. The function then calculates and prints the result of the expression \(2 \times \left(\frac{n}{10}\right) + s\). Note that the division of `n` is performed on a string, which will result in a TypeError, as `n` should be converted to an integer before performing arithmetic operations. Therefore, the function may encounter an error when executed.

