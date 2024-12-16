#State of the program right berfore the function call: the input to the function is an integer representing the camera angle in degrees, which can be any integer between -10^18 and 10^18 (inclusive), where positive values denote clockwise camera rotation and negative values denote counter-clockwise rotation.
def func():
    x = int(input())
    normalized_angle = x % 360
    turns = (360 - normalized_angle) // 90 % 4
    print(turns)
#Overall this is what the function does:The function reads an integer input from the user representing a camera angle in degrees, normalizes the angle to be within the range of -360 to 360 degrees, calculates the number of 90-degree turns required to reach a specific position based on the normalized angle, and prints the result. However, the function does not handle negative input angles correctly, does not perform any error checking, and does not account for input values outside the range of -10^18 to 10^18.

