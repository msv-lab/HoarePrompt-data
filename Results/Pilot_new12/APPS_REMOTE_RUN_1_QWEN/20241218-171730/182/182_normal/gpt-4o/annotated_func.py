#State of the program right berfore the function call: x is an integer such that -10^18 ≤ x ≤ 10^18, representing the camera angle in degrees where positive values denote clockwise rotation and negative values denote counter-clockwise rotation.
def func():
    x = int(input())
    normalized_angle = x % 360
    turns = (360 - normalized_angle) // 90 % 4
    print(turns)
#Overall this is what the function does:The function reads an integer `x` representing the camera angle in degrees. It then normalizes this angle to a value between 0 and 359 using modulo 360 operation. Next, it calculates the number of turns needed to align the camera by dividing the difference between 360 and the normalized angle by 90, and taking the result modulo 4 to ensure it is within the range of 0 to 3. The function prints the number of turns required. The function does not return any value. Note that the function does not check if the input `x` is within the range \([-10^{18}, 10^{18}]\), which could lead to unexpected behavior if the input is outside this range.

