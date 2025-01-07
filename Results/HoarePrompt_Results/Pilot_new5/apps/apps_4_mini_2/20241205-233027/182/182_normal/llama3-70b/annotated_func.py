#State of the program right berfore the function call: x is an integer such that -10^18 ≤ x ≤ 10^18.
def func():
    x = int(input())
    x = x % 360
    if (x == 0) :
        print(0)
    else :
        print((x + 90 - 1) // 90 % 4)
    #State of the program after the if-else block has been executed: *`x` is equal to `x % 360`, where `x` is between 0 and 359 if originally non-negative, or between -359 and 0 if originally negative. If `x` is equal to 0, the function will output 0. Otherwise, it will print either 1, 2, or 3 based on the value of `x`.
#Overall this is what the function does:The function accepts no parameters and prompts the user for an integer input `x`, which is then constrained to the range [0, 359] by taking `x % 360`. It prints 0 if `x` is 0; otherwise, it prints an integer from the set {1, 2, 3} based on the value of `x`. The printout value corresponds to the sector in a circle divided into four quadrants (90-degree segments). If the input is negative, it effectively reduces the input into the positive equivalent within the range of 0 to 359, but does not handle cases where `x` is directly outside the specified range.

