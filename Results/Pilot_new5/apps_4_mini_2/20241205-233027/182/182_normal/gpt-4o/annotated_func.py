#State of the program right berfore the function call: x is an integer representing the camera angle in degrees, where -10^18 ≤ x ≤ 10^18.
def func():
    x = int(input())
    normalized_angle = x % 360
    turns = (360 - normalized_angle) // 90 % 4
    print(turns)
#Overall this is what the function does:The function accepts no parameters directly but reads an integer input representing a camera angle in degrees (ranging from -10^18 to 10^18). It normalizes this angle within the range of 0 to 359 degrees and calculates how many 90-degree turns counterclockwise are needed to align with the positive x-axis. The result, which is the number of turns, is printed but not returned, meaning the function does not provide a direct output value.

