#State of the program right berfore the function call: x is an integer such that -10^18 ≤ x ≤ 10^18, representing the camera rotation angle in degrees.
def func():
    x = int(input())
    normalized_angle = x % 360
    turns = (360 - normalized_angle) // 90 % 4
    print(turns)
#Overall this is what the function does:The function accepts an integer input representing the camera rotation angle in degrees, normalizes it within the range of 0 to 359 degrees, calculates how many 90-degree turns are needed to return to the original direction, and prints this number. The function does not accept any parameters directly; instead, it reads the value from user input. It handles a range of values for the angle from -10^18 to 10^18, correctly normalizing negative angles as well.

