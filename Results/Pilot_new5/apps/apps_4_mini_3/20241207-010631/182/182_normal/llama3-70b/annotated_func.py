#State of the program right berfore the function call: x is an integer such that -10^18 ≤ x ≤ 10^18, representing the camera angle in degrees, where positive values indicate clockwise rotation and negative values indicate counter-clockwise rotation.
def func():
    x = int(input())
    x = x % 360
    if (x == 0) :
        print(0)
    else :
        print((x + 90 - 1) // 90 % 4)
    #State of the program after the if-else block has been executed: *`x` is an integer such that -10^18 ≤ `x` ≤ 10^18 and in the range [0, 359]. If `x` is 0, then 0 has been printed. If `x` is not equal to 0, the output of the expression is either 1, 2, or 0 based on the value of `x`.
#Overall this is what the function does:The function accepts an integer input `x`, representing the camera angle in degrees, where -10^18 ≤ x ≤ 10^18. It normalizes `x` to the range [0, 359] by taking `x % 360`. If the normalized angle is 0, it prints 0. If the angle is not 0, it calculates and prints the quadrant of the angle based on its value, returning 1 for angles between 1-89, 2 for angles between 90-179, 3 for angles between 180-269, and 0 for angles between 270-359. Edge cases include large negative and positive values of `x`, which are effectively wrapped to the corresponding angle within the 0-359 range.

