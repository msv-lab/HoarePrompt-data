#State of the program right berfore the function call: There is an integer input representing the camera angle in degrees, where positive values denote clockwise camera rotation and negative values denote counter-clockwise rotation, and the angle is in the range -10^18 ≤ x ≤ 10^18.
def func():
    x = int(input())
    normalized_angle = x % 360
    turns = (360 - normalized_angle) // 90 % 4
    print(turns)
#Overall this is what the function does:The function accepts an integer input representing the camera angle in degrees, validates it within the range -10^18 ≤ x ≤ 10^18, normalizes the angle to a value between 0 and 359, calculates the number of 90-degree turns required to reach the nearest 90-degree mark in the clockwise direction, and prints the result as an integer value. The function does not handle non-integer inputs, and it assumes the input will always be provided when the function is called. It does not return a value but instead prints the calculated number of turns directly to the output. The final state of the program after it concludes includes the printed result, which represents the minimum number of 90-degree clockwise turns needed from the normalized input angle to reach the nearest 90-degree mark.

