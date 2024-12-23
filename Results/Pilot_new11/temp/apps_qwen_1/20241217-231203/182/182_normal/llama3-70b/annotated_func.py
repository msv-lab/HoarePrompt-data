#State of the program right berfore the function call: x is an integer such that -10^18 ≤ x ≤ 10^18, representing the camera angle in degrees where positive values denote clockwise rotation and negative values denote counter-clockwise rotation.
def func():
    x = int(input())
    x = x % 360
    if (x == 0) :
        print(0)
    else :
        print((x + 90 - 1) // 90 % 4)
    #State of the program after the if-else block has been executed: `x` is an integer in the range -359 ≤ x < 360. If `x` is 0, the value of `x` remains 0. If `x` is not 0, the value of `x` is printed as 0, 1, 2, or 3 based on the original value of `x`.
#Overall this is what the function does:The function takes an integer input `x` representing a camera angle in degrees, where positive values denote clockwise rotation and negative values denote counter-clockwise rotation. It then computes and prints the equivalent rotation angle within the range of -359 to 359 degrees. Specifically, it first normalizes `x` using modulo 360 to ensure it falls within this range. If `x` is exactly 0, it prints 0. Otherwise, it prints one of 0, 1, 2, or 3 based on the normalized value of `x` adjusted by adding 90 and then taking modulo 90 and finally modulo 4.

