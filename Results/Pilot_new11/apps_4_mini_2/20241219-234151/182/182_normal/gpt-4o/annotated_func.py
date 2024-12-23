#State of the program right berfore the function call: x is an integer representing the camera angle in degrees, where -10^18 ≤ x ≤ 10^18.
def func():
    x = int(input())
    normalized_angle = x % 360
    turns = (360 - normalized_angle) // 90 % 4
    print(turns)
#Overall this is what the function does:The function accepts no parameters directly but reads an integer input from the user, which represents a camera angle in degrees (`x`). It then normalizes this angle to find its equivalent within the range of 0 to 359 degrees. It calculates how many 90-degree turns are needed to align the camera to the nearest reference point (effectively determining how far the angle is from being facing 'up' or 0 degrees). Finally, it prints the number of 90-degree turns required, which can vary from 0 to 3 depending on the input angle's value. The function does not return any value.

