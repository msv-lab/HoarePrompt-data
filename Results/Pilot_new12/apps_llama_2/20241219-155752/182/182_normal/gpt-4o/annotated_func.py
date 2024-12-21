#State of the program right berfore the function call: the function takes no arguments, but the input to the program is an integer x such that -10^18 ≤ x ≤ 10^18, representing the camera angle in degrees, where positive values denote clockwise camera rotation and negative values denote counter-clockwise rotation.
def func():
    x = int(input())
    normalized_angle = x % 360
    turns = (360 - normalized_angle) // 90 % 4
    print(turns)
#Overall this is what the function does:The function takes an integer input from the user, representing a camera angle in degrees, normalizes this angle to a value between 0 and 360, calculates the number of 90-degree turns required to face the direction opposite to the input angle, and prints this value. The function does not handle any potential errors that may occur during the input process, such as non-integer inputs. The input angle is considered as a clockwise rotation if positive and counter-clockwise rotation if negative. The final state of the program is the printed number of 90-degree turns, with the input angle being normalized to its equivalent orientation in the range of 0 to 360 degrees, but the original input value is not preserved or returned.

