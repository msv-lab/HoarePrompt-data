#State of the program right berfore the function call: The function takes no arguments, but the input to the program is an integer x, where -10^18 ≤ x ≤ 10^18, representing the camera angle in degrees, with positive values denoting clockwise camera rotation and negative values denoting counter-clockwise rotation.
def func():
    x = int(input())
    normalized_angle = x % 360
    turns = (360 - normalized_angle) // 90 % 4
    print(turns)
#Overall this is what the function does:The function calculates and prints the minimum number of 90-degree clockwise turns required to align with the 0-degree position, given a camera angle in degrees as input from the user. It normalizes the input angle to a value between 0 and 359 degrees, then determines the number of turns needed, covering all potential cases, including positive and negative input angles, as well as edge cases where the input angle is a multiple of 360 degrees or exceeds the range of -10^18 to 10^18. After execution, the program's state includes the printed value of the minimum number of turns, and the input variable's value, which is used for calculation but not returned or modified externally.

